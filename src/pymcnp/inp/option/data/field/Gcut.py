import typing

from ..... import abc
from .... import literal
from ..Field import Field


class Gcut(Field):
    """
    Represents gcut field data options.

    Attributes:
        keyword: gcut field data option ``r'GCUT'`` symbol.
        equals: gcut field data option ``r'='`` symbol.
        e: gcut field data option ``e`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'GCUT'] = abc.Terminal[r'GCUT']('GCUT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    e: literal.Real
