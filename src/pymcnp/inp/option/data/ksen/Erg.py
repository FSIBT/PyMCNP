import typing

from ..... import abc
from .... import literal
from ..Ksen import Ksen


class Erg(Ksen):
    """
    Represents erg ksen data options.

    Attributes:
        keyword: erg ksen data option ``r'ERG'`` symbol.
        equals: erg ksen data option ``r'='`` symbol.
        e: erg ksen data option ``e`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'ERG'] = abc.Terminal[r'ERG']('ERG')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    e: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
