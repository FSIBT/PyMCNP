import typing

from ..... import abc
from ..Rand import Rand
from .... import literal


class Hist(Rand):
    """
    Represents hist rand data options.

    Attributes:
        keyword: hist rand data option ``r'HIST'`` symbol.
        equals: hist rand data option ``r'='`` symbol.
        n: hist rand data option ``n`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'HIST'] | str = abc.Terminal[r'HIST']('HIST')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    n: literal.Integer | int | str
