"""
``types`` contains class representing basic MCNP types.

``types`` packages the ``McnpInteger``, ``McnpReal``, ``Zaid``, and
``Designator`` classes, providing an object-oriented, importable interface for
MCNP types.
"""

from __future__ import annotations
import re
import enum
from typing import Literal, Final

from . import _parser
from . import errors


class DistributionNumber:
    """
    ``DistributionNumber`` represents MCNP distribution numbers.

    Attributes:
        n: number.
    """

    def __init__(self, n: int):
        """
        ``__init__`` initializes ``DistributionNumber``.

        Parameters:
            n: number.
        """

        if n is None or not (1 <= n <= 999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DN, info=str(n))

        self.n: Final[int] = n

    @staticmethod
    def from_mcnp(source: str):
        """
        ``from_mcnp`` generates ``DistributionNumber`` objects from INP.

        ``from_mcnp`` constructs instances of ``DistributionNumber`` from INP
        source strings, so it operates as a class constructor method
        and INP parser helper function.

        Parameters:
            source: INP for distribution number.

        Returns:
            ``DistributionNumber`` object.
        """

        source = _parser.Preprocessor.process_inp(source)

        match = re.match(r'\A[dD](\d|\d\d|\d\d\d)\Z', source)
        if match is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DN, info=source)

        return DistributionNumber(int(match[1]))


class Zaid:
    """
    ``Zaid`` represents nuclide information numbers.

    Attributes:
        z: Atomic number.
        a: Mass number.
        abx: Cross-section evaluation & class information.
    """

    def __init__(self, z: int, a: int, abx: str = None):
        """
        ``__init__`` initializes ``Zaid``.

        Parameters:
            z: Atomic number.
            a: Mass number.
            abx: Cross-section evaluation & class information.
        """

        if z is None or not (000 <= z <= 999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_ZAID_Z, info=str(z))

        if a is None or not (000 <= a <= 999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_ZAID_A, info=str(a))

        # if abx is None:
        #    raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_ZAID_ABX, info = str(abx))

        self.z: Final[int] = z
        self.a: Final[int] = a
        self.abx: Final[str] = abx

    @staticmethod
    def from_mcnp(source: str):
        """
        ``from_mcnp`` generates ``Zaid`` objects from INP.

        ``from_mcnp`` constructs instances of ``Zaid`` from INP
        source strings, so it operates as a class constructor method
        and INP parser helper function.

        Parameters:
            source: INP for zaid.

        Returns:
            ``Zaid`` object.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            source.split('.'),
            errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_ZAID),
        )

        zzzaaa = tokens.popl()
        if len(zzzaaa) < 4:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_ZAID_Z, info=source)

        try:
            a = int(zzzaaa[-3:])
        except ValueError:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_ZAID_A, info=source)

        try:
            z = int(zzzaaa[:-3])
        except ValueError:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_ZAID_Z, info=source)

        abx = None
        if tokens:
            abx = tokens.popl()

        if tokens:
            raise errors.MCNPSytnaxError(errors.MCNPSytnaxCodes.TOOLONG_ZAID)

        return Zaid(z, a, abx)

    def to_mcnp(self) -> str:
        """
        ``to_mcnp`` generates INP from ``Zaid`` objects.

        ``to_mcnp`` creates INP source string from ``Zaid``
        objects, so it provides an MCNP endpoint.

        Returns:
            INP string for ``Zaid`` object.
        """

        return (
            f'{self.z:03}{self.a:03}.{self.abx}'
            if self.abx is not None
            else f'{self.z:03}{self.a:03}'
        )


class Designator:
    """
    ``Designator`` represents MCNP particle designators.

    Attributes:
        particles: Tuple of particles.
    """

    class Particle(str, enum.Enum):
        """
        ``Particle`` represents individular particle designators.
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

    def __init__(self, particles: tuple[Particle]):
        """
        ``__init__`` initializes ``Designator``.

        Parameters:
            particles: Tuple of particles.

        Raises:
            MCNPSemanticError: INVALID_MCNP_DESIGNATOR.
        """

        if particles is None:
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_MCNP_DESIGNATOR, info=str(particles)
            )

        for particle in particles:
            if particle is None:
                raise errors.MCNPSemanticError(
                    errors.MCNPSemanticCodes.INVALID_MCNP_DESIGNATOR,
                    info=str(particles),
                )

        self.particles: Final[tuple[Designator.Particle]] = particles

    @staticmethod
    def from_mcnp(source: str):
        """
        ``from_mcnp`` generates ``Designator`` objects from INP.

        ``from_mcnp`` constructs instances of ``Designator`` from INP
        source strings, so it operates as a class constructor method
        and INP parser helper function.

        Parameters:
            source: INP for particle designator(s).

        Returns:
            Tuple of ``Designator`` objects.
        """

        try:
            particles = tuple([Designator.Particle(token) for token in source.split(',')])
        except ValueError:
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_MCNP_DESIGNATOR, info=source
            )

        return Designator(particles)

    def to_mcnp(self) -> str:
        """
        ``to_mcnp`` generates INP from ``Designator`` objects.

        ``to_mcnp`` creates INP source string from ``Designator``
        objects, so it provides an MCNP endpoint.

        Returns:
            INP string for ``Designator`` object.
        """

        return ','.join(Designator.Particle(particle) for particle in self.particles)

    def __eq__(self, other):
        return self.particles == other.particles


