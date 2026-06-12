import typing
import decimal
import collections
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Wwn(Data):
    """
    Represents wwn data cards.

    Attributes:
        keyword: wwn data card `WWN` symbol.
        suffix: wwn data card `i` parameter.
        colon: wwn data card `colon` parameter.
        particle: wwn data card `particle` parameter.
        w: wwn data card `w` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'WWN'] | str = abc.Terminal[r'WWN']('WWN')
    suffix: literal.Integer | int | str
    colon: typing.Annotated[abc.Terminal, r':'] | str = abc.Terminal[r':'](':')
    particle: literal.Particle | str
    w: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )

    def __post_init__(self) -> None:
        """
        Validates wwn data cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (0 <= self.suffix):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
