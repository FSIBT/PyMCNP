import typing

from ..... import abc
from ..Embed import Embed


class Filetype(Embed):
    """
    Represents filetype embed data options.

    Attributes:
        keyword: filetype embed data option ``r'FILETYPE'`` symbol.
        equals: filetype embed data option ``r'='`` symbol.
        type: filetype embed data option ``type`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'FILETYPE'] = abc.Terminal[r'FILETYPE']('FILETYPE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    type: typing.Annotated[abc.Terminal, r'(?:ASCII|BINARY)']
