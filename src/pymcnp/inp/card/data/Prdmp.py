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
    ndp: literal.Integer
    ndm: literal.Integer
    mct: literal.Integer
    ndmp: literal.Integer
    dmmp: literal.Integer
