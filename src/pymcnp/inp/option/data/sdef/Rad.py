import typing
import decimal
import dataclasses

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Rad(Sdef):
    """
    Represents rad sdef data options.

    Attributes:
        keyword: rad sdef data option `RAD` symbol.
        equals: rad sdef data option `equals` parameter.
        x: rad sdef data option `x` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'RAD'] | str = abc.Terminal[r'RAD']('RAD')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: literal.Real | literal.Distribution | literal.DependentDistribution | literal.EmbeddedDistribution | int | float | decimal.Decimal | str
