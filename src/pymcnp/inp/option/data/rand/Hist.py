import typing
import dataclasses

from ..... import abc
from ..Rand import Rand
from .... import literal


class Hist(Rand):
    """
    Represents hist rand data options.

    Attributes:
        keyword: hist rand data option `HIST` symbol.
        equals: hist rand data option `=` symbol.
        n: hist rand data option `n` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'HIST'] | str = abc.Terminal[r'HIST']('HIST')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    n: literal.Integer | int | str = dataclasses.field(kw_only=True)
