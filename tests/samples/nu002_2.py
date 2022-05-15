import typing


def f(x: typing.Optional[int]) -> typing.Any:
    return x


def g(x: list[typing.Optional[int]]) -> typing.Any:
    return x


def h() -> typing.Optional[int]:
    return


def i() -> list[typing.Optional[str]]:
    return []


C: typing.Optional[list[int]]
C: typing.Optional[int] = None


class X:
    pass


D: typing.Optional[X]
D: typing.Optional[X] = None


isinstance(C, typing.Optional[int])
