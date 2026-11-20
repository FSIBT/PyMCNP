import typing

from .... import abc
from ..Block import Block
from ... import literal


class Mt(Block):
    """
    Represents mt block dawwg data options.

    Attributes:
        keyword: mt block suboption ``r'MT'`` symbol.
        equals: mt block suboption ``r'='`` symbol.
        value: mt block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'MT'] = abc.Terminal[r'MT']('MT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    value: literal.Integer
