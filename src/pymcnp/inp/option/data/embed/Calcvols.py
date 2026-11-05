import typing

from ..... import abc
from ..Embed import Embed


class Calcvols(Embed):
    """
    Represents calcvols embed data options.

    Attributes:
        keyword: calcvols embed data option ``r'CALC_VOLS'`` symbol.
        equals: calcvols embed data option ``r'='`` symbol.
        value: calcvols embed data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'CALC_VOLS'] | str = abc.Terminal[r'CALC_VOLS']('CALC_VOLS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:YES|NO)'] | str
