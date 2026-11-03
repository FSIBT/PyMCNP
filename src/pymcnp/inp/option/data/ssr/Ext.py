import typing

from ..... import abc
from ..Ssr import Ssr
from .... import literal


class Ext(Ssr):
    """
    Represents ext ssr data options.

    Attributes:
        keyword: ext ssr data option `EXT` symbol.
        equals: ext ssr data option `=` symbol.
        n: ext ssr data option `n` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'EXT'] | str = abc.Terminal[r'EXT']('EXT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    n: literal.Distribution | str
