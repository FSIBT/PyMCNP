import typing


from .... import abc
from ... import literal
from ..Data import Data


class Void(Data):
    """
    Represents void data cards.

    Attributes:
        keyword: void data card ``r'VOID'`` symbol.
        c: void data card ``c`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'VOID'] = abc.Terminal[r'VOID']('VOID')
    c: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
