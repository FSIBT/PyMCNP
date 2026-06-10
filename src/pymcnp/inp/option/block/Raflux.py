import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Raflux(Block):
    """
    Represents raflux block dawwg data options.

    Attributes:
        keyword: raflux block suboption `RAFLUX` symbol.
        equals: raflux block suboption `=` symbol.
        value: raflux block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'RAFLUX'] | str = abc.Terminal[r'RAFLUX']('RAFLUX')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
