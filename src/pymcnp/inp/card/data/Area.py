import typing

from .... import abc
from ... import literal
from ..Data import Data


class Area(Data):
    """
    Represents area data cards.

    Attributes:
        keyword: area data card ``r'AREA'`` symbol.
        x: area data card ``x`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'AREA'] = abc.Terminal[r'AREA']('AREA')
    x: typing.Annotated[abc.Array, literal.Real | literal.Jump, None] | typing.Annotated[abc.Terminal, r'']
