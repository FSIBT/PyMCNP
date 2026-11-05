import typing
import decimal

from ..... import abc
from ..Embee import Embee
from .... import literal


class Energy(Embee):
    """
    Represents energy embee data options.

    Attributes:
        keyword: energy embee data option ``r'ENERGY'`` symbol.
        equals: energy embee data option ``r'='`` symbol.
        value: energy embee data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'ENERGY'] | str = abc.Terminal[r'ENERGY']('ENERGY')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Real | int | float | decimal.Decimal | str
