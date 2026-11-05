import typing

from .... import abc
from ..Block import Block
from ... import literal


class Angp(Block):
    """
    Represents angp block dawwg data options.

    Attributes:
        keyword: angp block suboption ``r'ANGP'`` symbol.
        equals: angp block suboption ``r'='`` symbol.
        value: angp block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'ANGP'] | str = abc.Terminal[r'ANGP']('ANGP')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
