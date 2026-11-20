import typing

from ..... import abc
from ..Fmesh import Fmesh
from .... import literal


class Axs(Fmesh):
    """
    Represents axs fmesh data options.

    Attributes:
        keyword: axs fmesh data option ``r'AXS'`` symbol.
        equals: axs fmesh data option ``r'='`` symbol.
        x: axs fmesh data option ``x`` parameter.
        y: axs fmesh data option ``y`` parameter.
        z: axs fmesh data option ``z`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'AXS'] = abc.Terminal[r'AXS']('AXS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    x: literal.Real
    y: literal.Real
    z: literal.Real
