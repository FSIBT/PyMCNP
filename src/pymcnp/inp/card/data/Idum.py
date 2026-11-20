import typing


from .... import abc
from ... import literal
from ..Data import Data


class Idum(Data):
    """
    Represents idum data cards.

    Attributes:
        keyword: idum data card ``r'IDUM'`` symbol.
        i: idum data card ``i`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'IDUM'] = abc.Terminal[r'IDUM']('IDUM')
    i: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
