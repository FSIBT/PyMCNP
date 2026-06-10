import typing
import dataclasses

from ... import abc
from .. import literal
from ..Group import Group


class ParenthesizedIntegers(Group):
    """
    Represents parenthesizedinteger groups.

    Attributes:
        parenthesis_open:
        integers:
        parenthesis_close:
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    parenthesis_open: typing.Annotated[abc.Terminal, r'\('] | str = abc.Terminal[r'\(']('(')
    integers: literal.CellIndex | str
    parenthesis_close: typing.Annotated[abc.Terminal, r'\)'] | str = abc.Terminal[r'\)'](')')
