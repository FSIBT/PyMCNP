import typing

from ..... import abc
from .... import literal
from ..M import M


class Refs(M):
    """
    Represents refs m data options.

    Attributes:
        keyword: refs m data option ``r'REFS'`` symbol.
        equals: refs m data option ``r'='`` symbol.
        b1: refs m data option ``b1`` parameter.
        c1: refs m data option ``c1`` parameter.
        b2: refs m data option ``b2`` parameter.
        c2: refs m data option ``c2`` parameter.
        b3: refs m data option ``b3`` parameter.
        c3: refs m data option ``c3`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'REFS'] = abc.Terminal[r'REFS']('REFS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    b1: literal.Real
    c1: literal.Real
    b2: literal.Real
    c2: literal.Real
    b3: literal.Real
    c3: literal.Real
