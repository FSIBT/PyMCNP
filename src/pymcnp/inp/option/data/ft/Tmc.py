import typing
import decimal
import dataclasses

from ..... import abc
from .... import literal
from ..Ft import Ft


class Tmc(Ft):
    """
    Represents tmc ft data options.

    Attributes:
        id: tmc group `TMC` symbol.
        a: tmc group `a` parameter.
        b: tmc group `b` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    id: typing.Annotated[abc.Terminal, r'TMC'] | str = abc.Terminal[r'TMC']('TMC')
    a: literal.Real | int | float | decimal.Decimal | str
    b: literal.Real | int | float | decimal.Decimal | str
