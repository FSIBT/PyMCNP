import typing
import dataclasses

from .... import abc
from ..Block import Block
from ... import literal


class Rzflux(Block):
    """
    Represents rzflux block dawwg data options.

    Attributes:
        keyword: rzflux block suboption `RZFLUX` symbol.
        equals: rzflux block suboption `=` symbol.
        value: rzflux block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'RZFLUX'] | str = abc.Terminal[r'RZFLUX']('RZFLUX')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
