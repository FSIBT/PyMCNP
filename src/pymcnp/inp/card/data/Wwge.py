import typing
import decimal
import collections
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Wwge(Data):
    """
    Represents wwge data cards.

    Attributes:
        keyword: wwge data card `WWGE` symbol.
        colon: wwge data card `colon` parameter.
        particle: wwge data card `particle` parameter.
        e: wwge data card `e` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'WWGE'] | str = abc.Terminal[r'WWGE']('WWGE')
    colon: typing.Annotated[abc.Terminal, r':'] | str = abc.Terminal[r':'](':')
    particle: literal.Particle | str
    e: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )
