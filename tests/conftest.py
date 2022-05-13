from pathlib import Path
from typing import Iterator

import pytest

from flake8_pep604 import PEP604Checker


@pytest.fixture(scope="function")
def checker(request) -> Iterator[PEP604Checker]:
    sample_name = request.param
    source_file = Path("tests/samples") / sample_name

    c = PEP604Checker(filename=str(source_file))
    yield c
