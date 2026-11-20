import typing

from ..... import abc
from .... import literal
from ..Mesh import Mesh


class Axs(Mesh):
    """
    Represents axs mesh data options.

    Attributes:
        keyword: axs mesh data option ``r'AXS'`` symbol.
        equals: axs mesh data option ``r'='`` symbol.
        x: axs mesh data option ``x`` parameter.
        y: axs mesh data option ``y`` parameter.
        z: axs mesh data option ``z`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'AXS'] = abc.Terminal[r'AXS']('AXS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    x: literal.Real
    y: literal.Real
    z: literal.Real
