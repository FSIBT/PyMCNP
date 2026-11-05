import typing

from .... import abc
from ..Block import Block
from ... import literal


class Asrite(Block):
    """
    Represents asrite block dawwg data options.

    Attributes:
        keyword: asrite block suboption ``r'ASRITE'`` symbol.
        equals: asrite block suboption ``r'='`` symbol.
        value: asrite block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'ASRITE'] | str = abc.Terminal[r'ASRITE']('ASRITE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
