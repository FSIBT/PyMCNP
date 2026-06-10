import typing
import decimal
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Leb(Data):
    """
    Represents leb data cards.

    Attributes:
        keyword: leb data card `LEB` symbol.
        yzere: leb data card `yzere` parameter.
        bzere: leb data card `bzere` parameter.
        yzero: leb data card `yzero` parameter.
        bzero: leb data card `bzero` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'LEB'] | str = abc.Terminal[r'LEB']('LEB')
    yzere: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    bzere: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    yzero: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    bzero: literal.Real | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates leb data cards.
        """

        if isinstance(self.yzere, literal.Real) and not (self.yzere > 0):
            raise abc.Error('Invalid value.', f'{self.yzere=}')

        if isinstance(self.bzere, literal.Real) and not (self.bzere > 0):
            raise abc.Error('Invalid value.', f'{self.bzere=}')

        if isinstance(self.yzero, literal.Real) and not (self.yzero > 0):
            raise abc.Error('Invalid value.', f'{self.yzero=}')

        if isinstance(self.bzero, literal.Real) and not (self.bzero > 0):
            raise abc.Error('Invalid value.', f'{self.bzero=}')
