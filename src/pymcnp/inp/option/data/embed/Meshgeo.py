import typing

from ..... import abc
from ..Embed import Embed


class Meshgeo(Embed):
    """
    Represents meshgeo embed data options.

    Attributes:
        keyword: meshgeo embed data option `MESHGEO` symbol.
        equals: meshgeo embed data option `=` symbol.
        format: meshgeo embed data option `format` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'MESHGEO'] | str = abc.Terminal[r'MESHGEO']('MESHGEO')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    format: typing.Annotated[abc.Terminal, r'(?:LNK3DNT|ABAQUS|MCNPUM|HDF5)'] | str
