import re
import typing

from . import _type
from .. import errors


class Designator(_type.Type):
    """
    Represents MCNP particle designators.

    Attributes:
        particles: Particle formula.
    """

    _REGEX = re.compile(r'\A([nqpef|!u<v>hglb+_-~xcywo@/*zk?%^dtsa#](?:,[nqpef|!u<v>hglb+_-~xcywo@/*zk?%^dtsa#])*)\Z', re.IGNORECASE)

    def __init__(self, particles: str):
        """
        Initializes `Designator`.

        Parameters:
            particles: Particle formula.

        Returns:
            `Designator`.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        if particles is None:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, particles)

        self.particles: typing.Final[str] = particles

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Designator` from MCNP.

        Parameters:
            source: MCNP for `Designator`.

        Returns:
            `Designator`.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        tokens = Designator._REGEX.match(source)

        if not tokens:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source)

        return Designator(tokens[0])

    def to_mcnp(self) -> str:
        """
        Generates MCNP from `Designator`.

        Returns:
            MCNP designator.
        """

        return self.particles
