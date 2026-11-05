import typing

from .... import abc
from ..Block import Block
from ... import literal


class Edoutf(Block):
    """
    Represents edoutf block dawwg data options.

    Attributes:
        keyword: edoutf block suboption ``r'EDOUTF'`` symbol.
        equals: edoutf block suboption ``r'='`` symbol.
        value: edoutf block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'EDOUTF'] | str = abc.Terminal[r'EDOUTF']('EDOUTF')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
