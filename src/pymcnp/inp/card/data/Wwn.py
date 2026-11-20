import typing

from .... import abc
from ... import literal
from ..Data import Data


class Wwn(Data):
    """
    Represents wwn data cards.

    Attributes:
        keyword: wwn data card ``r'WWN'`` symbol.
        suffix: wwn data card ``i`` parameter.
        colon: wwn data card ``colon`` parameter.
        particle: wwn data card ``particle`` parameter.
        w: wwn data card ``w`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'WWN'] = abc.Terminal[r'WWN']('WWN')
    suffix: literal.Integer
    colon: typing.Annotated[abc.Terminal, r':'] = abc.Terminal[r':'](':')
    particle: literal.Particle
    w: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates wwn data cards.

        Raises:
            Error: Invalid value.
        """

        if not (0 <= self.suffix):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
