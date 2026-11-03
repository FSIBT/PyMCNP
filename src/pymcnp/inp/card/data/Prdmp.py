import typing

from .... import abc
from ... import literal
from ..Data import Data


class Prdmp(Data):
    """
    Represents prdmp data cards.

    Attributes:
        keyword: prdmp data card `PRDMP` symbol.
        ndp: prdmp data card `ndp` parameter.
        ndm: prdmp data card `ndm` parameter.
        mct: prdmp data card `mct` parameter.
        ndmp: prdmp data card `ndmp` parameter.
        dmmp: prdmp data card `dmmp` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'PRDMP'] | str = abc.Terminal[r'PRDMP']('PRDMP')
    ndp: literal.Integer | int | str
    ndm: literal.Integer | int | str
    mct: literal.Integer | int | str
    ndmp: literal.Integer | int | str
    dmmp: literal.Integer | int | str
