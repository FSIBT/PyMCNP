import typing

from ..... import abc
from ..Fmesh import Fmesh
from .... import literal


class Tmesh(Fmesh):
    """
    Represents tmesh fmesh data options.

    Attributes:
        keyword: tmesh fmesh data option ``r'TMESH'`` symbol.
        equals: tmesh fmesh data option ``r'='`` symbol.
        t: tmesh fmesh data option ``t`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'TMESH'] = abc.Terminal[r'TMESH']('TMESH')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    t: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
