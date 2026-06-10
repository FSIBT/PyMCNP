import typing
import decimal
import dataclasses

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Pos(Sdef):
    """
    Represents pos sdef data options.
    """

    pass


class Pos_0(Pos):
    """
    Represents pos sdef data options, form #0.

    Attributes:
        keyword: pos sdef data option `POS` symbol.
        equals: pos sdef data option `equals` parameter.
        x: pos sdef data option `x` parameter.
        y: pos sdef data option `y` parameter.
        z: pos sdef data option `z` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'POS'] | str = abc.Terminal[r'POS']('POS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    x: literal.Real | int | float | decimal.Decimal | str
    y: literal.Real | int | float | decimal.Decimal | str
    z: literal.Real | int | float | decimal.Decimal | str


class Pos_1(Pos):
    """
    Represents pos sdef data options, form #1.

    Attributes:
        keyword: pos sdef data option `POS` symbol.
        equals: pos sdef data option `equals` parameter.
        value: pos sdef data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'POS'] | str = abc.Terminal[r'POS']('POS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Distribution | literal.DependentDistribution | str
