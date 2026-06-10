import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Nogeod(Block):
    """
    Represents nogeod block dawwg data options.

    Attributes:
        keyword: nogeod block suboption `NOGEOD` symbol.
        equals: nogeod block suboption `=` symbol.
        value: nogeod block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'NOGEOD'] | str = abc.Terminal[r'NOGEOD']('NOGEOD')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
