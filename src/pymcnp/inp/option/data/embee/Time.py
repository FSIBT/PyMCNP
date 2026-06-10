import typing
import decimal
import dataclasses

from ..... import abc
from ..Embee import Embee
from .... import literal


class Time(Embee):
    """
    Represents time embee data options.

    Attributes:
        keyword: time embee data option `TIME` symbol.
        equals: time embee data option `=` symbol.
        value: time embee data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'TIME'] | str = abc.Terminal[r'TIME']('TIME')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Real | int | float | decimal.Decimal | str
