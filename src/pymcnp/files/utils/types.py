"""
Contains classes representing basic MCNP value types.
"""

from __future__ import annotations
import re
import enum
from typing import Literal, Final

from . import errors
from . import _parser
from . import _object


class DistributionNumber(_object.PyMcnpObject):
    """
    Represents MCNP distribution numbers.

    ``DistributionNumber`` implements ``_object.PyMcnpObject``.

    Attributes:
        n: number.
    """

    def __init__(self, n: int):
        """
        Initializes ``DistributionNumber``.

        Parameters:
            n: number.

        Raises:
            McnpError: INVALID_DN.
        """

        if n is None or not (1 <= n <= 999):
            raise errors.McnpError(errors.McnpCode.INVALID_DN, str(n))

        self.n: Final[int] = n

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DistributionNumber`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``DistributionNumber``.

        Returns:
            ``DistributionNumber`` object.

        Raises:
            McnpError: UNRECOGNIZED_KEYWORD.
        """

        source = _parser.Preprocessor.process_inp(source)

        match = re.match(r'\A[dD](\d|\d\d|\d\d\d)\Z', source)
        if match is None:
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD, source)

        return DistributionNumber(int(match[1]))

    def to_mcnp(self):
        """
        Generates INP from ``DistributionNumber`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``DistributionNumber``.
        """

        return f'd{self.n}'


class EmbeddedDistributionNumber(_object.PyMcnpObject):
    """
    Represents MCNP embedded distribution numbers.

    ``EmbeddedDistributionNumber`` implements ``_object.PyMcnpObject``.

    Attributes:
        numbers: Tuple of distribution numbers.
    """

    def __init__(self, numbers: tuple[DistributionNumber]):
        """
        Initializes ``EmbeddedDistributionNumber``.

        Parameters:
            numbers: Tuple of distribution numbers.

        Raises:
            McnpError: INVALID_DN.
        """

        if numbers is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DN, str(numbers))

        for number in numbers:
            if number is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DN, str(number))

        self.numbers: Final[tuple[DistributionNumber]] = numbers

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``EmbeddedDistributionNumber`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``EmbeddedDistributionNumber``.

        Returns:
            ``EmbeddedDistributionNumber`` object.

        Raises:
            McnpError: UNRECOGNIZED_KEYWORD.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = re.split(r'>', source)

        numbers = []
        for token in tokens:
            numbers.append(DistributionNumber.from_mcnp(token))

        return EmbeddedDistributionNumber(tuple(numbers))

    def to_mcnp(self):
        """
        Generates INP from ``EmbeddedDistributionNumber`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``EmbeddedDistributionNumber``.
        """

        return '>'.join(number.to_mcnp() for number in self.numbers)


class Zaid(_object.PyMcnpObject):
    """
    Represents nuclide information numbers.

    ``Zaid`` implements ``_object.PyMcnpObject``.

    Attributes:
        z: Atomic number.
        a: Mass number.
        abx: Cross-section evaluation & class information.
    """

    def __init__(self, z: int, a: int, abx: str = None):
        """
        Initializes ``Zaid``.

        Parameters:
            z: Atomic number.
            a: Mass number.
            abx: Cross-section evaluation & class information.
        """

        if z is None or not (000 <= z <= 999):
            raise errors.McnpError(errors.McnpCode.INVALID_ZAID_Z, str(z))

        if a is None or not (000 <= a <= 999):
            raise errors.McnpError(errors.McnpCode.INVALID_ZAID_A, str(a))

        # if abx is None:
        #    raise errors.McnpError(errors.McnpCode.INVALID_ZAID_ABX, info = str(abx))

        self.z: Final[int] = z
        self.a: Final[int] = a
        self.abx: Final[str] = abx

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Zaid`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Zaid``.

        Returns:
            ``Zaid`` object.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            source.split('.'),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        zzzaaa = tokens.popl()
        if len(zzzaaa) < 4:
            raise errors.McnpError(errors.McnpCode.INVALID_ZAID_Z, source)

        try:
            a = int(zzzaaa[-3:])
        except ValueError:
            raise errors.McnpError(errors.McnpCode.INVALID_ZAID_A, source)

        try:
            z = int(zzzaaa[:-3])
        except ValueError:
            raise errors.McnpError(errors.McnpCode.INVALID_ZAID_Z, source)

        abx = None
        if tokens:
            abx = tokens.popl()

        if tokens:
            raise errors.McnpError(errors.McnpCode.UNEXPECTED_TOKEN, source)

        return Zaid(z, a, abx)

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Zaid`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Zaid``.
        """

        return (
            f'{self.z:03}{self.a:03}.{self.abx}'
            if self.abx is not None
            else f'{self.z:03}{self.a:03}'
        )


class Particle(_object.PyMcnpObject, enum.StrEnum):
    """
    Represents particle designators.

    ``Particle`` implements ``_object.PyMcnpObject`` and ``enum.StrEnum``.
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
        Generates ``Particle`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Particle``.

        Returns:
            ``Particle`` object.
        """

        return Particle(source)

    def to_mcnp(self):
        """
        Generates INP from ``Particle`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Particle``.
        """

        return self.value


class Designator(_object.PyMcnpObject):
    """
    Represents MCNP particle designators.

    ``Designator`` implements ``_object.PyMcnpObject``.

    Attributes:
        particles: Tuple of particles.
    """

    def __init__(self, particles: tuple[Particle]):
        """
        Initializes ``Designator``.

        Parameters:
            particles: Tuple of particles.

        Raises:
            McnpError: INVALID_TYPES_DESIGNATOR.
        """

        if particles is None:
            raise errors.McnpError(errors.McnpCode.INVALID_TYPES_DESIGNATOR, str(particles))

        for particle in particles:
            if particle is None:
                raise errors.McnpError(
                    errors.McnpCode.INVALID_TYPES_DESIGNATOR,
                    str(particles),
                )

        self.particles: Final[tuple[Particle]] = particles

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Designator`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Designator``.

        Returns:
            ``Designator`` object.
        """

        try:
            particles = tuple([Particle(token) for token in source.split(',')])
        except ValueError:
            raise errors.McnpError(errors.McnpCode.INVALID_TYPES_DESIGNATOR, source)

        return Designator(particles)

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Designator`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Designator``.
        """

        return ','.join(Particle(particle) for particle in self.particles)


