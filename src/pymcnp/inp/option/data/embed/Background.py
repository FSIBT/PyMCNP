import typing
import dataclasses

from ..... import abc
from ..Embed import Embed
from .... import literal


class Background(Embed):
    """
    Represents background embed data options.

    Attributes:
        keyword: background embed data option `BACKGROUND` symbol.
        equals: background embed data option `=` symbol.
        c: background embed data option `c` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'BACKGROUND'] | str = abc.Terminal[r'BACKGROUND']('BACKGROUND')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    c: literal.Integer | int | str
