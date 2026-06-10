import typing
import decimal
import dataclasses

from ..... import abc
from .... import literal
from ..Mesh import Mesh


class Vec(Mesh):
    """
    Represents vec mesh data options.

    Attributes:
        keyword: vec mesh data option `VEC` symbol.
        equals: vec mesh data option `=` symbol.
        x: vec mesh data option `x` parameter.
        y: vec mesh data option `y` parameter.
        z: vec mesh data option `z` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'VEC'] | str = abc.Terminal[r'VEC']('VEC')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: literal.Real | int | float | decimal.Decimal | str
    y: literal.Real | int | float | decimal.Decimal | str
    z: literal.Real | int | float | decimal.Decimal | str
