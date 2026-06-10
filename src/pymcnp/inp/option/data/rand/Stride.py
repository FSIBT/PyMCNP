import typing
import dataclasses

from ..... import abc
from ..Rand import Rand
from .... import literal


class Stride(Rand):
    """
    Represents stride rand data options.

    Attributes:
        keyword: stride rand data option `STRIDE` symbol.
        equals: stride rand data option `=` symbol.
        value: stride rand data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'STRIDE'] | str = abc.Terminal[r'STRIDE']('STRIDE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
