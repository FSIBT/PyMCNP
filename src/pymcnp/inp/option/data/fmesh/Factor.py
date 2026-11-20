import typing

from ..... import abc
from ..Fmesh import Fmesh
from .... import literal


class Factor(Fmesh):
    """
    Represents factor fmesh data options.

    Attributes:
        keyword: factor fmesh data option ``r'FACTOR'`` symbol.
        equals: factor fmesh data option ``r'='`` symbol.
        value: factor fmesh data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'FACTOR'] = abc.Terminal[r'FACTOR']('FACTOR')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    value: literal.Real
