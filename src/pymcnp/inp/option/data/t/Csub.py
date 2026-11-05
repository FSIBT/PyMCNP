import typing

from ..... import abc
from .... import literal
from ..T import T


class Csub(T):
    """
    Represents csub t data options.

    Attributes:
        keyword: csub t data option ``r'CSUB'`` symbol.
        equals: csub t data option ``r'='`` symbol.
        value: csub t data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'CSUB'] | str = abc.Terminal[r'CSUB']('CSUB')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
