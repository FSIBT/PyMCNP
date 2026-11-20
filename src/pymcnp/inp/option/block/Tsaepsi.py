import typing

from .... import abc
from ..Block import Block
from ... import literal


class Tsaepsi(Block):
    """
    Represents tsaepsi block dawwg data options.

    Attributes:
        keyword: tsaepsi block suboption ``r'TSAEPSI'`` symbol.
        equals: tsaepsi block suboption ``r'='`` symbol.
        value: tsaepsi block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'TSAEPSI'] = abc.Terminal[r'TSAEPSI']('TSAEPSI')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    value: literal.Real
