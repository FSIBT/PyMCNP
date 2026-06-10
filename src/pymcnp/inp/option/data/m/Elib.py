import typing
import dataclasses

from ..... import abc
from ..M import M


class Elib(M):
    """
    Represents elib m data options.

    Attributes:
        keyword: elib m data option `ELIB` symbol.
        equals: elib m data option `=` symbol.
        x: elib m data option `x` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'ELIB'] | str = abc.Terminal[r'ELIB']('ELIB')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: typing.Annotated[abc.Terminal, r'\S+'] | str
