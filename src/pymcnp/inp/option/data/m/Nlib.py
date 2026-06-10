import typing
import dataclasses

from ..... import abc
from ..M import M


class Nlib(M):
    """
    Represents nlib m data options.

    Attributes:
        keyword: nlib m data option `NLIB` symbol.
        equals: nlib m data option `=` symbol.
        x: nlib m data option `x` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'NLIB'] | str = abc.Terminal[r'NLIB']('NLIB')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: typing.Annotated[abc.Terminal, r'\S+'] | str
