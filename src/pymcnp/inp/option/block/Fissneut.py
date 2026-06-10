import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Fissneut(Block):
    """
    Represents fissneut block dawwg data options.

    Attributes:
        keyword: fissneut block suboption `FISSNEUT` symbol.
        equals: fissneut block suboption `=` symbol.
        value: fissneut block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'FISSNEUT'] | str = abc.Terminal[r'FISSNEUT']('FISSNEUT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
