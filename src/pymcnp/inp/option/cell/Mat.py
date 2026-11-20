import typing

from .... import abc
from ..Cell import Cell
from ... import literal


class Mat(Cell):
    """
    Represents mat cell options.

    Attributes:
        keyword: mat cell option ``r'MAT'`` symbol.
        equals: mat cell option ``r'='`` symbol.
        m: mat cell option ``m`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'MAT'] = abc.Terminal[r'MAT']('MAT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    m: literal.Integer

    def __post_init__(self) -> None:
        """
        Validates mat cell options.

        Raises:
            Error: Invalid value.
        """

        if not (0 <= self.m <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.m=}')
