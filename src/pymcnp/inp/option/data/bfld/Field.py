import typing
import decimal

from ..... import abc
from ..Bfld import Bfld
from .... import literal


class Field(Bfld):
    """
    Represents field bfld data options.

    Attributes:
        keyword: field bfld data option `FIELD` symbol.
        equals: field bfld data option `=` symbol.
        f: field bfld data option `f` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'FIELD'] | str = abc.Terminal[r'FIELD']('FIELD')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    f: literal.Real | int | float | decimal.Decimal | str
