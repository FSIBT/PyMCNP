import typing

from .... import abc
from ..Block import Block
from ... import literal


class Fmmix(Block):
    """
    Represents fmmix block dawwg data options.

    Attributes:
        keyword: fmmix block suboption ``r'FMMIX'`` symbol.
        equals: fmmix block suboption ``r'='`` symbol.
        value: fmmix block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'FMMIX'] = abc.Terminal[r'FMMIX']('FMMIX')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    value: literal.Integer
