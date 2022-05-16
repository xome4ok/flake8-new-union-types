import pytest

from flake8_new_union_types import PEP604Checker


class TestNU002:
    @pytest.mark.parametrize(
        ("checker", "expected_errors"),
        [("nu002_1.py", 11), ("nu002_2.py", 10)],
        indirect=["checker"],
    )
    def test_it_finds_optional(
        self, checker: PEP604Checker, expected_errors: int
    ) -> None:
        result = checker.run()
        errors = list(result)
        assert len(errors) == expected_errors
        assert all(e[2].startswith("NU002") for e in errors)

    @pytest.mark.parametrize(
        "checker",
        [
            "nu002_3.py",
        ],
        indirect=["checker"],
    )
    def test_it_allows_forward_refs(self, checker: PEP604Checker) -> None:
        result = checker.run()
        errors = list(result)
        assert not errors
