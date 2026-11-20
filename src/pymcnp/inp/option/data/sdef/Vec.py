import typing

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Vec(Sdef):
    """
    Represents vec sdef data options.
    """


class Vec_0(Vec):
    """
    Represents vec sdef data options, form #0.

    Attributes:
        keyword: vec sdef data option ``r'VEC'`` symbol.
        equals: vec sdef data option ``equals`` parameter.
        x: vec sdef data option ``x`` parameter.
        y: vec sdef data option ``y`` parameter.
        z: vec sdef data option ``z`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'VEC'] = abc.Terminal[r'VEC']('VEC')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    x: literal.Real
    y: literal.Real
    z: literal.Real


class Vec_1(Vec):
    """
    Represents vec sdef data options, form #1.

    Attributes:
        keyword: vec sdef data option ``r'VEC'`` symbol.
        equals: vec sdef data option ``equals`` parameter.
        value: vec sdef data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'VEC'] = abc.Terminal[r'VEC']('VEC')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    value: literal.Distribution | literal.DependentDistribution
