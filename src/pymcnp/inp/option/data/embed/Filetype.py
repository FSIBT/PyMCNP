import typing
import dataclasses

from ..... import abc
from ..Embed import Embed


class Filetype(Embed):
    """
    Represents filetype embed data options.

    Attributes:
        keyword: filetype embed data option `FILETYPE` symbol.
        equals: filetype embed data option `=` symbol.
        type: filetype embed data option `type` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'FILETYPE'] | str = abc.Terminal[r'FILETYPE']('FILETYPE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    type: typing.Annotated[abc.Terminal, r'(?:ASCII|BINARY)'] | str
