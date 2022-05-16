import pytest

from flake8_new_union_types import PEP604Checker


class TestNU001:
    @pytest.mark.parametrize(
        ("checker", "expected_errors"),
        [("nu001_1.py", 10), ("nu001_2.py", 9)],
        indirect=["checker"],
    )
    def test_it_finds_union(
        self, checker: PEP604Checker, expected_errors: int
    ) -> None:
        result = checker.run()
        errors = list(result)
        assert len(errors) == expected_errors
        assert all(e[2].startswith("NU001") for e in errors)

    @pytest.mark.parametrize(
        "checker",
        [
            "nu001_3.py",
        ],
        indirect=["checker"],
    )
    def test_it_allows_forward_refs(self, checker: PEP604Checker) -> None:
        result = checker.run()
        errors = list(result)
        assert not errors
