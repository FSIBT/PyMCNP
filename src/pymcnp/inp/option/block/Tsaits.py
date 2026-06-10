import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Tsaits(Block):
    """
    Represents tsaits block dawwg data options.

    Attributes:
        keyword: tsaits block suboption `TSAITS` symbol.
        equals: tsaits block suboption `=` symbol.
        value: tsaits block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'TSAITS'] | str = abc.Terminal[r'TSAITS']('TSAITS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
