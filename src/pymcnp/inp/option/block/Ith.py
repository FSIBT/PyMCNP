import typing

from .... import abc
from ..Block import Block
from ... import literal


class Ith(Block):
    """
    Represents ith block dawwg data options.

    Attributes:
        keyword: ith block suboption ``r'ITH'`` symbol.
        equals: ith block suboption ``r'='`` symbol.
        value: ith block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'ITH'] | str = abc.Terminal[r'ITH']('ITH')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
