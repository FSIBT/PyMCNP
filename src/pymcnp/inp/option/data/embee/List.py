import typing
import decimal
import collections
import dataclasses

from ..... import abc
from ..Embee import Embee
from .... import literal


class List(Embee):
    """
    Represents list embee data options.

    Attributes:
        keyword: list embee data option `LIST` symbol.
        equals: list embee data option `=` symbol.
        value: list embee data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'LIST'] | str = abc.Terminal[r'LIST']('LIST')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[
        r''
    ]('')
