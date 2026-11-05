import typing

from ..... import abc
from ..Kopts import Kopts


class Fmatreduce(Kopts):
    """
    Represents fmatreduce kopts data options.

    Attributes:
        keyword: fmatreduce kopts data option ``r'FMATREDUCE'`` symbol.
        equals: fmatreduce kopts data option ``r'='`` symbol.
        value: fmatreduce kopts data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'FMATREDUCE'] | str = abc.Terminal[r'FMATREDUCE']('FMATREDUCE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:YES|NO)'] | str
