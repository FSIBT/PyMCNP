import typing
import dataclasses

from ..... import abc
from .... import literal
from ..Kopts import Kopts


class Blocksize(Kopts):
    """
    Represents blocksize kopts data options.

    Attributes:
        keyword: blocksize kopts data option `BLOCKSIZE` symbol.
        equals: blocksize kopts data option `=` symbol.
        ncy: blocksize kopts data option `ncy` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

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
