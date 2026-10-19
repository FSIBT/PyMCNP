import typing
import decimal
import collections
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Dxc(Data):
    """
    Represents dxc data cards.

    Attributes:
        keyword: dxc data card `DXC` symbol.
        suffix: dxc data card `n` parameter.
        colon: dxc data card `colon` parameter.
        particle: dxc data card `particle` parameter.
        p: dxc data card `p` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'DXC'] | str = abc.Terminal[r'DXC']('DXC')
    suffix: literal.Integer | int | str = dataclasses.field(kw_only=True)
    colon: typing.Annotated[abc.Terminal, r':'] | str = abc.Terminal[r':'](':')
    particle: literal.Particle | str = dataclasses.field(kw_only=True)
    p: (
        typing.Annotated[abc.Array, literal.Real | literal.Jump, None]
        | typing.Annotated[abc.Terminal, r'']
        | collections.abc.Sequence[literal.Real | literal.Jump | int | float | decimal.Decimal | str]
        | str
    ) = dataclasses.field(kw_only=True)

    def __post_init__(self) -> None:
        """
        Validates dxc data cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
