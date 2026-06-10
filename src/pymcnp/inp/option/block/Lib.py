import typing
import dataclasses

from .... import abc
from ..Block import Block


class Lib(Block):
    """
    Represents lib block dawwg data options.

    Attributes:
        keyword: lib block suboption `LIB` symbol.
        equals: lib block suboption `=` symbol.
        value: lib block suboption `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'LIB'] | str = abc.Terminal[r'LIB']('LIB')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'\S+'] | str
