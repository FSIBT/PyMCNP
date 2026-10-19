import typing
import dataclasses

from ..... import abc
from ..M import M


class Plib(M):
    """
    Represents plib m data options.

    Attributes:
        keyword: plib m data option `PLIB` symbol.
        equals: plib m data option `=` symbol.
        x: plib m data option `x` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'PLIB'] | str = abc.Terminal[r'PLIB']('PLIB')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: typing.Annotated[abc.Terminal, r'\S+'] | str = dataclasses.field(kw_only=True)
