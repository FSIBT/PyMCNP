import typing
import dataclasses

from .... import abc
from ..Block import Block


class Srcacc(Block):
    """
    Represents srcacc block dawwg data options.

    Attributes:
        keyword: srcacc block suboption `SRCACC` symbol.
        equals: srcacc block suboption `=` symbol.
        value: srcacc block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'SRCACC'] | str = abc.Terminal[r'SRCACC']('SRCACC')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'\S+'] | str
