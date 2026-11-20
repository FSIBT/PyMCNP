import typing

from ..... import abc
from ..Bfld import Bfld
from .... import literal


class Mxdeflc(Bfld):
    """
    Represents mxdeflc bfld data options.

    Attributes:
        keyword: mxdeflc bfld data option ``r'MXDEFLC'`` symbol.
        equals: mxdeflc bfld data option ``r'='`` symbol.
        a: mxdeflc bfld data option ``a`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'MXDEFLC'] = abc.Terminal[r'MXDEFLC']('MXDEFLC')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    a: literal.Real
