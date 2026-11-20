import typing

from ..... import abc
from .... import literal
from ..Burn import Burn


class Time(Burn):
    """
    Represents time burn data options.

    Attributes:
        keyword: time burn data option ``r'TIME'`` symbol.
        equals: time burn data option ``r'='`` symbol.
        t: time burn data option ``t`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'TIME'] = abc.Terminal[r'TIME']('TIME')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    t: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
