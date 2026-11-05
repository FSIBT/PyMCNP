import typing
import decimal

from ..... import abc
from ..Stop import Stop
from .... import literal


class Ctme(Stop):
    """
    Represents ctme stop data options.

    Attributes:
        keyword: ctme stop data option ``r'CTME'`` symbol.
        equals: ctme stop data option ``r'='`` symbol.
        tme: ctme stop data option ``tme`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'CTME'] | str = abc.Terminal[r'CTME']('CTME')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    tme: literal.Real | int | float | decimal.Decimal | str
