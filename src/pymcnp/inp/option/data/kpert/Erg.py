import typing

from ..... import abc
from ..Kpert import Kpert
from .... import literal


class Erg(Kpert):
    """
    Represents erg kpert data options.

    Attributes:
        keyword: erg kpert data option ``r'ERG'`` symbol.
        equals: erg kpert data option ``r'='`` symbol.
        e: erg kpert data option ``e`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'ERG'] = abc.Terminal[r'ERG']('ERG')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    e: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
