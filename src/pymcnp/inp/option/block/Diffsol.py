import typing
import dataclasses

from .... import abc
from ..Block import Block


class Diffsol(Block):
    """
    Represents diffsol block dawwg data options.

    Attributes:
        keyword: diffsol block suboption `DIFFSOL` symbol.
        equals: diffsol block suboption `=` symbol.
        value: diffsol block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'DIFFSOL'] | str = abc.Terminal[r'DIFFSOL']('DIFFSOL')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'\S+'] | str
