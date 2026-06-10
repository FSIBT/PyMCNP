import typing
import dataclasses

from ..... import abc
from ..M import M


class Hlib(M):
    """
    Represents hlib m data options.

    Attributes:
        keyword: hlib m data option `HLIB` symbol.
        equals: hlib m data option `=` symbol.
        x: hlib m data option `x` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'HLIB'] | str = abc.Terminal[r'HLIB']('HLIB')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: typing.Annotated[abc.Terminal, r'\S+'] | str
