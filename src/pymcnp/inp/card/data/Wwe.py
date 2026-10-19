import typing
import decimal
import collections
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Wwe(Data):
    """
    Represents wwe data cards.

    Attributes:
        keyword: wwe data card `WWE` symbol.
        colon: wwe data card `colon` parameter.
        particle: wwe data card `particle` parameter.
        e: wwe data card `e` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'WWE'] | str = abc.Terminal[r'WWE']('WWE')
    colon: typing.Annotated[abc.Terminal, r':'] | str = abc.Terminal[r':'](':')
    particle: literal.Particle | str = dataclasses.field(kw_only=True)
    e: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )
