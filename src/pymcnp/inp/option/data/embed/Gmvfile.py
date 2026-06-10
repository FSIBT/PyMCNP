import typing
import dataclasses

from ..... import abc
from ..Embed import Embed


class Gmvfile(Embed):
    """
    Represents gmvfile embed data options.

    Attributes:
        keyword: gmvfile embed data option `GMVFILE` symbol.
        equals: gmvfile embed data option `=` symbol.
        filename: gmvfile embed data option `filename` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'GMVFILE'] | str = abc.Terminal[r'GMVFILE']('GMVFILE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    filename: typing.Annotated[abc.Terminal, r'\S+'] | str
