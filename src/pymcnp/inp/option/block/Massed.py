import typing

from .... import abc
from ..Block import Block
from ... import literal


class Massed(Block):
    """
    Represents massed block dawwg data options.

    Attributes:
        keyword: massed block suboption ``r'MASSED'`` symbol.
        equals: massed block suboption ``r'='`` symbol.
        value: massed block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'MASSED'] | str = abc.Terminal[r'MASSED']('MASSED')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
