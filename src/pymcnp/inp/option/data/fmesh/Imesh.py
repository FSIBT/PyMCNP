import typing

from ..... import abc
from ..Fmesh import Fmesh
from .... import literal


class Imesh(Fmesh):
    """
    Represents imesh fmesh data options.

    Attributes:
        keyword: imesh fmesh data option ``r'IMESH'`` symbol.
        equals: imesh fmesh data option ``r'='`` symbol.
        x: imesh fmesh data option ``x`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'IMESH'] = abc.Terminal[r'IMESH']('IMESH')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    x: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
