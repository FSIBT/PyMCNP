import typing
import decimal
import collections
import dataclasses

from ..... import abc
from ..Ptrac import Ptrac
from .... import literal


class Value(Ptrac):
    """
    Represents value ptrac data options.

    Attributes:
        keyword: value ptrac data option `VALUE` symbol.
        equals: value ptrac data option `=` symbol.
        value: value ptrac data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'VALUE'] | str = abc.Terminal[r'VALUE']('VALUE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[
        r''
    ]('')
