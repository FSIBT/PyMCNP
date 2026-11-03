import typing
import decimal
import collections

from ..... import abc
from ..Fmesh import Fmesh
from .... import literal


class Imesh(Fmesh):
    """
    Represents imesh fmesh data options.

    Attributes:
        keyword: imesh fmesh data option `IMESH` symbol.
        equals: imesh fmesh data option `=` symbol.
        x: imesh fmesh data option `x` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'IMESH'] | str = abc.Terminal[r'IMESH']('IMESH')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )
