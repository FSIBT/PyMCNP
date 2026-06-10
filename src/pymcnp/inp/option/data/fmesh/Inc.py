import typing
import decimal
import dataclasses

from ..... import abc
from ..Fmesh import Fmesh
from .... import literal


class Inc(Fmesh):
    """
    Represents inc fmesh data options.
    """

    pass


class Inc_0(Inc):
    """
    Represents inc fmesh data options, form #0.

    Attributes:
        keyword: inc fmesh data option `INC` symbol.
        equals: inc fmesh data option `=` symbol.
        low: inc fmesh data option `low` parameter.
        high: inc fmesh data option `high` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'INC'] | str = abc.Terminal[r'INC']('INC')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    low: literal.Integer | literal.Jump | int | str = literal.Jump('J')
    high: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r'INFINITE'] | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')


class Inc_1(Inc):
    """
    Represents inc fmesh data options, form #1.

    Attributes:
        keyword: inc fmesh data option `INC` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'INC'] | str = abc.Terminal[r'INC']('INC')
