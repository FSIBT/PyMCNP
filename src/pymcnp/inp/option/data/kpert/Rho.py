import typing
import decimal
import collections

from ..... import abc
from ..Kpert import Kpert
from .... import literal


class Rho(Kpert):
    """
    Represents rho kpert data options.

    Attributes:
        keyword: rho kpert data option ``r'RHO'`` symbol.
        equals: rho kpert data option ``r'='`` symbol.
        r: rho kpert data option ``r`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'RHO'] | str = abc.Terminal[r'RHO']('RHO')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    r: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )
