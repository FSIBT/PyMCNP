import typing

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Cel(Sdef):
    """
    Represents cel sdef data options.

    Attributes:
        keyword: cel sdef data option ``r'CEL'`` symbol.
        equals: cel sdef data option ``equals`` parameter.
        c: cel sdef data option ``c`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'CEL'] | str = abc.Terminal[r'CEL']('CEL')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    c: literal.Integer | literal.CellIndex | literal.Distribution | literal.DependentDistribution | literal.EmbeddedDistribution | int | str
