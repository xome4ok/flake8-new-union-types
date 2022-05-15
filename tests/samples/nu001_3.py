from typing import Union


def f(x: Union["X", int]):
    return x


def g() -> Union["X", int]:
    return 0


def h(x: Union[int, "X"]):
    return x


def i() -> Union[int, "X"]:
    return 0


def j(x: Union["X", "Y"]):
    return x


def k() -> Union["X", "Y"]:
    return X()


class X:
    pass


class Y:
    pass
