import typing


from .... import abc
from ... import literal
from ..Data import Data


class Talnp(Data):
    """
    Represents talnp data cards.

    Attributes:
        keyword: talnp data card ``r'TALNP'`` symbol.
        t: talnp data card ``t`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'TALNP'] = abc.Terminal[r'TALNP']('TALNP')
    t: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
