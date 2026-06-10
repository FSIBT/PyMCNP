import typing
import decimal
import collections
import dataclasses

from ..... import abc
from ..Kpert import Kpert
from .... import literal


class Rho(Kpert):
    """
    Represents rho kpert data options.

    Attributes:
        keyword: rho kpert data option `RHO` symbol.
        equals: rho kpert data option `=` symbol.
        r: rho kpert data option `r` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'RHO'] | str = abc.Terminal[r'RHO']('RHO')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    r: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )
