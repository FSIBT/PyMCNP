import typing

from ..... import abc
from ..Dawwg import Dawwg


class Xsec(Dawwg):
    """
    Represents xsec dawwg data options.

    Attributes:
        keyword: xsec dawwg data option ``r'XSEC'`` symbol.
        equals: xsec dawwg data option ``r'='`` symbol.
        name: xsec dawwg data option ``name`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'XSEC'] | str = abc.Terminal[r'XSEC']('XSEC')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    name: typing.Annotated[abc.Terminal, r'\S+'] | str
