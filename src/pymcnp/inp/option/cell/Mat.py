import typing
import dataclasses

from .... import abc
from ..Cell import Cell
from ... import literal


class Mat(Cell):
    """
    Represents mat cell options.

    Attributes:
        keyword: mat cell option `MAT` symbol.
        equals: mat cell option `=` symbol.
        m: mat cell option `m` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'MAT'] | str = abc.Terminal[r'MAT']('MAT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    m: literal.Integer | int | str

    def __post_init__(self) -> None:
        """
        Validates mat cell options.
        """

        assert isinstance(self.m, literal.Integer)

        if not (0 <= self.m <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.m=}')
