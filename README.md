# flake8-pep604

[![Build Status](https://travis-ci.com/xome4ok/flake8-pep604.svg?branch=master)](https://travis-ci.com/xome4ok/flake8-pep604)
[![PyPI](https://img.shields.io/pypi/v/flake8-pep604)](https://pypi.org/project/flake8-pep604/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flake8-pep604)](https://pypi.org/project/flake8-pep604/)
[![PyPI - License](https://img.shields.io/pypi/l/flake8-pep604)](https://pypi.org/project/flake8-pep604/)

Flake8 plugin to enforce the new `Union` and `Optional` annotation syntax defined in [PEP 604](https://peps.python.org/pep-0604/).

```python
Union[X, Y] = X | Y

Optional[X] = X | None
```

## Installation

```
pip install flake8-pep604
```

or if you use [poetry](https://python-poetry.org/):

```
poetry add --dev flake8-pep604
```

## Usage

## Error list

* ZQ001 Use "A | B" syntax instead of Union (PEP 604)
* ZQ002 Use "A | None" syntax instead of Optional (PEP 604)

## Configuration

There is no way to configure the plugin at the moment.
