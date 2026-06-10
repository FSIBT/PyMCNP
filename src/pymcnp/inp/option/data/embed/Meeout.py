import typing
import dataclasses

from ..... import abc
from ..Embed import Embed


class Meeout(Embed):
    """
    Represents meeout embed data options.

    Attributes:
        keyword: meeout embed data option `MEEOUT` symbol.
        equals: meeout embed data option `=` symbol.
        filename: meeout embed data option `filename` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'MEEOUT'] | str = abc.Terminal[r'MEEOUT']('MEEOUT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    filename: typing.Annotated[abc.Terminal, r'\S+'] | str
