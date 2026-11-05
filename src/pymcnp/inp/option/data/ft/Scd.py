import typing

from ..... import abc
from ..Ft import Ft


class Scd(Ft):
    """
    Represents scd ft data options.

    Attributes:
        id: scd group ``r'SCD'`` symbol.
    """

    id: typing.Annotated[abc.Terminal, r'SCD'] | str = abc.Terminal[r'SCD']('SCD')
