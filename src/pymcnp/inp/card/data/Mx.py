import typing


from .... import abc
from ... import literal
from ..Data import Data


class Mx(Data):
    """
    Represents mx data cards.

    Attributes:
        keyword: mx data card ``r'MX'`` symbol.
        suffix: mx data card ``n`` parameter.
        colon: mx data card ``r':'`` symbol.
        particle: mx data card ``particle`` parameter.
        z: mx data card ``z`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'MX'] = abc.Terminal[r'MX']('MX')
    suffix: literal.Integer
    colon: typing.Annotated[abc.Terminal, r':'] = abc.Terminal[r':'](':')
    particle: literal.Particle
    z: typing.Annotated[abc.Array, literal.Zaid | typing.Annotated[abc.Terminal, r'MODEL|0'], None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates mx data cards.

        Raises:
            Error: Invalid value.
        """

        if not (0 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
