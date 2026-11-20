import typing

from .... import abc
from ..Block import Block
from ... import literal


class Rzmflux(Block):
    """
    Represents rzmflux block dawwg data options.

    Attributes:
        keyword: rzmflux block suboption ``r'RZMFLUX'`` symbol.
        equals: rzmflux block suboption ``r'='`` symbol.
        value: rzmflux block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'RZMFLUX'] = abc.Terminal[r'RZMFLUX']('RZMFLUX')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    value: literal.Integer
