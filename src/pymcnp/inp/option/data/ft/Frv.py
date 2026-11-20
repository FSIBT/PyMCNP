import typing

from ..... import abc
from .... import literal
from ..Ft import Ft


class Frv(Ft):
    """
    Represents frv ft data options.

    Attributes:
        id: frv group ``r'FRV'`` symbol.
        v1: frv group ``v1`` parameter.
        v2: frv group ``v2`` parameter.
        v3: frv group ``v3`` parameter.
    """

    id: typing.Annotated[abc.Terminal, r'FRV'] = abc.Terminal[r'FRV']('FRV')
    v1: literal.Real
    v2: literal.Real
    v3: literal.Real
