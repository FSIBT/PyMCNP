import typing

from ..... import abc
from ..Act import Act


class Fission(Act):
    """
    Represents fission act data options.

    Attributes:
        keyword: fission act data option ``r'FISSION'`` symbol.
        equals: fission act data option ``r'='`` symbol.
        value: fission act data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'FISSION'] | str = abc.Terminal[r'FISSION']('FISSION')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'NONE|ALL|(?:[npefa](?:,[npefa]){0,4})'] | str
