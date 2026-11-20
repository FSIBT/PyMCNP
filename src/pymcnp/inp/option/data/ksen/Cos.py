import typing

from ..... import abc
from .... import literal
from ..Ksen import Ksen


class Cos(Ksen):
    """
    Represents cos ksen data options.

    Attributes:
        keyword: cos ksen data option ``r'COS'`` symbol.
        equals: cos ksen data option ``r'='`` symbol.
        angles: cos ksen data option ``angles`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'COS'] = abc.Terminal[r'COS']('COS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    angles: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
