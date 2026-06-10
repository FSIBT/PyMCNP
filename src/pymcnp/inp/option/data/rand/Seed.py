import typing
import dataclasses

from ..... import abc
from ..Rand import Rand
from .... import literal


class Seed(Rand):
    """
    Represents seed rand data options.

    Attributes:
        keyword: seed rand data option `SEED` symbol.
        equals: seed rand data option `=` symbol.
        value: seed rand data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'SEED'] | str = abc.Terminal[r'SEED']('SEED')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
