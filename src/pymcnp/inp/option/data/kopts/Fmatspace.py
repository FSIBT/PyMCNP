import typing
import dataclasses

from ..... import abc
from .... import literal
from ..Kopts import Kopts


class Fmatspace(Kopts):
    """
    Represents fmatspace kopts data options.

    Attributes:
        keyword: fmatspace kopts data option `FMATSPACE` symbol.
        equals: fmatspace kopts data option `=` symbol.
        fmat_space: fmatspace kopts data option `fmat_space` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'FMATSPACE'] | str = abc.Terminal[r'FMATSPACE']('FMATSPACE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    fmat_space: literal.Integer | int | str
