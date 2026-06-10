import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Edoutf(Block):
    """
    Represents edoutf block dawwg data options.

    Attributes:
        keyword: edoutf block suboption `EDOUTF` symbol.
        equals: edoutf block suboption `=` symbol.
        value: edoutf block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'EDOUTF'] | str = abc.Terminal[r'EDOUTF']('EDOUTF')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
