import typing

from ..... import abc
from ..Act import Act


class Nonfiss(Act):
    """
    Represents nofiss act data options.

    Attributes:
        keyword: nofiss act data option ``r'NONFISS'`` symbol.
        equals: nofiss act data option ``r'='`` symbol.
        value: nofiss act data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'NONFISS'] | str = abc.Terminal[r'NONFISS']('NONFISS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'NONE|ALL|(?:[npefa](?:,[npefa]){0,4})'] | str
