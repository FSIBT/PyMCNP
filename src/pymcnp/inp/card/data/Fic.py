import typing

from .... import abc
from ... import literal
from ..Data import Data


class Fic(Data):
    """
    Represents fic data cards.

    Attributes:
        keyword: fic data card ``r'FIC'`` symbol.
        suffix: fic data card ``n`` parameter.
        colon: fic data card ``r':'`` symbol.
        particle: fic data card ``particle`` parameter.
        x1: fic data card ``x1`` parameter.
        y1: fic data card ``y1`` parameter.
        z1: fic data card ``z1`` parameter.
        r0: fic data card ``r0`` parameter.
        x2: fic data card ``x2`` parameter.
        y2: fic data card ``y2`` parameter.
        z2: fic data card ``z2`` parameter.
        f1: fic data card ``f1`` parameter.
        f2: fic data card ``f2`` parameter.
        f3: fic data card ``f3`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'FIC'] = abc.Terminal[r'FIC']('FIC')
    suffix: literal.Integer
    colon: typing.Annotated[abc.Terminal, r':'] = abc.Terminal[r':'](':')
    particle: literal.Particle
    x1: literal.Real
    y1: literal.Real
    z1: literal.Real
    r0: literal.Real
    x2: literal.Real
    y2: literal.Real
    z2: literal.Real
    f1: literal.Real
    f2: literal.Real | literal.Jump = literal.Jump('J')
    f3: literal.Real

    def __post_init__(self) -> None:
        """
        Validates fic data cards.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')

        if not self.r0 == 0:
            raise abc.Error('Invalid value.', f'{self.r0=}')

        if not self.f1 >= 0:
            raise abc.Error('Invalid value.', f'{self.f1=}')

        if self.f3 not in {0, 1}:
            raise abc.Error('Invalid value.', f'{self.f3=}')
