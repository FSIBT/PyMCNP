import typing
import decimal
import dataclasses

from ..... import abc
from ..Ssr import Ssr
from .... import literal


class Axs(Ssr):
    """
    Represents axs ssr data options.

    Attributes:
        keyword: axs ssr data option `AXS` symbol.
        equals: axs ssr data option `=` symbol.
        u: axs ssr data option `u` parameter.
        v: axs ssr data option `v` parameter.
        w: axs ssr data option `w` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'AXS'] | str = abc.Terminal[r'AXS']('AXS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    u: literal.Real | int | float | decimal.Decimal | str
    v: literal.Real | int | float | decimal.Decimal | str
    w: literal.Real | int | float | decimal.Decimal | str
