import typing

from ..... import abc
from .... import literal
from ..Mesh import Mesh


class Vec(Mesh):
    """
    Represents vec mesh data options.

    Attributes:
        keyword: vec mesh data option ``r'VEC'`` symbol.
        equals: vec mesh data option ``r'='`` symbol.
        x: vec mesh data option ``x`` parameter.
        y: vec mesh data option ``y`` parameter.
        z: vec mesh data option ``z`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'VEC'] = abc.Terminal[r'VEC']('VEC')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    x: literal.Real
    y: literal.Real
    z: literal.Real
