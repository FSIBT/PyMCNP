import typing
import decimal
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Ctme(Data):
    """
    Represents ctme data cards.

    Attributes:
        keyword: ctme data card `CTME` symbol.
        tme: ctme data card `tme` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'CTME'] | str = abc.Terminal[r'CTME']('CTME')
    tme: literal.Real | int | float | decimal.Decimal | str
