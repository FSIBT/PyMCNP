import typing
import decimal
import collections

from ..... import abc
from .... import literal
from ..Burn import Burn


class Pfrac(Burn):
    """
    Represents pfrac burn data options.

    Attributes:
        keyword: pfrac burn data option ``r'PFRAC'`` symbol.
        equals: pfrac burn data option ``r'='`` symbol.
        f: pfrac burn data option ``f`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'PFRAC'] | str = abc.Terminal[r'PFRAC']('PFRAC')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    f: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )
