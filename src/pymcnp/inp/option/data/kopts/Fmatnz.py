import typing
import decimal
import dataclasses

from ..... import abc
from .... import literal
from ..Kopts import Kopts


class Fmatnz(Kopts):
    """
    Represents fmatnz kopts data options.

    Attributes:
        keyword: fmatnz kopts data option `FMATNZ` symbol.
        equals: fmatnz kopts data option `=` symbol.
        fmat_nz: fmatnz kopts data option `fmat_nz` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'FMATNZ'] | str = abc.Terminal[r'FMATNZ']('FMATNZ')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    fmat_nz: literal.Real | int | float | decimal.Decimal | str
