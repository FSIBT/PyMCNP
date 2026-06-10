import typing
import decimal
import dataclasses

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Wgt(Sdef):
    """
    Represents wgt sdef data options.

    Attributes:
        keyword: wgt sdef data option `WGT` symbol.
        equals: wgt sdef data option `equals` parameter.
        x: wgt sdef data option `x` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'WGT'] | str = abc.Terminal[r'WGT']('WGT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: literal.Real | int | float | decimal.Decimal | str
