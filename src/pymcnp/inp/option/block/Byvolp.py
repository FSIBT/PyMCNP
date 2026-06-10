import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Byvolp(Block):
    """
    Represents byvolp block dawwg data options.

    Attributes:
        keyword: byvolp block suboption `BYVOLP` symbol.
        equals: byvolp block suboption `=` symbol.
        value: byvolp block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'BYVOLP'] | str = abc.Terminal[r'BYVOLP']('BYVOLP')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
