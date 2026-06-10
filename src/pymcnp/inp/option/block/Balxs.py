import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Balxs(Block):
    """
    Represents balxs block dawwg data options.

    Attributes:
        keyword: balxs block suboption `BALXS` symbol.
        equals: balxs block suboption `=` symbol.
        value: balxs block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'BALXS'] | str = abc.Terminal[r'BALXS']('BALXS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
