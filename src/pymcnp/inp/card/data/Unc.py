import typing
import dataclasses


from .... import abc
from ... import literal
from ..Data import Data


class Unc(Data):
    """
    Represents unc data cards.

    Attributes:
        keyword: unc data card ``r'UNC'`` symbol.
        colon: unc data card ``r':'`` symbol.
        particle: unc data card ``particle`` parameter.
        u: unc data card ``u`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'UNC'] = abc.Terminal[r'UNC']('UNC')
    colon: typing.Annotated[abc.Terminal, r':'] = abc.Terminal[r':'](':')
    particle: literal.Particle
    u: typing.Annotated[abc.Array, literal.Integer | literal.Jump, None] | typing.Annotated[abc.Terminal, r''] = dataclasses.field(kw_only=True)

    def __post_init__(self) -> None:
        """
        Validates unc data cards.

        Raises:
            Error: Invalid value.
        """

        if not isinstance(self.u, abc.Terminal) and not all(uj in {0, 1} for uj in self.u):
            raise abc.Error('Invalid value.', f'{self.u=}')
