import typing

from ..... import abc
from ..Act import Act


class Dg(Act):
    """
    Represents dg act data options.

    Attributes:
        keyword: dg act data option ``r'DG'`` symbol.
        equals: dg act data option ``r'='`` symbol.
        value: dg act data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'DG'] | str = abc.Terminal[r'DG']('DG')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:LINES|MG|NONE)'] | str
