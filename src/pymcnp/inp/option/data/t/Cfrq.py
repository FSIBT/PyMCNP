import typing
import decimal
import dataclasses

from ..... import abc
from .... import literal
from ..T import T


class Cfrq(T):
    """
    Represents cfrq t data options.

    Attributes:
        keyword: cfrq t data option `CFRQ` symbol.
        equals: cfrq t data option `=` symbol.
        value: cfrq t data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'CFRQ'] | str = abc.Terminal[r'CFRQ']('CFRQ')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Real | int | float | decimal.Decimal | str
