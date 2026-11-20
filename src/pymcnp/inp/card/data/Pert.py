import typing

from .... import abc
from ... import literal
from ..Data import Data
from ... import option


class Pert(Data):
    """
    Represents pert data cards.

    Attributes:
        keyword: pert data card ``r'PERT'`` symbol.
        suffix: pert data card ``n`` parameter.
        colon: pert data card ``r':'`` symbol.
        particle: pert data card ``particle`` parameter.
        options: pert data card ``options`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'PERT'] = abc.Terminal[r'PERT']('PERT')
    suffix: literal.Integer
    colon: typing.Annotated[abc.Terminal, r':'] = abc.Terminal[r':'](':')
    particle: literal.Particle
    options: typing.Annotated[abc.Array, option.data.Pert, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates pert data cards.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')

        if not isinstance(self.options, abc.Terminal) and not any(isinstance(keyvalue, option.data.pert.Cell) for keyvalue in self.options):
            raise abc.Error('Invalid value.', f'{self.options=}')
