import typing

from .... import abc
from ... import literal
from ..Data import Data


class Fip(Data):
    """
    Represents fip data cards.

    Attributes:
        keyword: fip data card ``r'FIP'`` symbol.
        suffix: fip data card ``n`` parameter.
        colon: fip data card ``r':'`` symbol.
        particle: fip data card ``particle`` parameter.
        x1: fip data card ``x1`` parameter.
        y1: fip data card ``y1`` parameter.
        z1: fip data card ``z1`` parameter.
        r0: fip data card ``r0`` parameter.
        x2: fip data card ``x2`` parameter.
        y2: fip data card ``y2`` parameter.
        z2: fip data card ``z2`` parameter.
        f1: fip data card ``f1`` parameter.
        f2: fip data card ``f2`` parameter.
        f3: fip data card ``f3`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'FIP'] = abc.Terminal[r'FIP']('FIP')
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
    f1: literal.Real | literal.Jump = literal.Jump('J')
    f2: literal.Real
    f3: literal.Real

    def __post_init__(self) -> None:
        """
        Validates fip data cards.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')

        if not self.r0 == 0:
            raise abc.Error('Invalid value.', f'{self.r0=}')

        if isinstance(self.f1, literal.Real) and not self.f1 >= 0:
            raise abc.Error('Invalid value.', f'{self.f1=}')

        if not self.f2 >= 0:
            raise abc.Error('Invalid value.', f'{self.f2=}')
