import typing
import decimal

from .... import abc
from ..Block import Block
from ... import literal


class Norm(Block):
    """
    Represents norm block dawwg data options.

    Attributes:
        keyword: norm block suboption ``r'NORM'`` symbol.
        equals: norm block suboption ``r'='`` symbol.
        value: norm block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'NORM'] | str = abc.Terminal[r'NORM']('NORM')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Real | int | float | decimal.Decimal | str
