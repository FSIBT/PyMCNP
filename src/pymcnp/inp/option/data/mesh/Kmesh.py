import typing

from ..... import abc
from .... import literal
from ..Mesh import Mesh


class Kmesh(Mesh):
    """
    Represents kmesh mesh data options.

    Attributes:
        keyword: kmesh mesh data option ``r'KMESH'`` symbol.
        equals: kmesh mesh data option ``r'='`` symbol.
        z: kmesh mesh data option ``z`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'KMESH'] = abc.Terminal[r'KMESH']('KMESH')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    z: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
