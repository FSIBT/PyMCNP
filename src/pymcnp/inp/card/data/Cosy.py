import typing


from .... import abc
from ... import literal
from ..Data import Data


class Cosy(Data):
    """
    Represents cosy data cards.

    Attributes:
        keyword: cosy data card ``r'COSY'`` symbol.
        m: cosy data card ``m`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'COSY'] = abc.Terminal[r'COSY']('COSY')
    m: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
