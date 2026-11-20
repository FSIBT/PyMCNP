import typing

from ..... import abc
from ..Ssr import Ssr
from .... import literal


class Axs(Ssr):
    """
    Represents axs ssr data options.

    Attributes:
        keyword: axs ssr data option ``r'AXS'`` symbol.
        equals: axs ssr data option ``r'='`` symbol.
        u: axs ssr data option ``u`` parameter.
        v: axs ssr data option ``v`` parameter.
        w: axs ssr data option ``w`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'AXS'] = abc.Terminal[r'AXS']('AXS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    u: literal.Real
    v: literal.Real
    w: literal.Real
