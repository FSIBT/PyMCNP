import typing
import decimal

from ..... import abc
from .... import literal
from ..Kopts import Kopts


class Fmatny(Kopts):
    """
    Represents fmatny kopts data options.

    Attributes:
        keyword: fmatny kopts data option `FMATNY` symbol.
        equals: fmatny kopts data option `=` symbol.
        fmat_ny: fmatny kopts data option `fmat_ny` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'FMATNY'] | str = abc.Terminal[r'FMATNY']('FMATNY')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    fmat_ny: literal.Real | int | float | decimal.Decimal | str
