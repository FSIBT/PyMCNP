import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Ievt(Block):
    """
    Represents ievt block dawwg data options.

    Attributes:
        keyword: ievt block suboption `IEVT` symbol.
        equals: ievt block suboption `=` symbol.
        value: ievt block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'IEVT'] | str = abc.Terminal[r'IEVT']('IEVT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
