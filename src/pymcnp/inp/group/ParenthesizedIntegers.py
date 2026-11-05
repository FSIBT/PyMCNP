import typing

from ... import abc
from .. import literal
from ..Group import Group


class ParenthesizedIntegers(Group):
    """
    Represents parenthesized integer groups.

    Attributes:
        parenthesis_open: parenthesized integer group ``r'('`` symbol.
        integers: parenthesized integer group integers.
        parenthesis_close: parenthesized integer group ``r')'`` symbol.
    """

    parenthesis_open: typing.Annotated[abc.Terminal, r'\('] | str = abc.Terminal[r'\(']('(')
    integers: literal.CellIndex | str
    parenthesis_close: typing.Annotated[abc.Terminal, r'\)'] | str = abc.Terminal[r'\)'](')')
