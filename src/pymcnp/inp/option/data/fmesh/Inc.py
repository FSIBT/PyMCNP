import typing

from ..... import abc
from ..Fmesh import Fmesh
from .... import literal


class Inc(Fmesh):
    """
    Represents inc fmesh data options.
    """


class Inc_0(Inc):
    """
    Represents inc fmesh data options, form #0.

    Attributes:
        keyword: inc fmesh data option ``r'INC'`` symbol.
        equals: inc fmesh data option ``r'='`` symbol.
        low: inc fmesh data option ``low`` parameter.
        high: inc fmesh data option ``high`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'INC'] = abc.Terminal[r'INC']('INC')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    low: literal.Integer | literal.Jump = literal.Jump('J')
    high: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r'INFINITE'] | typing.Annotated[abc.Terminal, r''] = literal.Jump('J')


class Inc_1(Inc):
    """
    Represents inc fmesh data options, form #1.

    Attributes:
        keyword: inc fmesh data option ``r'INC'`` symbol.
    """

    keyword: typing.Annotated[abc.Terminal, r'INC'] = abc.Terminal[r'INC']('INC')
