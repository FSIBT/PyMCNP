import typing
import decimal
import dataclasses

from ..... import abc
from .... import literal
from ..Burn import Burn


class Power(Burn):
    """
    Represents power burn data options.

    Attributes:
        keyword: power burn data option `POWER` symbol.
        equals: power burn data option `=` symbol.
        pwr: power burn data option `pwr` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'POWER'] | str = abc.Terminal[r'POWER']('POWER')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    pwr: literal.Real | int | float | decimal.Decimal | str
