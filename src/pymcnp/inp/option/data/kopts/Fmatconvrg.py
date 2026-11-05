import typing

from ..... import abc
from ..Kopts import Kopts


class Fmatconvrg(Kopts):
    """
    Represents fmatconvrg kopts data options.

    Attributes:
        keyword: fmatconvrg kopts data option ``r'FMATCONVRG'`` symbol.
        equals: fmatconvrg kopts data option ``r'='`` symbol.
        value: fmatconvrg kopts data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'FMATCONVRG'] | str = abc.Terminal[r'FMATCONVRG']('FMATCONVRG')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:YES|NO)'] | str
