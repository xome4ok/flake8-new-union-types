import pytest

from flake8_pep604 import PEP604Checker


class TestZQ001:
    @pytest.mark.parametrize(
        ("checker", "expected_errors"),
        [("zq001_1.py", 9), ("zq001_2.py", 9)],
        indirect=["checker"],
    )
    def test_it_finds_union(
        self, checker: PEP604Checker, expected_errors: int
    ) -> None:
        result = checker.run()
        errors = list(result)
        assert len(errors) == expected_errors
        assert all(e[2].startswith("ZQ001") for e in errors)

    @pytest.mark.parametrize(
        "checker",
        [
            "zq001_3.py",
        ],
        indirect=["checker"],
    )
    @pytest.mark.xfail(reason="To be implemented")
    def test_it_allows_forward_refs(self, checker: PEP604Checker) -> None:
        result = checker.run()
        errors = list(result)
        assert not errors
