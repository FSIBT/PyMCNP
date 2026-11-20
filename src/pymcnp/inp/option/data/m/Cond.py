import typing

from ..... import abc
from .... import literal
from ..M import M


class Cond(M):
    """
    Represents cond m data options.

    Attributes:
        keyword: cond m data option ``r'COND'`` symbol.
        equals: cond m data option ``r'='`` symbol.
        value: cond m data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'COND'] = abc.Terminal[r'COND']('COND')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    value: literal.Real
