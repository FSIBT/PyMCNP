import typing
import dataclasses

from ..... import abc
from ..M import M


class Alib(M):
    """
    Represents alib m data options.

    Attributes:
        keyword: alib m data option `ALIB` symbol.
        equals: alib m data option `=` symbol.
        x: alib m data option `x` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'ALIB'] | str = abc.Terminal[r'ALIB']('ALIB')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: typing.Annotated[abc.Terminal, r'\S+'] | str = dataclasses.field(kw_only=True)
