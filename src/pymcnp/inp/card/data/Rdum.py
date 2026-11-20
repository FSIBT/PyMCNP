import typing

from .... import abc
from ... import literal
from ..Data import Data


class Rdum(Data):
    """
    Represents rdum data cards.

    Attributes:
        keyword: rdum data card ``r'RDUM'`` symbol.
        r: rdum data card ``r`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'RDUM'] = abc.Terminal[r'RDUM']('RDUM')
    r: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
