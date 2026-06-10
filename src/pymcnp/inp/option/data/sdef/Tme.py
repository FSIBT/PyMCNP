import typing
import decimal
import dataclasses

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Tme(Sdef):
    """
    Represents tme sdef data options.

    Attributes:
        keyword: tme sdef data option `TME` symbol.
        equals: tme sdef data option `equals` parameter.
        t: tme sdef data option `t` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'TME'] | str = abc.Terminal[r'TME']('TME')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    t: literal.Real | literal.Distribution | literal.DependentDistribution | literal.EmbeddedDistribution | int | float | decimal.Decimal | str
