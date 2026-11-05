import typing
import decimal

from ..... import abc
from ..Embee import Embee
from .... import literal


class Factor(Embee):
    """
    Represents factor embee data options.

    Attributes:
        keyword: factor embee data option ``r'FACTOR'`` symbol.
        equals: factor embee data option ``r'='`` symbol.
        value: factor embee data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'FACTOR'] | str = abc.Terminal[r'FACTOR']('FACTOR')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Real | int | float | decimal.Decimal | str
