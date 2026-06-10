import typing
import decimal
import dataclasses

from ..... import abc
from .... import literal
from ..T import T


class Cbeg(T):
    """
    Represents cbeg t data options.

    Attributes:
        keyword: cbeg t data option `CBEG` symbol.
        equals: cbeg t data option `=` symbol.
        value: cbeg t data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'CBEG'] | str = abc.Terminal[r'CBEG']('CBEG')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Real | int | float | decimal.Decimal | str
