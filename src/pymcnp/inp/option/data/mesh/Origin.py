import typing

from ..... import abc
from .... import literal
from ..Mesh import Mesh


class Origin(Mesh):
    """
    Represents origin mesh data options.

    Attributes:
        keyword: origin mesh data option ``r'ORIGIN'`` symbol.
        equals: origin mesh data option ``r'='`` symbol.
        x: origin mesh data option ``x`` parameter.
        y: origin mesh data option ``y`` parameter.
        z: origin mesh data option ``z`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'ORIGIN'] = abc.Terminal[r'ORIGIN']('ORIGIN')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    x: literal.Real
    y: literal.Real
    z: literal.Real
