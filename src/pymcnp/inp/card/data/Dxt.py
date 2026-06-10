import typing
import decimal
import collections
import dataclasses

from .... import abc
from ... import literal
from ... import group
from ..Data import Data


class Dxt(Data):
    """
    Represents dxt data cards.

    Attributes:
        keyword: dxt data card `DXT` symbol.
        colon: dxt data card `colon` parameter.
        particle: dxt data card `particle` parameter.
        x_y_z_ri_ro: dxt data card `x_y_z_ri_ro` parameter.
        dwc1: dxt data card `dwc1` parameter.
        dwc2: dxt data card `dwc2` parameter.
        dpwt: dxt data card `dpwt` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'DXT'] | str = abc.Terminal[r'DXT']('DXT')
    colon: typing.Annotated[abc.Terminal, r':'] | str = abc.Terminal[r':'](':')
    particle: literal.Particle | str
    x_y_z_ri_ro: typing.Annotated[abc.Array, group.Dxtran, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[group.Dxtran | str] | str = abc.Terminal[r'']('')
    dwc1: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    dwc2: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    dpwt: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
