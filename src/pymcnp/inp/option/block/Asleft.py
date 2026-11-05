import typing

from .... import abc
from ..Block import Block
from ... import literal


class Asleft(Block):
    """
    Represents asleft block dawwg data options.

    Attributes:
        keyword: asleft block suboption ``r'ASLEFT'`` symbol.
        equals: asleft block suboption ``r'='`` symbol.
        value: asleft block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'ASLEFT'] | str = abc.Terminal[r'ASLEFT']('ASLEFT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
