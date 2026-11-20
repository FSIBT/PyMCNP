import typing

from ..... import abc
from ..Embed import Embed
from .... import literal


class Background(Embed):
    """
    Represents background embed data options.

    Attributes:
        keyword: background embed data option ``r'BACKGROUND'`` symbol.
        equals: background embed data option ``r'='`` symbol.
        c: background embed data option ``c`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'BACKGROUND'] = abc.Terminal[r'BACKGROUND']('BACKGROUND')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    c: literal.Integer
