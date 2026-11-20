import typing

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class X(Sdef):
    """
    Represents x sdef data options.

    Attributes:
        keyword: x sdef data option ``r'X'`` symbol.
        equals: x sdef data option ``equals`` parameter.
        x: x sdef data option ``x`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'X'] = abc.Terminal[r'X']('X')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    x: literal.Real | literal.Distribution | literal.DependentDistribution | literal.EmbeddedDistribution
