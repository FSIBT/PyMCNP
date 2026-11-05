import typing

from .... import abc
from ..Block import Block
from ... import literal


class Nomacr(Block):
    """
    Represents nomacr block dawwg data options.

    Attributes:
        keyword: nomacr block suboption ``r'NOMACR'`` symbol.
        equals: nomacr block suboption ``r'='`` symbol.
        value: nomacr block suboption ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'NOMACR'] | str = abc.Terminal[r'NOMACR']('NOMACR')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
