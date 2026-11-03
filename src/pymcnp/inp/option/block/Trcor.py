import typing

from .... import abc
from ..Block import Block


class Trcor(Block):
    """
    Represents trcor block dawwg data options.

    Attributes:
        keyword: trcor block suboption `TRCOR` symbol.
        equals: trcor block suboption `=` symbol.
        value: trcor block suboption `value` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'TRCOR'] | str = abc.Terminal[r'TRCOR']('TRCOR')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'\S+'] | str
