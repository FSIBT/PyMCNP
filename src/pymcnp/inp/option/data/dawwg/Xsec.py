import typing
import dataclasses

from ..... import abc
from ..Dawwg import Dawwg


class Xsec(Dawwg):
    """
    Represents xsec dawwg data options.

    Attributes:
        keyword: xsec dawwg data option `XSEC` symbol.
        equals: xsec dawwg data option `=` symbol.
        name: xsec dawwg data option `name` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'XSEC'] | str = abc.Terminal[r'XSEC']('XSEC')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    name: typing.Annotated[abc.Terminal, r'\S+'] | str
