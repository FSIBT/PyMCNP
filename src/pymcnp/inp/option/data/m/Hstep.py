import typing

from ..... import abc
from .... import literal
from ..M import M


class Hstep(M):
    """
    Represents hstep m data options.

    Attributes:
        keyword: hstep m data option ``r'HSTEP'`` symbol.
        equals: hstep m data option ``r'='`` symbol.
        n: hstep m data option ``n`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'HSTEP'] | str = abc.Terminal[r'HSTEP']('HSTEP')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    n: literal.Integer | int | str
