from typing import Any, Union


def f(x: Union[int, str]) -> Any:
    return x


def g(x: list[Union[int, None]]) -> Any:
    return x


def h() -> Union[int, None]:
    return


def i() -> list[Union[int, str]]:
    return []


C: Union[list[int], list[str]]
C: Union[list[int], list[str]] = []


class X:
    pass


D: Union[X, int]
D: Union[X, int] = 1


isinstance(C, Union[int, str])


class T:
    a: Union[int, str]
    b: Union["X", str, int]
