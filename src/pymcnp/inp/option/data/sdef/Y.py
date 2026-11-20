import typing

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Y(Sdef):
    """
    Represents y sdef data options.

    Attributes:
        keyword: y sdef data option ``r'Y'`` symbol.
        equals: y sdef data option ``equals`` parameter.
        y: y sdef data option ``y`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'Y'] = abc.Terminal[r'Y']('Y')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    y: literal.Real | literal.Distribution | literal.DependentDistribution | literal.EmbeddedDistribution
