import typing

from .... import abc
from ... import literal
from ..Data import Data


class Prdmp(Data):
    """
    Represents prdmp data cards.

    Attributes:
        keyword: prdmp data card ``r'PRDMP'`` symbol.
        ndp: prdmp data card ``ndp`` parameter.
        ndm: prdmp data card ``ndm`` parameter.
        mct: prdmp data card ``mct`` parameter.
        ndmp: prdmp data card ``ndmp`` parameter.
        dmmp: prdmp data card ``dmmp`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'PRDMP'] = abc.Terminal[r'PRDMP']('PRDMP')
    ndp: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] = literal.Jump('J')
    ndm: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] = literal.Jump('J')
    mct: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] = literal.Jump('J')
    ndmp: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] = literal.Jump('J')
    dmmp: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] = literal.Jump('J')
