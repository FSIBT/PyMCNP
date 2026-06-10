import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Tsasn(Block):
    """
    Represents tsasn block dawwg data options.

    Attributes:
        keyword: tsasn block suboption `TSASN` symbol.
        equals: tsasn block suboption `=` symbol.
        value: tsasn block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'TSASN'] | str = abc.Terminal[r'TSASN']('TSASN')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
