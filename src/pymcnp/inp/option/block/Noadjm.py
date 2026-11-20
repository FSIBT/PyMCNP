import typing

from .... import abc
from ..Block import Block
from ... import literal


class Noadjm(Block):
    """
    Represents noadjm block dawwg data options.

    Attributes:
        keyword: noadjm block suboption ``r'NOADJM'`` symbol.
        equals: noadjm block suboption ``r'='`` symbol.
        value: noadjm block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'NOADJM'] = abc.Terminal[r'NOADJM']('NOADJM')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    value: literal.Integer
