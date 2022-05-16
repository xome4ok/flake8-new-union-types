from typing import List, Optional, Union


def f(x: Optional["X"]):
    return x


def g() -> Optional["X"]:
    return 0


def h(x: Optional["X"]):
    return x


def i() -> Optional[Union[int, "X"]]:
    return 0


def j() -> Union[Optional["X"], Optional["Y"]]:
    return X()


def k() -> Optional[List["X"]]:
    return None


class X:
    pass


class Y:
    pass
