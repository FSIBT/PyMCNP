import typing

from .... import abc
from ..Block import Block


class Trcor(Block):
    """
    Represents trcor block dawwg data options.

    Attributes:
        keyword: trcor block suboption ``r'TRCOR'`` symbol.
        equals: trcor block suboption ``r'='`` symbol.
        value: trcor block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'TRCOR'] = abc.Terminal[r'TRCOR']('TRCOR')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'\S+']
