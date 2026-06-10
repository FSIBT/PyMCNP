import typing
import dataclasses

from ..... import abc
from ..M import M


class Tlib(M):
    """
    Represents tlib m data options.

    Attributes:
        keyword: tlib m data option `TLIB` symbol.
        equals: tlib m data option `=` symbol.
        x: tlib m data option `x` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'TLIB'] | str = abc.Terminal[r'TLIB']('TLIB')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: typing.Annotated[abc.Terminal, r'\S+'] | str
