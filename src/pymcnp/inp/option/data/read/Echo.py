import typing

from ..... import abc
from ..Read import Read


class Echo(Read):
    """
    Represents echo read data options.

    Attributes:
        keyword: echo read data option ``r'ECHO'`` symbol.
    """

    keyword: typing.Annotated[abc.Terminal, r'ECHO'] | str = abc.Terminal[r'ECHO']('ECHO')
