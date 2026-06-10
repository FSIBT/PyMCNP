import typing
import decimal
import dataclasses

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Eff(Sdef):
    """
    Represents eff sdef data options.

    Attributes:
        keyword: eff sdef data option `EFF` symbol.
        equals: eff sdef data option `equals` parameter.
        x: eff sdef data option `x` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'EFF'] | str = abc.Terminal[r'EFF']('EFF')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: literal.Real | int | float | decimal.Decimal | str
