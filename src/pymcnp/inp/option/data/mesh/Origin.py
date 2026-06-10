import typing
import decimal
import dataclasses

from ..... import abc
from .... import literal
from ..Mesh import Mesh


class Origin(Mesh):
    """
    Represents origin mesh data options.

    Attributes:
        keyword: origin mesh data option `ORIGIN` symbol.
        equals: origin mesh data option `=` symbol.
        x: origin mesh data option `x` parameter.
        y: origin mesh data option `y` parameter.
        z: origin mesh data option `z` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'ORIGIN'] | str = abc.Terminal[r'ORIGIN']('ORIGIN')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: literal.Real | int | float | decimal.Decimal | str
    y: literal.Real | int | float | decimal.Decimal | str
    z: literal.Real | int | float | decimal.Decimal | str
