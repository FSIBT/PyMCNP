import typing

from .... import abc
from ..Block import Block
from ... import literal


class Nosolv(Block):
    """
    Represents nosolv block dawwg data options.

    Attributes:
        keyword: nosolv block suboption ``r'NOSOLV'`` symbol.
        equals: nosolv block suboption ``r'='`` symbol.
        value: nosolv block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'NOSOLV'] = abc.Terminal[r'NOSOLV']('NOSOLV')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    value: literal.Integer
