import typing

from ..... import abc
from ..Kopts import Kopts


class Precursor(Kopts):
    """
    Represents precursor kopts data options.

    Attributes:
        keyword: precursor kopts data option ``r'PRECURSOR'`` symbol.
        equals: precursor kopts data option ``r'='`` symbol.
        value: precursor kopts data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'PRECURSOR'] | str = abc.Terminal[r'PRECURSOR']('PRECURSOR')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:YES|NO)'] | str
