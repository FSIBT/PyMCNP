import typing

from .... import abc
from ... import literal
from ..Data import Data


class Pwt(Data):
    """
    Represents pwt data cards.

    Attributes:
        keyword: pwt data card ``r'PWT'`` symbol.
        w: pwt data card ``w`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'PWT'] = abc.Terminal[r'PWT']('PWT')
    w: typing.Annotated[abc.Array, literal.Real | literal.Jump, None] | typing.Annotated[abc.Terminal, r'']
