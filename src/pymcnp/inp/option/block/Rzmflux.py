import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Rzmflux(Block):
    """
    Represents rzmflux block dawwg data options.

    Attributes:
        keyword: rzmflux block suboption `RZMFLUX` symbol.
        equals: rzmflux block suboption `=` symbol.
        value: rzmflux block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'RZMFLUX'] | str = abc.Terminal[r'RZMFLUX']('RZMFLUX')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
