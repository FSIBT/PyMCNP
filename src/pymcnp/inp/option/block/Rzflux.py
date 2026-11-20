import typing

from .... import abc
from ..Block import Block
from ... import literal


class Rzflux(Block):
    """
    Represents rzflux block dawwg data options.

    Attributes:
        keyword: rzflux block suboption ``r'RZFLUX'`` symbol.
        equals: rzflux block suboption ``r'='`` symbol.
        value: rzflux block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'RZFLUX'] = abc.Terminal[r'RZFLUX']('RZFLUX')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    value: literal.Integer
