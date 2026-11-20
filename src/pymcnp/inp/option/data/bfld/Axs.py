import typing

from ..... import abc
from ..Bfld import Bfld
from .... import literal


class Axs(Bfld):
    """
    Represents axs bfld data options.

    Attributes:
        keyword: axs bfld data option ``r'AXS'`` symbol.
        equals: axs bfld data option ``r'='`` symbol.
        uq: axs bfld data option ``uq`` parameter.
        vq: axs bfld data option ``vq`` parameter.
        wq: axs bfld data option ``wq`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'AXS'] = abc.Terminal[r'AXS']('AXS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    uq: literal.Real
    vq: literal.Real
    wq: literal.Real
