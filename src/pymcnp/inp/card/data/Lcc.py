import typing
import decimal
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Lcc(Data):
    """
    Represents lcc data cards.

    Attributes:
        keyword: lcc data card `LCC` symbol.
        stincl: lcc data card `stincl` parameter.
        v0incl: lcc data card `v0incl` parameter.
        xfoisaincl: lcc data card `xfoisaincl` parameter.
        npaulincl: lcc data card `npaulincl` parameter.
        nosurfincl: lcc data card `nosurfincl` parameter.
        j_0: phys data card `J` parameter, #0.
        j_1: phys data card `J` parameter, #1.
        ecutincl: lcc data card `ecutincl` parameter.
        ebankincl: lcc data card `ebankincl` parameter.
        ebankabia: lcc data card `ebankabia` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'LCC'] | str = abc.Terminal[r'LCC']('LCC')
    stincl: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    v0incl: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    xfoisaincl: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    npaulincl: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | str | int = literal.Jump('J')
    nosurfincl: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | str | int = literal.Jump('J')
    j_0: literal.Jump | typing.Annotated[abc.Terminal, r''] | str = literal.Jump('J')
    j_1: literal.Jump | typing.Annotated[abc.Terminal, r''] | str = literal.Jump('J')
    ecutincl: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    ebankincl: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    ebankabia: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')

    def __post_init__(self) -> None:
        """
        Validates lcc data cards.
        """

        if isinstance(self.npaulincl, literal.Integer) and self.npaulincl not in {1, 0, -1}:
            raise abc.Error('Invalid value.', f'{self.npaulincl=}')

        if isinstance(self.nosurfincl, literal.Integer) and self.nosurfincl not in {-2, -1, 0, 1}:
            raise abc.Error('Invalid value.', f'{self.nosurfincl=}')
