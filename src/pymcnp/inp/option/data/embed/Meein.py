import typing

from ..... import abc
from ..Embed import Embed


class Meein(Embed):
    """
    Represents meein embed data options.

    Attributes:
        keyword: meein embed data option ``r'MEEIN'`` symbol.
        equals: meein embed data option ``r'='`` symbol.
        filename: meein embed data option ``filename`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'MEEIN'] | str = abc.Terminal[r'MEEIN']('MEEIN')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    filename: typing.Annotated[abc.Terminal, r'\S+'] | str
