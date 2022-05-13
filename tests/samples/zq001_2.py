import typing


def f(x: typing.Union[int, str]) -> typing.Any:
    return x


def g(x: list[typing.Union[int, None]]) -> typing.Any:
    return x


def h() -> typing.Union[int, None]:
    return


def i() -> list[typing.Union[int, str]]:
    return []


C: typing.Union[list[int], list[str]]
C: typing.Union[list[int], list[str]] = []


class X:
    pass


D: typing.Union[X, int]
D: typing.Union[X, int] = 1


isinstance(C, typing.Union[int, str])
