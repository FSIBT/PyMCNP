import typing

from ..... import abc
from .... import literal
from ..Ksen import Ksen


class Legendre(Ksen):
    """
    Represents legendre ksen data options.

    Attributes:
        keyword: legendre ksen data option ``r'LEGENDRE'`` symbol.
        equals: legendre ksen data option ``r'='`` symbol.
        value: legendre ksen data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'LEGENDRE'] | str = abc.Terminal[r'LEGENDRE']('LEGENDRE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
