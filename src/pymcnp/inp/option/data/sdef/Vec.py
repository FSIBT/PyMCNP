import typing
import decimal
import dataclasses

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Vec(Sdef):
    """
    Represents vec sdef data options.
    """

    pass


class Vec_0(Vec):
    """
    Represents vec sdef data options, form #0.

    Attributes:
        keyword: vec sdef data option `VEC` symbol.
        equals: vec sdef data option `equals` parameter.
        x: vec sdef data option `x` parameter.
        y: vec sdef data option `y` parameter.
        z: vec sdef data option `z` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'VEC'] | str = abc.Terminal[r'VEC']('VEC')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: literal.Real | int | float | decimal.Decimal | str
    y: literal.Real | int | float | decimal.Decimal | str
    z: literal.Real | int | float | decimal.Decimal | str


class Vec_1(Vec):
    """
    Represents vec sdef data options, form #1.

    Attributes:
        keyword: vec sdef data option `VEC` symbol.
        equals: vec sdef data option `equals` parameter.
        value: vec sdef data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'VEC'] | str = abc.Terminal[r'VEC']('VEC')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Distribution | literal.DependentDistribution | str
