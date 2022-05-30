import ast
from contextlib import contextmanager, ExitStack
from functools import partial
from typing import Any, Iterator, List, NamedTuple, Optional, Tuple, Type

import attr
import pycodestyle

__version__ = "0.4.1"


Flake8Error = Tuple[int, int, str, Any]


class ExtendedError(NamedTuple):
    lineno: int
    col: int
    message: str
    type: Any
    vars: Tuple[Any, ...]


@attr.s
class PEP604Visitor(ast.NodeVisitor):
    filename: str = attr.ib()
    lines: List[str] = attr.ib()
    errors: List[ExtendedError] = attr.ib(default=attr.Factory(list))
    local_errors: List[ExtendedError] = attr.ib(default=attr.Factory(list))
    context: List[ast.AST] = attr.ib(default=attr.Factory(list))

    @staticmethod
    def _visit_subscript(
        node: ast.Subscript,
    ) -> Optional["Error"]:  # type: ignore
        name = None
        if isinstance(node.value, ast.Name):
            name = node.value.id
        if (
            isinstance(node.value, ast.Attribute)
            and isinstance(node.value.value, ast.Name)
            and node.value.value.id == "typing"
        ):
            name = node.value.attr

        if name == "Union":
            return NU001(node.lineno, node.col_offset)
        if name == "Optional":
            return NU002(node.lineno, node.col_offset)

        return None

    def _context_tracking_generic_visit(self, node: ast.AST) -> Any:
        self.context.append(node)
        super().generic_visit(node)
        self.context.pop()

    @contextmanager
    def context_tracking_generic_visit(self) -> Iterator[None]:
        _generic_visit = self.generic_visit
        self.generic_visit = self._context_tracking_generic_visit  # type: ignore
        self.local_errors.clear()
        yield
        self.generic_visit = _generic_visit  # type: ignore
        self.errors.extend(self.local_errors)

    def visit_Constant(self, node: ast.Constant) -> Any:
        if self.context and isinstance(node.value, str):
            self.local_errors = [NU003(node.lineno, node.col_offset)]

    def visit_Subscript(self, node: ast.Subscript) -> Any:
        stack = ExitStack()
        error = self._visit_subscript(node)
        if error:
            stack.enter_context(self.context_tracking_generic_visit())
            self.local_errors.append(error)
        self.generic_visit(node)
        stack.close()


@attr.s(hash=False)
class PEP604Checker:
    name = "flake8-new-union-types"
    version = __version__

    tree: ast.AST = attr.ib(default=None)
    filename: str = attr.ib(default="(none)")
    lines: List[str] = attr.ib(default=None)
    visitor: Type[PEP604Visitor] = attr.ib(
        init=False, default=attr.Factory(lambda: PEP604Visitor)
    )

    def run(self) -> Iterator[Flake8Error]:
        if not (self.tree and self.lines):
            self.load_file()
        visitor = self.visitor(filename=self.filename, lines=self.lines)
        visitor.visit(self.tree)
        for e in visitor.errors:
            if pycodestyle.noqa(self.lines[e.lineno - 1]):
                continue

            yield self.adapt_error(e)

    @classmethod
    def adapt_error(cls, e: "ExtendedError") -> Flake8Error:
        """Adapt the extended error namedtuple to be compatible with Flake8."""
        return e._replace(message=e.message.format(*e.vars))[:4]

    def load_file(self) -> None:
        """Load the file in a way that auto-detects source encoding and deals
        with broken terminal encodings for stdin.
        Stolen from flake8_import_order because it's good.
        """

        if self.filename in ("stdin", "-", None):
            self.filename = "stdin"
            self.lines = pycodestyle.stdin_get_value().splitlines(True)
        else:
            self.lines = pycodestyle.readlines(self.filename)

        if not self.tree:
            self.tree = ast.parse("".join(self.lines))


Error = partial(partial, ExtendedError, type=PEP604Checker, vars=())


NU001 = Error(message='NU001 Use `Foo | Bar` syntax instead of Union (PEP 604)')
NU002 = Error(
    message='NU002 Use `Foo | None` syntax instead of Optional (PEP 604)'
)
NU003 = Error(
    message='NU003 Present the whole expression as a string to annotate forward refs, e.g. `"int | Foo"` (PEP 604)'
)
