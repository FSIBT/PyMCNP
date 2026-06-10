import typing
import decimal
import dataclasses

from ..... import abc
from .... import literal
from ..Field import Field


class Gcut(Field):
    """
    Represents gcut field data options.

    Attributes:
        keyword: gcut field data option `GCUT` symbol.
        equals: gcut field data option `=` symbol.
        e: gcut field data option `e` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'GCUT'] | str = abc.Terminal[r'GCUT']('GCUT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    e: literal.Real | int | float | decimal.Decimal | str
