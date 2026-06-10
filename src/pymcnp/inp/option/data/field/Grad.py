import typing
import decimal
import dataclasses

from ..... import abc
from .... import literal
from ..Field import Field


class Grad(Field):
    """
    Represents grad field data options.

    Attributes:
        keyword: grad field data option `GRAD` symbol.
        equals: grad field data option `=` symbol.
        r: grad field data option `r` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'GRAD'] | str = abc.Terminal[r'GRAD']('GRAD')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    r: literal.Real | int | float | decimal.Decimal | str
