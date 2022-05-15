# flake8-new-union-types
[![Build Status](https://github.com/xome4ok/flake8-new-union-types/actions/workflows/check.yml/badge.svg?branch=main)](https://github.com/xome4ok/flake8-new-union-types/actions/workflows/check.yml)
[![PyPI](https://img.shields.io/pypi/v/flake8-new-union-types)](https://pypi.org/project/flake8-new-union-types/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flake8-new-union-types)](https://pypi.org/project/flake8-new-union-types/)
[![PyPI - License](https://img.shields.io/pypi/l/flake8-new-union-types)](https://pypi.org/project/flake8-new-union-types/)

Flake8 plugin to enforce the new `Union` and `Optional` annotation syntax defined in [PEP 604](https://peps.python.org/pep-0604/).

```python
Union[X, Y] = X | Y

Optional[X] = X | None
```

## Installation

```
pip install flake8-new-union-types
```

or if you use [poetry](https://python-poetry.org/):

```
poetry add --dev flake8-new-union-types
```

## Usage

## Error list

* NU001 Use "A | B" syntax instead of Union (PEP 604)
* NU002 Use "A | None" syntax instead of Optional (PEP 604)

## Configuration

There is no way to configure the plugin at the moment.
