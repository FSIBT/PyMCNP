import typing
import decimal
import dataclasses

from ..... import abc
from ..Bfld import Bfld
from .... import literal


class Mxdeflc(Bfld):
    """
    Represents mxdeflc bfld data options.

    Attributes:
        keyword: mxdeflc bfld data option `MXDEFLC` symbol.
        equals: mxdeflc bfld data option `=` symbol.
        a: mxdeflc bfld data option `a` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'MXDEFLC'] | str = abc.Terminal[r'MXDEFLC']('MXDEFLC')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    a: literal.Real | int | float | decimal.Decimal | str
