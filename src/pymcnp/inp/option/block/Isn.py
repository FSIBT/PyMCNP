import typing

from .... import abc
from ..Block import Block
from ... import literal


class Isn(Block):
    """
    Represents isn block dawwg data options.

    Attributes:
        keyword: isn block suboption ``r'ISN'`` symbol.
        equals: isn block suboption ``r'='`` symbol.
        value: isn block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'ISN'] | str = abc.Terminal[r'ISN']('ISN')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
