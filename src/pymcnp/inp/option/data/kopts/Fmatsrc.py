import typing
import dataclasses

from ..... import abc
from ..Kopts import Kopts


class Fmatsrc(Kopts):
    """
    Represents fmatsrc kopts data options.

    Attributes:
        keyword: fmatsrc kopts data option `FMATSRC` symbol.
        equals: fmatsrc kopts data option `=` symbol.
        value: fmatsrc kopts data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'FMATSRC'] | str = abc.Terminal[r'FMATSRC']('FMATSRC')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:YES|NO|AUTO)'] | str
