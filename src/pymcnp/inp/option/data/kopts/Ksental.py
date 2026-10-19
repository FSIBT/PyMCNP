import typing
import dataclasses

from ..... import abc
from ..Kopts import Kopts


class Ksental(Kopts):
    """
    Represents ksental kopts data options.
    """


class Ksental_0(Ksental):
    """
    Represents ksental kopts data options, form #0.

    Attributes:
        keyword: ksental kopts data option `KSENTAL` symbol.
        equals: ksental kopts data option `=` symbol.
        fileopt: ksental kopts data option `fileopt` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'KSENTAL'] | str = abc.Terminal[r'KSENTAL']('KSENTAL')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    fileopt: typing.Annotated[abc.Terminal, r'MCTAL'] | str = dataclasses.field(kw_only=True)


class Ksental_1(Ksental):
    """
    Represents ksental kopts data options, form #1.

    Attributes:
        keyword: ksental kopts data option `KSENTAL` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'KSENTAL'] | str = abc.Terminal[r'KSENTAL']('KSENTAL')
