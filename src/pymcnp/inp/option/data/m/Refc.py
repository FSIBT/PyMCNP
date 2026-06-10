import typing
import decimal
import dataclasses

from ..... import abc
from ..M import M
from .... import literal


class Refc(M):
    """
    Represents refc m data options.

    Attributes:
        keyword: refi m data option `REFI` symbol.
        equals: refi m data option `=` symbol.
        a: refi m data option `a` parameter.
        b: refi m data option `b` parameter.
        c: refi m data option `c` parameter.
        d: refi m data option `d` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'REFC'] | str = abc.Terminal[r'REFC']('REFC')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    a: literal.Real | int | float | decimal.Decimal | str
    b: literal.Real | int | float | decimal.Decimal | str
    c: literal.Real | int | float | decimal.Decimal | str
    d: literal.Real | int | float | decimal.Decimal | str
