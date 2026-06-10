import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Rmflux(Block):
    """
    Represents rmflux block dawwg data options.

    Attributes:
        keyword: rmflux block suboption `RMFLUX` symbol.
        equals: rmflux block suboption `=` symbol.
        value: rmflux block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'RMFLUX'] | str = abc.Terminal[r'RMFLUX']('RMFLUX')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
