import typing
import decimal
import collections
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Wwgt(Data):
    """
    Represents wwgt data cards.

    Attributes:
        keyword: wwgt data card `WWGT` symbol.
        colon: wwgt data card `colon` parameter.
        particle: wwgt data card `particle` parameter.
        t: wwgt data card `t` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'WWGT'] | str = abc.Terminal[r'WWGT']('WWGT')
    colon: typing.Annotated[abc.Terminal, r':'] | str = abc.Terminal[r':'](':')
    particle: literal.Particle | str
    t: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )
