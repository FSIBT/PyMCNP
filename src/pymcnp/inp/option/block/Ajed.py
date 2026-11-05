import typing

from .... import abc
from ..Block import Block
from ... import literal


class Ajed(Block):
    """
    Represents ajed block dawwg data options.

    Attributes:
        keyword: ajed block suboption ``r'AJED'`` symbol.
        equals: ajed block suboption ``r'='`` symbol.
        value: ajed block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'AJED'] | str = abc.Terminal[r'AJED']('AJED')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
