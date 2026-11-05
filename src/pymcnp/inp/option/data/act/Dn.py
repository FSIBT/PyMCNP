import typing

from ..... import abc
from ..Act import Act


class Dn(Act):
    """
    Represents dn act data options.

    Attributes:
        keyword: dn act data option ``r'DN'`` symbol.
        equals: dn act data option ``r'='`` symbol.
        value: dn act data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'DN'] | str = abc.Terminal[r'DN']('DN')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:MODEL|LIBRARY|BOTH|PROMPT)'] | str
