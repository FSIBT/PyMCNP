import typing
import decimal
import dataclasses

from ..... import abc
from .... import literal
from ..M import M


class Cond(M):
    """
    Represents cond m data options.

    Attributes:
        keyword: cond m data option `COND` symbol.
        equals: cond m data option `=` symbol.
        value: cond m data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'COND'] | str = abc.Terminal[r'COND']('COND')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Real | int | float | decimal.Decimal | str
