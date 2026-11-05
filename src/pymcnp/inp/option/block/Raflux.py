import typing

from .... import abc
from ..Block import Block
from ... import literal


class Raflux(Block):
    """
    Represents raflux block dawwg data options.

    Attributes:
        keyword: raflux block suboption ``r'RAFLUX'`` symbol.
        equals: raflux block suboption ``r'='`` symbol.
        value: raflux block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'RAFLUX'] | str = abc.Terminal[r'RAFLUX']('RAFLUX')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
