import typing
import decimal
import dataclasses

from ..... import abc
from .... import literal
from ..M import M


class Refs(M):
    """
    Represents refs m data options.

    Attributes:
        keyword: refs m data option `REFS` symbol.
        equals: refs m data option `=` symbol.
        b1: refs m data option `b1` parameter.
        c1: refs m data option `c1` parameter.
        b2: refs m data option `b2` parameter.
        c2: refs m data option `c2` parameter.
        b3: refs m data option `b3` parameter.
        c3: refs m data option `c3` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'REFS'] | str = abc.Terminal[r'REFS']('REFS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    b1: literal.Real | int | float | decimal.Decimal | str
    c1: literal.Real | int | float | decimal.Decimal | str
    b2: literal.Real | int | float | decimal.Decimal | str
    c2: literal.Real | int | float | decimal.Decimal | str
    b3: literal.Real | int | float | decimal.Decimal | str
    c3: literal.Real | int | float | decimal.Decimal | str
