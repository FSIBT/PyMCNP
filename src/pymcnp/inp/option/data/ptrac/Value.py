import typing
import decimal
import collections

from ..... import abc
from ..Ptrac import Ptrac
from .... import literal


class Value(Ptrac):
    """
    Represents value ptrac data options.

    Attributes:
        keyword: value ptrac data option ``r'VALUE'`` symbol.
        equals: value ptrac data option ``r'='`` symbol.
        value: value ptrac data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'VALUE'] | str = abc.Terminal[r'VALUE']('VALUE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[
        r''
    ]('')
