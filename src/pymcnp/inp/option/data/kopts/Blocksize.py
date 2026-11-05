import typing

from ..... import abc
from .... import literal
from ..Kopts import Kopts


class Blocksize(Kopts):
    """
    Represents blocksize kopts data options.

    Attributes:
        keyword: blocksize kopts data option ``r'BLOCKSIZE'`` symbol.
        equals: blocksize kopts data option ``r'='`` symbol.
        ncy: blocksize kopts data option ``ncy`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'BLOCKSIZE'] | str = abc.Terminal[r'BLOCKSIZE']('BLOCKSIZE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    ncy: literal.Integer | int | str

    def __post_init__(self) -> None:
        """
        Validates blocksize kopts data options.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.ncy, literal.Integer)

        if not self.ncy >= 2:
            raise abc.Error('Invalid value.', f'{self.ncy=}')
