import typing
import dataclasses

from ..... import abc
from ..Rand import Rand
from .... import literal


class Gen(Rand):
    """
    Represents gen rand data options.

    Attributes:
        keyword: gen rand data option `GEN` symbol.
        equals: gen rand data option `=` symbol.
        n: gen rand data option `n` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'GEN'] | str = abc.Terminal[r'GEN']('GEN')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    n: literal.Integer | int | str
