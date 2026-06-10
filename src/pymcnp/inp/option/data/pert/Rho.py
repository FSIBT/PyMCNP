import typing
import decimal
import dataclasses

from ..... import abc
from ..Pert import Pert
from .... import literal


class Rho(Pert):
    """
    Represents rho pert data options.

    Attributes:
        keyword: rho pert data option `RHO` symbol.
        equals: rho pert data option `=` symbol.
        r: rho pert data option `r` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'RHO'] | str = abc.Terminal[r'RHO']('RHO')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    r: literal.Real | int | float | decimal.Decimal | str
