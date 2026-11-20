import typing

from ..... import abc
from .... import literal
from ..Kopts import Kopts


class Fmatncyc(Kopts):
    """
    Represents fmatncyc kopts data options.

    Attributes:
        keyword: fmatncyc kopts data option ``r'FMATNCYC'`` symbol.
        equals: fmatncyc kopts data option ``r'='`` symbol.
        fmat_ncyc: fmatncyc kopts data option ``fmat_ncyc`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'FMATNCYC'] = abc.Terminal[r'FMATNCYC']('FMATNCYC')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    fmat_ncyc: literal.Integer
