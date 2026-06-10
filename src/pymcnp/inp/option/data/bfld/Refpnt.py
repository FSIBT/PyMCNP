import typing
import decimal
import dataclasses

from ..... import abc
from ..Bfld import Bfld
from .... import literal


class Refpnt(Bfld):
    """
    Represents refpnt bfld data options.

    Attributes:
        keyword: refpnt bfld data option `REFPNT` symbol.
        equals: refpnt bfld data option `=` symbol.
        x: refpnt bfld data option `x` parameter.
        y: refpnt bfld data option `y` parameter.
        z: refpnt bfld data option `z` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'REFPNT'] | str = abc.Terminal[r'REFPNT']('REFPNT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: literal.Real | int | float | decimal.Decimal | str
    y: literal.Real | int | float | decimal.Decimal | str
    z: literal.Real | int | float | decimal.Decimal | str
