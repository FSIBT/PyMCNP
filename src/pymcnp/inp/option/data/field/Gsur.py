import typing
import dataclasses

import collections

from ..... import abc
from .... import literal
from ..Field import Field


class Gsur(Field):
    """
    Represents gsur field data options.

    Attributes:
        keyword: gsur field data option `GSUR` symbol.
        equals: gsur field data option `=` symbol.
        s: gsur field data option `s` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'GSUR'] | str = abc.Terminal[r'GSUR']('GSUR')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    s: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
