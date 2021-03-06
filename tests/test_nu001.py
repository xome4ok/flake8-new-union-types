import pytest

from flake8_new_union_types import PEP604Checker


class TestNU001:
    @pytest.mark.parametrize(
        ("checker", "expected_errors"),
        [("nu001_1.py", 9), ("nu001_2.py", 9)],
        indirect=["checker"],
    )
    def test_it_finds_union(
        self, checker: PEP604Checker, expected_errors: int
    ) -> None:
        result = checker.run()
        errors = list(result)
        assert len(errors) == expected_errors
        assert all(e[2].startswith("NU001") for e in errors)
