import typing
import decimal
import dataclasses

from ..... import abc
from ..Fmesh import Fmesh
from .... import literal


class Origin(Fmesh):
    """
    Represents origin fmesh data options.

    Attributes:
        keyword: origin fmesh data option `ORIGIN` symbol.
        equals: origin fmesh data option `=` symbol.
        x: origin fmesh data option `x` parameter.
        y: origin fmesh data option `y` parameter.
        z: origin fmesh data option `z` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'ORIGIN'] | str = abc.Terminal[r'ORIGIN']('ORIGIN')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: literal.Real | int | float | decimal.Decimal | str
    y: literal.Real | int | float | decimal.Decimal | str
    z: literal.Real | int | float | decimal.Decimal | str
