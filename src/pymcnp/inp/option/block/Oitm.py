import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Oitm(Block):
    """
    Represents oitm block dawwg data options.

    Attributes:
        keyword: oitm block suboption `OITM` symbol.
        equals: oitm block suboption `=` symbol.
        value: oitm block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'OITM'] | str = abc.Terminal[r'OITM']('OITM')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
