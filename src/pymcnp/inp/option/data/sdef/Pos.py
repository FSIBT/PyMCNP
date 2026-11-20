import typing

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Pos(Sdef):
    """
    Represents pos sdef data options.
    """


class Pos_0(Pos):
    """
    Represents pos sdef data options, form #0.

    Attributes:
        keyword: pos sdef data option ``r'POS'`` symbol.
        equals: pos sdef data option ``equals`` parameter.
        x: pos sdef data option ``x`` parameter.
        y: pos sdef data option ``y`` parameter.
        z: pos sdef data option ``z`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'POS'] = abc.Terminal[r'POS']('POS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    x: literal.Real
    y: literal.Real
    z: literal.Real


class Pos_1(Pos):
    """
    Represents pos sdef data options, form #1.

    Attributes:
        keyword: pos sdef data option ``r'POS'`` symbol.
        equals: pos sdef data option ``equals`` parameter.
        value: pos sdef data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'POS'] = abc.Terminal[r'POS']('POS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    value: literal.Distribution | literal.DependentDistribution
