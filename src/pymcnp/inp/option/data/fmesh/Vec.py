import typing
import decimal
import dataclasses

from ..... import abc
from ..Fmesh import Fmesh
from .... import literal


class Vec(Fmesh):
    """
    Represents vec fmesh data options.

    Attributes:
        keyword: vec fmesh data option `VEC` symbol.
        equals: vec fmesh data option `=` symbol.
        x: vec fmesh data option `x` parameter.
        y: vec fmesh data option `y` parameter.
        z: vec fmesh data option `z` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'VEC'] | str = abc.Terminal[r'VEC']('VEC')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: literal.Real | int | float | decimal.Decimal | str
    y: literal.Real | int | float | decimal.Decimal | str
    z: literal.Real | int | float | decimal.Decimal | str
