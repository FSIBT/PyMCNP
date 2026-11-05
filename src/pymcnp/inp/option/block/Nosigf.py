import typing

from .... import abc
from ..Block import Block
from ... import literal


class Nosigf(Block):
    """
    Represents nosigf block dawwg data options.

    Attributes:
        keyword: nosigf block suboption ``r'NOSIGF'`` symbol.
        equals: nosigf block suboption ``r'='`` symbol.
        value: nosigf block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'NOSIGF'] | str = abc.Terminal[r'NOSIGF']('NOSIGF')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
