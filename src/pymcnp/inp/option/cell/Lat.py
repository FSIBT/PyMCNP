import typing
import dataclasses

from .... import abc
from ..Cell import Cell
from ... import literal


class Lat(Cell):
    """
    Represents lat cell options.

    Attributes:
        keyword: lat cell option `LAT` symbol.
        equals: lat cell option `=` symbol.
        n: lat cell option `n` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'LAT'] | str = abc.Terminal[r'LAT']('LAT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    n: literal.Integer | int | str

    def __post_init__(self) -> None:
        """
        Validates lat cell options.

        Raises:
            Error: Invalid value.
        """

        if self.n not in {1, 2}:
            raise abc.Error('Invalid value.', f'{self.n=}')
