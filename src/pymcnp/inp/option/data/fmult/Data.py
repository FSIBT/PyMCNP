import typing

from ..... import abc
from ..Fmult import Fmult
from .... import literal


class Data(Fmult):
    """
    Represents data fmult data options.

    Attributes:
        keyword: data fmult data option ``r'DATA'`` symbol.
        equals: data fmult data option ``r'='`` symbol.
        d: data fmult data option ``d`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'DATA'] | str = abc.Terminal[r'DATA']('DATA')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    d: literal.Integer | int | str

    def __post_init__(self) -> None:
        """
        Validates data fmult data options.

        Raises:
            Error: Invalid value.
        """

        if self.d not in {0, 1, 2, 3}:
            raise abc.Error('Invalid value.', f'{self.d=}')
