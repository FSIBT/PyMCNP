import typing
import decimal
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Fip(Data):
    """
    Represents fip data cards.

    Attributes:
        keyword: fip data card `FIP` symbol.
        suffix: fip data card `n` parameter.
        colon: fip data card `:` symbol.
        particle: fip data card `particle` parameter.
        x1: fip data card `x1` parameter.
        y1: fip data card `y1` parameter.
        z1: fip data card `z1` parameter.
        r0: fip data card `r0` parameter.
        x2: fip data card `x2` parameter.
        y2: fip data card `y2` parameter.
        z2: fip data card `z2` parameter.
        f1: fip data card `f1` parameter.
        f2: fip data card `f2` parameter.
        f3: fip data card `f3` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'FIP'] | str = abc.Terminal[r'FIP']('FIP')
    suffix: literal.Integer | int | str
    colon: typing.Annotated[abc.Terminal, r':'] | str = abc.Terminal[r':'](':')
    particle: literal.Particle | str
    x1: literal.Real | int | float | decimal.Decimal | str
    y1: literal.Real | int | float | decimal.Decimal | str
    z1: literal.Real | int | float | decimal.Decimal | str
    r0: literal.Real | int | float | decimal.Decimal | str
    x2: literal.Real | int | float | decimal.Decimal | str
    y2: literal.Real | int | float | decimal.Decimal | str
    z2: literal.Real | int | float | decimal.Decimal | str
    f1: literal.Real | literal.Jump | int | float | decimal.Decimal | str = literal.Jump('J')
    f2: literal.Real | int | float | decimal.Decimal | str
    f3: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates fip data cards.
        """

        assert isinstance(self.suffix, literal.Integer)
        assert isinstance(self.r0, literal.Real)
        assert isinstance(self.f1, (literal.Real, literal.Jump))
        assert isinstance(self.f2, literal.Real)

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')

        if not self.r0 == 0:
            raise abc.Error('Invalid value.', f'{self.r0=}')

        if isinstance(self.f1, literal.Real) and not self.f1 >= 0:
            raise abc.Error('Invalid value.', f'{self.f1=}')

        if not self.f2 >= 0:
            raise abc.Error('Invalid value.', f'{self.f2=}')
