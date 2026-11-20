import typing

from .... import abc
from ... import literal
from ..Data import Data
from ... import option


class Fmesh(Data):
    """
    Represents fmesh data cards.

    Attributes:
        prefix: fmesh data card ``prefix`` parameter.
        keyword: fmesh data card ``r'FMESH'`` symbol.
        suffix: fmesh data card ``n`` parameter.
        colon: fmesh data card ``r':'`` symbol.
        particle: fmesh data card ``particle`` parameter.
        options: fmesh data card ``options`` parameter.
    """

    prefix: typing.Annotated[abc.Terminal, r'\*'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'FMESH'] = abc.Terminal[r'FMESH']('FMESH')
    suffix: literal.Integer
    colon: typing.Annotated[abc.Terminal, r':'] = abc.Terminal[r':'](':')
    particle: literal.Particle
    options: typing.Annotated[abc.Array, option.data.Fmesh, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates fmesh data cards.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
