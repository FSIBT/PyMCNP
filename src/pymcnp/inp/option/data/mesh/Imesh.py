import typing
import decimal
import collections

from ..... import abc
from .... import literal
from ..Mesh import Mesh


class Imesh(Mesh):
    """
    Represents imesh mesh data options.

    Attributes:
        keyword: imesh mesh data option ``r'IMESH'`` symbol.
        equals: imesh mesh data option ``r'='`` symbol.
        x: imesh mesh data option ``x`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'IMESH'] | str = abc.Terminal[r'IMESH']('IMESH')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )
