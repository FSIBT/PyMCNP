import typing

from .... import abc
from ..Block import Block
from ... import literal


class Isct(Block):
    """
    Represents isct block dawwg data options.

    Attributes:
        keyword: isct block suboption ``r'ISCT'`` symbol.
        equals: isct block suboption ``r'='`` symbol.
        value: isct block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'ISCT'] | str = abc.Terminal[r'ISCT']('ISCT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