class McnpInteger:
    """
    ``McnpInteger`` represents the INP integer value.

    Attributes:
        value: Integer or J jump symbol.
    """

    def __init__(self, value: int | Literal['j']):
        """
        ``__init__`` initializes ``McnpInteger``.

        Parameters:
            value: Integer or J jump symbol.

        Raises:
            MCNPSemanticError: INVALID_MCNP_INTEGER.
        """

        if value is None:
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_MCNP_INTEGER, info=str(value)
            )

        if isinstance(value, int):
            value = value
        elif value == 'j':
            value = 'j'
        else:
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_MCNP_INTEGER, info=str(value)
            )

        self.value: Final[int | Literal['j']] = value

    @staticmethod
    def from_mcnp(source: str):
        """
        ``from_mcnp`` generates ``McnpInteger`` objects from INP.

        ``from_mcnp`` constructs instances of ``McnpInteger`` from INP
        source strings, so it operates as a class constructor method
        and INP parser helper function.

        Parameters:
            source: INP for value.

        Returns:
            ``McnpInteger`` object.
        """

        source = _parser.Preprocessor.process_inp(source)

        if re.match(r'\A[+-]?[0-9]+[Ee][+-]?[0-9]+\Z', source):
            delimiters = re.findall(r'[+-]', source)
            content = re.split(r'[+-]', source)

            if len(delimiters) == 2:
                value = int(float(f'{delimiters[0]}{content[1]}e{delimiters[1]}{content[2]}'))
            elif len(delimiters) == 0:
                value = int(float(source))
            else:
                value = int(float(f'{content[0]}e{delimiters[0]}{content[1]}'))
        elif re.match(r'\A[+-]?[0-9]+\Z', source):
            value = int(source)
        else:
            value = source

        return McnpInteger(value)

    def to_mcnp(self):
        """
        ``to_mcnp`` generates INP from ``McnpInteger`` objects.

        ``to_mcnp`` creates INP source string from ``McnpInteger``
        objects, so it provides an MCNP endpoint.

        Returns:
            INP string for ``McnpInteger`` object.
        """

        return str(self.value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f'<McnpInteger({self.value}) at {id(self)!r}>'

    def __eq__(a, b: McnpInteger | int):
        return a.value == b.value if isinstance(b, McnpInteger) else a.value == b

    def __lt__(a, b: McnpInteger | int):
        return a.value < b.value if isinstance(b, McnpInteger) else a.value < b

    def __le__(a, b: McnpInteger | int):
        return a.value <= b.value if isinstance(b, McnpInteger) else a.value <= b

    def __gt__(a, b: McnpInteger | int):
        return a.value > b.value if isinstance(b, McnpInteger) else a.value > b

    def __ge__(a, b: McnpInteger | int):
        return a.value >= b.value if isinstance(b, McnpInteger) else a.value >= b

    def __ne__(a, b: McnpInteger | int):
        return a.value != b.value if isinstance(b, McnpInteger) else a.value != b

    def __add__(a, b: McnpInteger | float):
        return (
            McnpInteger(a.value + b.value)
            if isinstance(b, McnpInteger)
            else McnpInteger(a.value + b)
        )

    def __sub__(a, b: McnpInteger | float):
        return (
            McnpInteger(a.value - b.value)
            if isinstance(b, McnpInteger)
            else McnpInteger(a.value - b)
        )

    def __mul__(a, b: McnpInteger | float):
        return (
            McnpInteger(a.value * b.value)
            if isinstance(b, McnpInteger)
            else McnpInteger(a.value * b)
        )


class McnpReal:
    """
    ``McnpReal`` represents the INP real/floating-point value.

    Attributes:
        value: Floating-point number or J jump symbol.
    """

    JUMP = 'j'

    def __init__(self, value: float | Literal['j']):
        """
        ``__init__`` initializes ``McnpReal``.

        Parameters:
            value: Floating-point number or J jump symbol.

        Raises:
            MCNPSemanticError: INVALID_MCNP_REAL.
        """

        if value is None:
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_MCNP_REAL, info=str(value)
            )

        if isinstance(value, float) or isinstance(value, int):
            value = float(value)
        elif value == 'j':
            value = 'j'
        else:
            raise errors.MCNPSemanticError(
                errors.MCNPSemanticCodes.INVALID_MCNP_REAL, info=str(value)
            )

        self.value: Final[float | Literal['j']] = value

    @staticmethod
    def from_mcnp(source: str):
        """
        ``from_mcnp`` generates ``McnpReal`` objects from INP.

        ``from_mcnp`` constructs instances of ``McnpReal`` from INP
        source strings, so it operates as a class constructor method
        and INP parser helper function.

        Parameters:
            source: INP for value.

        Returns:
            ``McnpReal`` object.
        """

        source = _parser.Preprocessor.process_inp(source)

        if re.match(
            r'\A[+-]?(([0-9]+)|([0-9]+[.][0-9]*)|([.][0-9]+))([Ee]([+-][0-9]+))?\Z',
            source,
        ):
            value = float(source)
        elif re.match(r'\A[+-]?(([0-9]+)|([0-9]+[.][0-9]*)|([.][0-9]+))([+-][0-9]+)?\Z', source):
            delimiters = re.findall(r'[+-]', source)
            content = re.split(r'[+-]', source)

            if len(delimiters) == 2:
                value = float(f'{delimiters[0]}{content[1]}e{delimiters[1]}{content[2]}')
            else:
                value = float(f'{content[0]}e{delimiters[0]}{content[1]}')
        else:
            value = source

        return McnpReal(value)

    def to_mcnp(self):
        """
        ``to_mcnp`` generates INP from ``McnpReal`` objects.

        ``to_mcnp`` creates INP source string from ``McnpReal``
        objects, so it provides an MCNP endpoint.

        Returns:
            INP string for ``McnpReal`` object.
        """

        return str(self.value)

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return f'<McnpReal({self.value}) at {id(self)!r}>'

    def __eq__(a, b: McnpReal | float):
        return a.value == b.value if isinstance(b, McnpReal) else a.value == b

    def __lt__(a, b: McnpReal | float):
        return a.value < b.value if isinstance(b, McnpReal) else a.value < b

    def __le__(a, b: McnpReal | float):
        return a.value <= b.value if isinstance(b, McnpReal) else a.value <= b

    def __gt__(a, b: McnpReal | float):
        return a.value > b.value if isinstance(b, McnpReal) else a.value > b

    def __ge__(a, b: McnpReal | float):
        return a.value >= b.value if isinstance(b, McnpReal) else a.value >= b

    def __ne__(a, b: McnpReal | float):
        return a.value != b.value if isinstance(b, McnpReal) else a.value != b

    def __add__(a, b: McnpReal | float):
        return McnpReal(a.value + b.value) if isinstance(b, McnpReal) else McnpReal(a.value + b)

    def __sub__(a, b: McnpReal | float):
        return McnpReal(a.value - b.value) if isinstance(b, McnpReal) else McnpReal(a.value - b)

    def __mul__(a, b: McnpReal | float):
        return McnpReal(a.value * b.value) if isinstance(b, McnpReal) else McnpReal(a.value * b)
