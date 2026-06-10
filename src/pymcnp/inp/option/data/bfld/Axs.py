import typing
import decimal
import dataclasses

from ..... import abc
from ..Bfld import Bfld
from .... import literal


class Axs(Bfld):
    """
    Represents axs bfld data options.

    Attributes:
        keyword: axs bfld data option `AXS` symbol.
        equals: axs bfld data option `=` symbol.
        uq: axs bfld data option `uq` parameter.
        vq: axs bfld data option `vq` parameter.
        wq: axs bfld data option `wq` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'AXS'] | str = abc.Terminal[r'AXS']('AXS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    uq: literal.Real | int | float | decimal.Decimal | str
    vq: literal.Real | int | float | decimal.Decimal | str
    wq: literal.Real | int | float | decimal.Decimal | str
