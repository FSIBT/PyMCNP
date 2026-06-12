import typing
import decimal
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Fic(Data):
    """
    Represents fic data cards.

    Attributes:
        keyword: fic data card `FIC` symbol.
        suffix: fic data card `n` parameter.
        colon: fic data card `:` symbol.
        particle: fic data card `particle` parameter.
        x1: fic data card `x1` parameter.
        y1: fic data card `y1` parameter.
        z1: fic data card `z1` parameter.
        r0: fic data card `r0` parameter.
        x2: fic data card `x2` parameter.
        y2: fic data card `y2` parameter.
        z2: fic data card `z2` parameter.
        f1: fic data card `f1` parameter.
        f2: fic data card `f2` parameter.
        f3: fic data card `f3` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'FIC'] | str = abc.Terminal[r'FIC']('FIC')
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
    f1: literal.Real | int | float | decimal.Decimal | str
    f2: literal.Real | literal.Jump | int | float | decimal.Decimal | str = literal.Jump('J')
    f3: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates fic data cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.suffix, literal.Integer)
        assert isinstance(self.r0, literal.Real)
        assert isinstance(self.f1, literal.Real)
        assert isinstance(self.f3, literal.Real)

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')

        if not self.r0 == 0:
            raise abc.Error('Invalid value.', f'{self.r0=}')

        if not self.f1 >= 0:
            raise abc.Error('Invalid value.', f'{self.f1=}')

        if self.f3 not in {0, 1}:
            raise abc.Error('Invalid value.', f'{self.f3=}')
