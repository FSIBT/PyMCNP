import typing
import dataclasses

from ..... import abc
from ..Kopts import Kopts


class Fmat(Kopts):
    """
    Represents fmat kopts data options.

    Attributes:
        keyword: fmat kopts data option `FMAT` symbol.
        equals: fmat kopts data option `=` symbol.
        value: fmat kopts data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'FMAT'] | str = abc.Terminal[r'FMAT']('FMAT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:YES|NO)'] | str
