import typing
import decimal
import collections
import dataclasses

from ..... import abc
from ..Fmult import Fmult
from .... import literal


class Sfnu(Fmult):
    """
    Represents sfnu fmult data options.

    Attributes:
        keyword: sfnu fmult data option `SFNU` symbol.
        equals: sfnu fmult data option `=` symbol.
        x: sfnu fmult data option `x` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'SFNU'] | str = abc.Terminal[r'SFNU']('SFNU')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )
