import typing
import decimal
import dataclasses

from ..... import abc
from .... import literal
from ..Kopts import Kopts


class Fmatnx(Kopts):
    """
    Represents fmatnx kopts data options.

    Attributes:
        keyword: fmatnx kopts data option `FMATNX` symbol.
        equals: fmatnx kopts data option `=` symbol.
        fmat_nx: fmatnx kopts data option `fmat_nx` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'FMATNX'] | str = abc.Terminal[r'FMATNX']('FMATNX')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    fmat_nx: literal.Real | int | float | decimal.Decimal | str
