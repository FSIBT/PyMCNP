import typing

from ..... import abc
from ..Fmesh import Fmesh
from .... import literal


class Jmesh(Fmesh):
    """
    Represents jmesh fmesh data options.

    Attributes:
        keyword: jmesh fmesh data option ``r'JMESH'`` symbol.
        equals: jmesh fmesh data option ``r'='`` symbol.
        y: jmesh fmesh data option ``y`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'JMESH'] = abc.Terminal[r'JMESH']('JMESH')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    y: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
