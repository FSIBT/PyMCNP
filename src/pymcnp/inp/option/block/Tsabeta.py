import typing
import decimal
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Tsabeta(Block):
    """
    Represents tsabeta block dawwg data options.

    Attributes:
        keyword: tsabeta block suboption `TSABETA` symbol.
        equals: tsabeta block suboption `=` symbol.
        value: tsabeta block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'TSABETA'] | str = abc.Terminal[r'TSABETA']('TSABETA')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Real | int | float | decimal.Decimal | str
