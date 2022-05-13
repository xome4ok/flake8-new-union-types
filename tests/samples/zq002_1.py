from typing import Optional, Any


def f(x: Optional[int, str]) -> Any:
    return x


def g(x: list[Optional[int]]) -> Any:
    return x


def h() -> Optional[int]:
    return


def i() -> list[Optional[str]]:
    return []


C: Optional[list[int]]
C: Optional[int] = None


class X:
    pass


D: Optional[X]
D: Optional[X] = None


isinstance(C, Optional[int])
