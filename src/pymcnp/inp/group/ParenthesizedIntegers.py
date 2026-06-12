import typing
import dataclasses

from ... import abc
from .. import literal
from ..Group import Group


class ParenthesizedIntegers(Group):
    """
    Represents parenthesized integer groups.

    Attributes:
        parenthesis_open: parenthesized integer group `(` symbol.
        integers: parenthesized integer group integers.
        parenthesis_close: parenthesized integer group `)` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    parenthesis_open: typing.Annotated[abc.Terminal, r'\('] | str = abc.Terminal[r'\(']('(')
    integers: literal.CellIndex | str
    parenthesis_close: typing.Annotated[abc.Terminal, r'\)'] | str = abc.Terminal[r'\)'](')')
