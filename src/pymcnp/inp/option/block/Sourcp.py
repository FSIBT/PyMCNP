import typing

from .... import abc
from ..Block import Block
from ... import literal


class Sourcp(Block):
    """
    Represents sourcp block dawwg data options.

    Attributes:
        keyword: sourcp block suboption ``r'SOURCP'`` symbol.
        equals: sourcp block suboption ``r'='`` symbol.
        value: sourcp block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'SOURCP'] | str = abc.Terminal[r'SOURCP']('SOURCP')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
