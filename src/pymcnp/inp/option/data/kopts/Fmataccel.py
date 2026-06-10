import typing
import dataclasses

from ..... import abc
from ..Kopts import Kopts


class Fmataccel(Kopts):
    """
    Represents fmataccel kopts data options.

    Attributes:
        keyword: fmataccel kopts data option `FMATACCEL` symbol.
        equals: fmataccel kopts data option `=` symbol.
        value: fmataccel kopts data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'FMATACCEL'] | str = abc.Terminal[r'FMATACCEL']('FMATACCEL')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:YES|NO)'] | str
