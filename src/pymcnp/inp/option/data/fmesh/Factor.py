import typing
import decimal
import dataclasses

from ..... import abc
from ..Fmesh import Fmesh
from .... import literal


class Factor(Fmesh):
    """
    Represents factor fmesh data options.

    Attributes:
        keyword: factor fmesh data option `FACTOR` symbol.
        equals: factor fmesh data option `=` symbol.
        value: factor fmesh data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'FACTOR'] | str = abc.Terminal[r'FACTOR']('FACTOR')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Real | int | float | decimal.Decimal | str
