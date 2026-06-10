import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Asleft(Block):
    """
    Represents asleft block dawwg data options.

    Attributes:
        keyword: asleft block suboption `ASLEFT` symbol.
        equals: asleft block suboption `=` symbol.
        value: asleft block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'ASLEFT'] | str = abc.Terminal[r'ASLEFT']('ASLEFT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
