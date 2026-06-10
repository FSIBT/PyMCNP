import typing
import dataclasses

from ..... import abc
from .... import literal
from ..Kopts import Kopts


class Fmatncyc(Kopts):
    """
    Represents fmatncyc kopts data options.

    Attributes:
        keyword: fmatncyc kopts data option `FMATNCYC` symbol.
        equals: fmatncyc kopts data option `=` symbol.
        fmat_ncyc: fmatncyc kopts data option `fmat_ncyc` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'FMATNCYC'] | str = abc.Terminal[r'FMATNCYC']('FMATNCYC')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    fmat_ncyc: literal.Integer | int | str
