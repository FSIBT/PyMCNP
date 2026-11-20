import typing

from ..... import abc
from ..Fmesh import Fmesh
from .... import literal


class Vec(Fmesh):
    """
    Represents vec fmesh data options.

    Attributes:
        keyword: vec fmesh data option ``r'VEC'`` symbol.
        equals: vec fmesh data option ``r'='`` symbol.
        x: vec fmesh data option ``x`` parameter.
        y: vec fmesh data option ``y`` parameter.
        z: vec fmesh data option ``z`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'VEC'] = abc.Terminal[r'VEC']('VEC')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    x: literal.Real
    y: literal.Real
    z: literal.Real
