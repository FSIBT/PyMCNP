import typing

from .... import abc
from ..Block import Block


class Srcacc(Block):
    """
    Represents srcacc block dawwg data options.

    Attributes:
        keyword: srcacc block suboption ``r'SRCACC'`` symbol.
        equals: srcacc block suboption ``r'='`` symbol.
        value: srcacc block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'SRCACC'] = abc.Terminal[r'SRCACC']('SRCACC')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'\S+']