class McnpInteger(_object.PyMcnpObject):
    """
    Represents the INP integer value.

    ``McnpInteger`` implements ``_object.PyMcnpObject``.

    Attributes:
        value: Integer or J jump symbol.
    """

    def __init__(self, value: int | Literal['j']):
        """
        Initializes ``McnpInteger``.

        Parameters:
            value: Integer or J jump symbol.

        Raises:
            McnpError: INVALID_TYPES_INTEGER.
        """

        if value is None:
            raise errors.McnpError(errors.McnpCode.INVALID_TYPES_INTEGER, str(value))

        if isinstance(value, int):
            value = value
        elif value == 'j':
            value = 'j'
        else:
            raise errors.McnpError(errors.McnpCode.INVALID_TYPES_INTEGER, str(value))

        self.value: Final[int | Literal['j']] = value

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``McnpInteger`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP.

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
        Generates INP from ``McnpInteger`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``McnpInteger``.
        """

        return str(self.value)

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

    def __int__(self) -> int:
        return int(self.value)


class McnpReal(_object.PyMcnpObject):
    """
    Represents the INP real/floating-point value.

    ``McnpReal`` implements ``_object.PyMcnpObject``.

    Attributes:
        value: Floating-point number or J jump symbol.
    """

    JUMP = 'j'

    def __init__(self, value: float | Literal['j']):
        """
        Initializes ``McnpReal``.

        Parameters:
            value: Floating-point number or J jump symbol.

        Raises:
            McnpError: INVALID_TYPES_REAL.
        """

        if value is None:
            raise errors.McnpError(errors.McnpCode.INVALID_TYPES_REAL, str(value))

        if isinstance(value, float) or isinstance(value, int):
            value = float(value)
        elif value == 'j':
            value = 'j'
        else:
            raise errors.McnpError(errors.McnpCode.INVALID_TYPES_REAL, str(value))

        self.value: Final[float | Literal['j']] = value

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``McnpReal`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``McnpReal``.

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
        Generates INP from ``McnpReal`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``McnpReal``.
        """

        return str(self.value)

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

    def __float__(self):
        return float(self.value)
