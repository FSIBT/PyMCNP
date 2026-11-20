import typing

from .... import abc
from ... import literal
from ..Data import Data


class Dxc(Data):
    """
    Represents dxc data cards.

    Attributes:
        keyword: dxc data card ``r'DXC'`` symbol.
        suffix: dxc data card ``n`` parameter.
        colon: dxc data card ``colon`` parameter.
        particle: dxc data card ``particle`` parameter.
        p: dxc data card ``p`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'DXC'] = abc.Terminal[r'DXC']('DXC')
    suffix: literal.Integer
    colon: typing.Annotated[abc.Terminal, r':'] = abc.Terminal[r':'](':')
    particle: literal.Particle
    p: typing.Annotated[abc.Array, literal.Real | literal.Jump, None] | typing.Annotated[abc.Terminal, r'']

    def __post_init__(self) -> None:
        """
        Validates dxc data cards.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
