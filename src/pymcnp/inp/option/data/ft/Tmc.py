import typing

from ..... import abc
from .... import literal
from ..Ft import Ft


class Tmc(Ft):
    """
    Represents tmc ft data options.

    Attributes:
        id: tmc group ``r'TMC'`` symbol.
        a: tmc group ``a`` parameter.
        b: tmc group ``b`` parameter.
    """

    id: typing.Annotated[abc.Terminal, r'TMC'] = abc.Terminal[r'TMC']('TMC')
    a: literal.Real
    b: literal.Real
