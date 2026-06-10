import typing
import dataclasses

from .... import abc
from ..Cell import Cell
from ... import literal


class Nonu(Cell):
    """
    Represents nonu cell options.
    """

    pass


class Nonu_0(Nonu):
    """
    Represents nonu cell options, form #0.

    Attributes:
        keyword: nonu cell option `NONU` symbol.
        equals: nonu cell option `=` symbol.
        a: nonu cell option `a` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'NONU'] | str = abc.Terminal[r'NONU']('NONU')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    a: literal.Integer | int | str


class Nonu_1(Nonu):
    """
    Represents nonu cell options, form #1.

    Attributes:
        keyword: nonu cell option `NONU` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'NONU'] | str = abc.Terminal[r'NONU']('NONU')
