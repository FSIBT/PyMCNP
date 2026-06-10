import typing
import dataclasses

from ..... import abc
from ..Fmult import Fmult
from .... import literal


class Shift(Fmult):
    """
    Represents shift fmult data options.

    Attributes:
        keyword: shift fmult data option `SHIFT` symbol.
        equals: shift fmult data option `=` symbol.
        s: shift fmult data option `s` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'SHIFT'] | str = abc.Terminal[r'SHIFT']('SHIFT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    s: literal.Integer | int | str

    def __post_init__(self) -> None:
        """
        Validates shift fmult data options.
        """

        if self.s not in {0, 1, 2, 3, 4}:
            raise abc.Error('Invalid value.', f'{self.s=}')
