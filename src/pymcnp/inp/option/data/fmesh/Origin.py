import typing

from ..... import abc
from ..Fmesh import Fmesh
from .... import literal


class Origin(Fmesh):
    """
    Represents origin fmesh data options.

    Attributes:
        keyword: origin fmesh data option ``r'ORIGIN'`` symbol.
        equals: origin fmesh data option ``r'='`` symbol.
        x: origin fmesh data option ``x`` parameter.
        y: origin fmesh data option ``y`` parameter.
        z: origin fmesh data option ``z`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'ORIGIN'] = abc.Terminal[r'ORIGIN']('ORIGIN')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    x: literal.Real
    y: literal.Real
    z: literal.Real
