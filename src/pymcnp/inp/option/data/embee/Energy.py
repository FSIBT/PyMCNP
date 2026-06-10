import typing
import decimal
import dataclasses

from ..... import abc
from ..Embee import Embee
from .... import literal


class Energy(Embee):
    """
    Represents energy embee data options.

    Attributes:
        keyword: energy embee data option `ENERGY` symbol.
        equals: energy embee data option `=` symbol.
        value: energy embee data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'ENERGY'] | str = abc.Terminal[r'ENERGY']('ENERGY')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Real | int | float | decimal.Decimal | str
