import typing

from ..... import abc
from .... import literal
from ..Ksen import Ksen


class Ein(Ksen):
    """
    Represents ein ksen data options.

    Attributes:
        keyword: ein ksen data option ``r'EIN'`` symbol.
        equals: ein ksen data option ``r'='`` symbol.
        e: ein ksen data option ``e`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'EIN'] = abc.Terminal[r'EIN']('EIN')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    e: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
