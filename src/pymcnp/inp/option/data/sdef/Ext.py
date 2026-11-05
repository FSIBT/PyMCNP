import typing
import decimal

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Ext(Sdef):
    """
    Represents ext sdef data options.

    Attributes:
        keyword: ext sdef data option ``r'EXT'`` symbol.
        equals: ext sdef data option ``equals`` parameter.
        x: ext sdef data option ``x`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'EXT'] | str = abc.Terminal[r'EXT']('EXT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: literal.Real | literal.Distribution | literal.DependentDistribution | literal.EmbeddedDistribution | int | float | decimal.Decimal | str
