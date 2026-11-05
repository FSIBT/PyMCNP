import typing

from .... import abc
from ..Block import Block
from ... import literal


class Fissrp(Block):
    """
    Represents fissrp block dawwg data options.

    Attributes:
        keyword: fissrp block suboption ``r'FISSRP'`` symbol.
        equals: fissrp block suboption ``r'='`` symbol.
        value: fissrp block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'FISSRP'] | str = abc.Terminal[r'FISSRP']('FISSRP')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
