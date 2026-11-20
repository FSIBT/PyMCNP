import typing

from .... import abc
from ..Block import Block
from ... import literal


class Ibb(Block):
    """
    Represents ibb block dawwg data options.

    Attributes:
        keyword: ibb block suboption ``r'IBB'`` symbol.
        equals: ibb block suboption ``r'='`` symbol.
        value: ibb block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'IBB'] = abc.Terminal[r'IBB']('IBB')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    value: literal.Integer
