import typing

from ..... import abc
from ..Read import Read


class Noecho(Read):
    """
    Represents noecho read data options.

    Attributes:
        keyword: noecho read data option ``r'NOECHO'`` symbol.
    """

    keyword: typing.Annotated[abc.Terminal, r'NOECHO'] | str = abc.Terminal[r'NOECHO']('NOECHO')
