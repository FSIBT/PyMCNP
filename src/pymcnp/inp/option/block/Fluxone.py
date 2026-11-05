import typing

from .... import abc
from ..Block import Block
from ... import literal


class Fluxone(Block):
    """
    Represents fluxone block dawwg data options.

    Attributes:
        keyword: fluxone block suboption ``r'FLUXONE'`` symbol.
        equals: fluxone block suboption ``r'='`` symbol.
        value: fluxone block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'FLUXONE'] | str = abc.Terminal[r'FLUXONE']('FLUXONE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
