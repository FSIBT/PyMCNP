import typing

from ..... import abc
from ..Embed import Embed


class Mgeoin(Embed):
    """
    Represents mgeoin embed data options.

    Attributes:
        keyword: mgeoin embed data option ``r'MGEOIN'`` symbol.
        equals: mgeoin embed data option ``r'='`` symbol.
        filename: mgeoin embed data option ``filename`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'MGEOIN'] | str = abc.Terminal[r'MGEOIN']('MGEOIN')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    filename: typing.Annotated[abc.Terminal, r'\S+'] | str
