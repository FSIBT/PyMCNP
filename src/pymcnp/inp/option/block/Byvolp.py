import typing

from .... import abc
from ..Block import Block
from ... import literal


class Byvolp(Block):
    """
    Represents byvolp block dawwg data options.

    Attributes:
        keyword: byvolp block suboption ``r'BYVOLP'`` symbol.
        equals: byvolp block suboption ``r'='`` symbol.
        value: byvolp block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'BYVOLP'] = abc.Terminal[r'BYVOLP']('BYVOLP')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    value: literal.Integer
