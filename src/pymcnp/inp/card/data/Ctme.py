import typing
import decimal

from .... import abc
from ... import literal
from ..Data import Data


class Ctme(Data):
    """
    Represents ctme data cards.

    Attributes:
        keyword: ctme data card ``r'CTME'`` symbol.
        tme: ctme data card ``tme`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'CTME'] | str = abc.Terminal[r'CTME']('CTME')
    tme: literal.Real | int | float | decimal.Decimal | str
