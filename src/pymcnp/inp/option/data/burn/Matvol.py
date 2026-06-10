import typing
import decimal
import dataclasses

from ..... import abc
from .... import literal
from ..Burn import Burn


class Matvol(Burn):
    """
    Represents matvol burn data options.

    Attributes:
        keyword: matvol burn data option `MATVOL` symbol.
        equals: matvol burn data option `=` symbol.
        v: matvol burn data option `v` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'MATVOL'] | str = abc.Terminal[r'MATVOL']('MATVOL')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    v: literal.Real | int | float | decimal.Decimal | str
