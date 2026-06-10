import typing
import dataclasses

from ..... import abc
from ..Kopts import Kopts


class Precursor(Kopts):
    """
    Represents precursor kopts data options.

    Attributes:
        keyword: precursor kopts data option `PRECURSOR` symbol.
        equals: precursor kopts data option `=` symbol.
        value: precursor kopts data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'PRECURSOR'] | str = abc.Terminal[r'PRECURSOR']('PRECURSOR')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:YES|NO)'] | str
