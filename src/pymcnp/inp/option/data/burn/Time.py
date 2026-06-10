import typing
import decimal
import collections
import dataclasses

from ..... import abc
from .... import literal
from ..Burn import Burn


class Time(Burn):
    """
    Represents time burn data options.

    Attributes:
        keyword: time burn data option `TIME` symbol.
        equals: time burn data option `=` symbol.
        t: time burn data option `t` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'TIME'] | str = abc.Terminal[r'TIME']('TIME')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    t: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )
