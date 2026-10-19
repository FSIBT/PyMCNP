import typing
import decimal
import dataclasses

from ..... import abc
from .... import literal
from ..Ft import Ft


class Geb(Ft):
    """
    Represents geb ft data options.

    Attributes:
        id: geb group `GEB` symbol.
        a: geb group `a` parameter.
        b: geb group `b` parameter.
        c: geb group `c` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    id: typing.Annotated[abc.Terminal, r'GEB'] | str = abc.Terminal[r'GEB']('GEB')
    a: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    b: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    c: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
