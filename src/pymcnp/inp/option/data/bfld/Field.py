import typing

from ..... import abc
from ..Bfld import Bfld
from .... import literal


class Field(Bfld):
    """
    Represents field bfld data options.

    Attributes:
        keyword: field bfld data option ``r'FIELD'`` symbol.
        equals: field bfld data option ``r'='`` symbol.
        f: field bfld data option ``f`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'FIELD'] = abc.Terminal[r'FIELD']('FIELD')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    f: literal.Real
