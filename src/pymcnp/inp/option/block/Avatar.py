import typing

from .... import abc
from ..Block import Block
from ... import literal


class Avatar(Block):
    """
    Represents avatar block dawwg data options.

    Attributes:
        keyword: avatar block suboption ``r'AVATAR'`` symbol.
        equals: avatar block suboption ``r'='`` symbol.
        value: avatar block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'AVATAR'] = abc.Terminal[r'AVATAR']('AVATAR')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    value: literal.Integer
