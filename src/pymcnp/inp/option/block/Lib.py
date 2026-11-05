import typing

from .... import abc
from ..Block import Block


class Lib(Block):
    """
    Represents lib block dawwg data options.

    Attributes:
        keyword: lib block suboption ``r'LIB'`` symbol.
        equals: lib block suboption ``r'='`` symbol.
        value: lib block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'LIB'] | str = abc.Terminal[r'LIB']('LIB')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'\S+'] | str
