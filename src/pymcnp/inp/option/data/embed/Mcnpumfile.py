import typing

from ..... import abc
from ..Embed import Embed


class Mcnpumfile(Embed):
    """
    Represents mcnpumfile embed data options.

    Attributes:
        keyword: mcnpumfile embed data option ``r'MCNPUMFILE'`` symbol.
        equals: mcnpumfile embed data option ``r'='`` symbol.
        filename: mcnpumfile embed data option ``filename`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'MCNPUMFILE'] = abc.Terminal[r'MCNPUMFILE']('MCNPUMFILE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    filename: typing.Annotated[abc.Terminal, r'\S+']
