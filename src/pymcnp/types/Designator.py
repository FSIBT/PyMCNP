import re
import typing

from . import _type
from .. import errors
from ..utils import _object


class Particle(_object.McnpTerminal):
    """
    Represents MCNP particle designators.
    """

    NEUTRON = 'n'
    ANTI_NEUTRON = 'q'
    PHOTON = 'p'
    ELECTRON = 'e'
    POSITRON = 'f'
    NEGATIVE_MUON = '|'
    POSITIVE_MUON = '!'
    ELECTRON_NEUTRINO = 'u'
    ANTI_ELECTRON_NEUTRINO = '<'
    MUON_NEUTRINO = 'v'
    ANTI_MUON_MEUTRINO = '>'
    PROTON = 'h'
    ANTI_PROTON = 'g'
    LAMBDA_BARYON = 'l'
    ANTI_LAMBDA_BARYON = 'b'
    POSITIVE_SIGMA_BARYON = '+'
    ANTI_POSITIVE_SIGMA_BARYON = '_'
    NEGATIVE_SIGMA_BARYON = '-'
    ANTI_NEGATIVE_SIGMA_BARYON = '~'
    CASCADE = 'x'
    ANTI_CASCADE = 'c'
    NEGATIVE_CASCADE = 'y'
    POSITIVE_CASCADE = 'w'
    OMEGA_BARYON = 'o'
    ANTI_OMEGA_BARYON = '@'
    POSITIVE_PION = '/'
    NEGATIVE_PION = '*'
    NEUTRAL_PION = 'z'
    POSITIVE_KAON = 'k'
    NEGATIVE_KAON = '?'
    SHORT_KAON = '%'
    LONG_KAON = '^'
    DEUTERON = 'd'
    TRITON = 't'
    HELION = 's'
    ALPHA = 'a'
    HEAVY_IONS = '#'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Particle`` from MCNP.

        Parameters:
            source: MCNP for ``Particle``.

        Returns:
            ``Particle``.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        try:
            return Particle(source)
        except Exception:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source)

    def to_mcnp(self):
        """
        Generates MCNP from ``Particle``.

        Returns:
            MCNP particle.
        """

        return str(self.value)


class Designator(_type.Type):
    """
    Represents MCNP particle designators.

    Attributes:
        particles: Designator particles.
    """

    _REGEX = re.compile(r'\A[nqpef|!u<v>hglb+_-~xcywo@/*zk?%^dtsa#]((?:,)[nqpef|!u<v>hglb+_-~xcywo@/*zk?%^dtsa#])*\Z')

    def __init__(self, particles: tuple[Particle]):
        """
        Initializes ``Designator``.

        Parameters:
            particles: Tuple of particles.

        Returns:
            ``Designator``.

        Raises:
            TypesError: SEMANTICS_TYPE.
        """

        if particles is None or None in particles:
            raise errors.TypesError(errors.TypesCode.SEMANTICS_TYPE, particles)

        self.particles: typing.Final[tuple[Particle]] = particles

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Designator`` from MCNP.

        Parameters:
            source: MCNP for ``Designator``.

        Returns:
            ``Designator``.

        Raises:
            TypesError: SYNTAX_TYPE.
        """

        try:
            return Designator(tuple(Particle.from_mcnp(token) for token in source.split(',')))
        except Exception:
            raise errors.TypesError(errors.TypesCode.SYNTAX_TYPE, source)

    def to_mcnp(self) -> str:
        """
        Generates MCNP from ``Designator``.

        Returns:
            MCNP designator.
        """

        return ','.join(particle.to_mcnp() for particle in self.particles)
