import typing
import dataclasses

from ..... import abc
from ..M import M


class Slib(M):
    """
    Represents slib m data options.

    Attributes:
        keyword: slib m data option `SLIB` symbol.
        equals: slib m data option `=` symbol.
        x: slib m data option `x` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'SLIB'] | str = abc.Terminal[r'SLIB']('SLIB')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: typing.Annotated[abc.Terminal, r'\S+'] | str
