import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Sourcp(Block):
    """
    Represents sourcp block dawwg data options.

    Attributes:
        keyword: sourcp block suboption `SOURCP` symbol.
        equals: sourcp block suboption `=` symbol.
        value: sourcp block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'SOURCP'] | str = abc.Terminal[r'SOURCP']('SOURCP')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
