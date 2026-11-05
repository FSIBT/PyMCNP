import typing

from ..... import abc
from ..Embed import Embed
from .... import literal


class Length(Embed):
    """
    Represents length embed data options.

    Attributes:
        keyword: length embed data option ``r'LENGTH'`` symbol.
        equals: length embed data option ``r'='`` symbol.
        f: length embed data option ``f`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'LENGTH'] | str = abc.Terminal[r'LENGTH']('LENGTH')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    f: literal.Integer | int | str
