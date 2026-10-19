import typing
import decimal
import dataclasses

from ..... import abc
from .... import literal
from ..Ft import Ft


class Frv(Ft):
    """
    Represents frv ft data options.

    Attributes:
        id: frv group `FRV` symbol.
        v1: frv group `v1` parameter.
        v2: frv group `v2` parameter.
        v3: frv group `v3` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    id: typing.Annotated[abc.Terminal, r'FRV'] | str = abc.Terminal[r'FRV']('FRV')
    v1: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    v2: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    v3: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
