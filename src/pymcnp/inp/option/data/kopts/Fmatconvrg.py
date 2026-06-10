import typing
import dataclasses

from ..... import abc
from ..Kopts import Kopts


class Fmatconvrg(Kopts):
    """
    Represents fmatconvrg kopts data options.

    Attributes:
        keyword: fmatconvrg kopts data option `FMATCONVRG` symbol.
        equals: fmatconvrg kopts data option `=` symbol.
        value: fmatconvrg kopts data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'FMATCONVRG'] | str = abc.Terminal[r'FMATCONVRG']('FMATCONVRG')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:YES|NO)'] | str
