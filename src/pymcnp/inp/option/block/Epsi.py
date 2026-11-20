import typing

from .... import abc
from ..Block import Block
from ... import literal


class Epsi(Block):
    """
    Represents epsi block dawwg data options.

    Attributes:
        keyword: epsi block suboption ``r'EPSI'`` symbol.
        equals: epsi block suboption ``r'='`` symbol.
        value: epsi block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'EPSI'] = abc.Terminal[r'EPSI']('EPSI')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    value: literal.Real
