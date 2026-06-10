import typing
import dataclasses

from ..... import abc
from .... import literal
from ..Kopts import Kopts


class Fmatskip(Kopts):
    """
    Represents fmatskip kopts data options.

    Attributes:
        keyword: fmatskip kopts data option `FMATSKIP` symbol.
        equals: fmatskip kopts data option `=` symbol.
        fmat_skip: fmatskip kopts data option `fmat_skip` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'FMATSKIP'] | str = abc.Terminal[r'FMATSKIP']('FMATSKIP')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    fmat_skip: literal.Integer | int | str
