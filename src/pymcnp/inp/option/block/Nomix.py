import typing

from .... import abc
from ..Block import Block
from ... import literal


class Nomix(Block):
    """
    Represents nomix block dawwg data options.

    Attributes:
        keyword: nomix block suboption ``r'NOMIX'`` symbol.
        equals: nomix block suboption ``r'='`` symbol.
        value: nomix block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'NOMIX'] | str = abc.Terminal[r'NOMIX']('NOMIX')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
