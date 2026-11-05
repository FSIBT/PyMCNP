import typing
import decimal

from ..... import abc
from .... import literal
from ..Kopts import Kopts


class Fmatnz(Kopts):
    """
    Represents fmatnz kopts data options.

    Attributes:
        keyword: fmatnz kopts data option ``r'FMATNZ'`` symbol.
        equals: fmatnz kopts data option ``r'='`` symbol.
        fmat_nz: fmatnz kopts data option ``fmat_nz`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'FMATNZ'] | str = abc.Terminal[r'FMATNZ']('FMATNZ')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    fmat_nz: literal.Real | int | float | decimal.Decimal | str
