import typing

from ..... import abc
from ..Kopts import Kopts


class Fmat(Kopts):
    """
    Represents fmat kopts data options.

    Attributes:
        keyword: fmat kopts data option ``r'FMAT'`` symbol.
        equals: fmat kopts data option ``r'='`` symbol.
        value: fmat kopts data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'FMAT'] | str = abc.Terminal[r'FMAT']('FMAT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:YES|NO)'] | str
