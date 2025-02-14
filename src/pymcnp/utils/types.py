import re
import enum
import typing

from . import errors
from . import _parser
from . import _object


class _Tuple(tuple, _object.McnpElement_):
    """
    Represents generic MCNP collections.
    """

    def __init__(self, value: tuple):
        if value is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TUPLE_VALUE, value)

        self.value: typing.Final[tuple] = tuple(value)

    def to_mcnp(self):
        return ' '.join(val.to_mcnp() for val in self.value)

    def __getitem__(self, key: any):
        return self.value[key]

    def __bool__(self):
        return bool(self.value)

    def extend(self, val: any):
        return self.__class__((*self.value, val))


class Integer(int, _object.McnpElement_):
    """
    Represents MCNP integers.
    """

    def __init__(self, value: int):
        """
        Initializes ``Integer``.

        Parameters:
                value: Integer value.

        Returns:
                ``Integer``.

        Raises:
                McnpError: SEMANTICS_INTEGER_VALUE.
        """

        if value is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_INTEGER_VALUE, value)

        self.value: typing.Final[int] = value

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Integer`` from MCNP.

        Parameters:
                source: MCNP integer.

        Returns:
                ``Integer``.

        Raises:
                McnpError: SYNTAX_INTEGER.
        """

        source, comments = _parser.preprocess_inp(source)

        try:
            return Integer(int(float(source)))
        except ValueError:
            raise errors.McnpError(errors.McnpCode.SYNTAX_INTEGER, source)

    def to_mcnp(self):
        """
        Generates MCNP from ``Integer``.

        Returns:
                MCNP integer.
        """

        return str(self.value)


class Real(float, _object.McnpElement_):
    """
    Represents MCNP reals.
    """

    def __init__(self, value: float):
        """
        Initializes ``Real``.

        Parameters:
                value: Real value.

        Returns:
                ``Real``.

        Raises:
                McnpError: SEMANTICS_REAL_VALUE.
        """

        if value is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_REAL_VALUE, value)

        self.value: typing.Final[float] = value

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Real`` from MCNP.

        Praameters:
                source: MCNP real.

        Returns:
                ``Real``.

        Raises:
                McnpError: SYNTAX_REAL.
        """

        source, comments = _parser.preprocess_inp(source)

        try:
            return Real(float(source))
        except ValueError:
            raise errors.McnpError(errors.McnpCode.SYNTAX_REAL, source)

    def to_mcnp(self):
        """
        Generates MCNP from ``Real``.

        Returns:
                MCNP real.
        """

        return str(self.value)


class String(str, _object.McnpElement_):
    """
    Represents MCNP strings.
    """

    def __init__(self, value: str):
        """
        Initializes ``String``.

        Parameters:
                value: String value.

        Returns:
                ``String``.

        Raises:
                McnpError: SEMANTICS_STRING_VALUE.
        """

        if value is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_STRING_VALUE, value)

        self.value: typing.Final[str] = value

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``String`` from MCNP.

        Praameters:
                source: MCNP string.

        Returns:
                ``String``.

        Raises:
                McnpError: SYNTAX_STRING.
        """

        source, comments = _parser.preprocess_inp(source)

        return String(source)

    def to_mcnp(self):
        """
        Generates MCNP from ``String``.

        Returns:
                MCNP string.
        """

        return self


class Repeat(_object.McnpElement_):
    """
    Represents MCNP repeats.
    """

    REGEX = re.compile(r'((?:\A)\d+)?r(?:\Z)')

    def __init__(self, n: int = None):
        """
        Initializes ``Repeat``.

        Parameters:
                n: Repetition number.

        Returns:
                ``Repeat``

        Raises
                McnpError: SEMANTICS_REPEAT_N.
        """

        if n is not None and not (n >= 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_REPEAT_N, n)

        self.n: typing.Final[int] = n

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Repeat`` from MCNP.

        Parameters:
                source: MCNP repeats.

        Returns:
                ``Repeat``.

        Raises:
                McnpError: SYNTAX_REPEAT.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Repeat.REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_REPEAT, source)

        n = int(tokens[1])

        return Repeat(n)

    def to_mcnp(self):
        """
        Genereates MCNP repeats from ``Repeat``.

        Returns:
                MCNP repeats.
        """

        return f'{self.n}r'


class Insert(_object.McnpElement_):
    """
    Represents MCNP inserts.
    """

    REGEX = re.compile(r'((?:\A)\d+)?i(?:\Z)')

    def __init__(self, n: int = None):
        """
        Initializes ``Insert``.

        Parameters:
                n: Repetition number.

        Returns:
                ``Insert``

        Raises
                McnpError: SEMANTICS_INSERT_N.
        """

        if n is not None and not (n >= 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_INSERT_N, n)

        self.n: typing.Final[int] = n

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Insert`` from MCNP.

        Parameters:
                source: MCNP inserts.

        Returns:
                ``Insert``.

        Raises:
                McnpError: SYNTAX_INSERT.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Insert.REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_INSERT, source)

        n = int(tokens[1])

        return Insert(n)

    def to_mcnp(self):
        """
        Genereates MCNP inserts from ``Insert``.

        Returns:
                MCNP inserts.
        """

        return f'{self.n}i'


class Multiply(_object.McnpElement_):
    """
    Represents MCNP multiply.
    """

    REGEX = re.compile(r'((?:\A)\d+)m(?:\Z)')

    def __init__(self, x: float):
        """
        Initializes ``Multiply``.

        Parameters:
                x: Multiply number.

        Returns:
                ``Multiply``

        Raises
                McnpError: SEMANTICS_MULTIPLY_X.
        """

        if x is not None and not x:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_MULTIPLY_X, x)

        self.x: typing.Final[float] = x

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Multiply`` from MCNP.

        Parameters:
                source: MCNP multiply.

        Returns:
                ``Multiply``.

        Raises:
                McnpError: SYNTAX_MULTIPLY.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Multiply.REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_MULTIPLY, source)

        x = float(tokens[1])

        return Multiply(x)

    def to_mcnp(self):
        """
        Genereates MCNP multiplies. from ``Multiply``.

        Returns:
                MCNP multiply.
        """

        return f'{self.x}m'


class Jump(_object.McnpElement_):
    """
    Represents MCNP jumps.
    """

    REGEX = re.compile(r'((?:\A)\d+)?j(?:\Z)')

    def __init__(self, n: int = None):
        """
        Initializes ``Jump``.

        Parameters:
                n: Repetition number.

        Returns:
                ``Jump``

        Raises
                McnpError: SEMANTICS_JUMP_N.
        """

        if n is not None and not (n >= 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_JUMP_N, n)

        self.n: typing.Final[int] = n

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Jump`` from MCNP.

        Parameters:
                source: MCNP jump.

        Returns:
                ``Jump``.

        Raises:
                McnpError: SYNTAX_JUMP.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Jump.REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_JUMP, source)

        n = int(tokens[1])

        return Jump(n)

    def to_mcnp(self):
        """
        Genereates MCNP jumps. from ``Jump``.

        Returns:
                MCNP jumps.
        """

        return f'{self.n}j'


class Log(_object.McnpElement_):
    """
    Represents MCNP logs.
    """

    REGEX = re.compile(r'((?:\A)\d+)?(log|ilog)(?:\Z)')

    def __init__(self, n: int = None):
        """
        Initializes ``Log``.

        Parameters:
                n: Repetition number.

        Returns:
                ``Log``

        Raises
                McnpError: SEMANTICS_LOG_N.
        """

        if n is not None and not (n >= 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_LOG_N, n)

        self.n: typing.Final[int] = n

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Log`` from MCNP.

        Parameters:
                source: MCNP log.

        Returns:
                ``Log``.

        Raises:
                McnpError: SYNTAX_LOG.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Log.REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_LOG, source)

        n = int(tokens[1])

        return Jump(n)

    def to_mcnp(self):
        """
        Genereates MCNP logs. from ``Logs``.

        Returns:
                MCNP logs.
        """

        return f'{self.n}j'


class DistributionNumber(_object.McnpElement_):
    """
    Represents MCNP distribution numbers.

    Attributes:
            n: Distribution identifier.
    """

    def __init__(self, n: int):
        """
        Initializes ``DistributionNumber``.

        Parameters:
                n: Distribution identifier.

        Returns:
                ``DistributionNumber``.

        Raises:
                McnpError: SEMANTICS_DISTRIBUTIONNUMBER_N.
        """

        if n is None or not (1 <= n <= 999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DISTRIBUTIONNUMBER_N, n)

        self.n: typing.Final[int] = n

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DistributionNumber`` from MCNP.

        Parameters:
                source: MCNP for ``DistributionNumber``.

        Returns:
                ``DistributionNumber``.

        Raises:
                McnpError: SYNTAX_DISTRIBUTIONNUMBER.
        """

        source = _parser.Preprocessor.process_inp(source)
        match = re.match(r'\A[dD](\d|\d\d|\d\d\d)\Z', source)

        if match is None:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DISTRIBUTIONNUMBER, source)

        return DistributionNumber(int(match[1]))

    def to_mcnp(self):
        """
        Generates MCNP from ``DistributionNumber`` objects.

        ``to_mcnp`` translates from PyMCNP to MCNP.

        Returns:
                MCNP for ``DistributionNumber``.
        """

        return f'd{self.n}'


class EmbeddedDistributionNumber(_object.McnpElement_):
    """
    Represents MCNP embedded distribution numbers.

    Attributes:
            numbers: Tuple of distribution numbers.
    """

    def __init__(self, numbers: tuple[DistributionNumber]):
        """
        Initializes ``EmbeddedDistributionNumber``.

        Parameters:
                numbers: Distribution numbers.

        Raises:
                McnpError: SEMANTICS_EMBEDDEDDISTRIBUTIONNUMBER_NUMBERS.
        """

        if numbers is None or None in numbers:
            raise errors.McnpError(
                errors.McnpCode.SEMANTICS_EMBEDDEDDISTRIBUTIONNUMBER_NUMBERS, numbers
            )

        self.numbers: typing.Final[tuple[DistributionNumber]] = numbers

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``EmbeddedDistributionNumber`` objects from MCNP.

        Parameters:
                source: MCNP for ``EmbeddedDistributionNumber``.

        Returns:
                ``EmbeddedDistributionNumber`` object.

        Raises:
                McnpError: SYNTAX_EMBEDDEDDISTRIBUTIONNUMBER.
        """

        source, comments = _parser.preprocess_inp(source)

        try:
            return EmbeddedDistributionNumber(
                DistributionNumber.from_mcnp(token) for token in source.split('>')
            )
        except errors.McnpError:
            raise errors.McnpError(errors.McnpCode.SYNTAX_EMBEDDEDDISTRIBUTIONNUMBER, source)

    def to_mcnp(self):
        """
        Generates MCNP from ``EmbeddedDistributionNumber`` objects.

        Returns:
                MCNP for ``EmbeddedDistributionNumber``.
        """

        return '>'.join(number.to_mcnp() for number in self.numbers)


class Zaid(_object.McnpElement_):
    """
    Represents MCNP nuclide information numbers.

    Attributes:
            z: Atomic number.
            a: Mass number.
            abx: Cross-section evaluation & class information.
    """

    _REGEX = re.compile(r'(?:\A)(\d{1,3})(\d\d\d)((?:[.])\S+)?(?:\Z)')

    def __init__(self, z: int, a: int, abx: str = None):
        """
        Initializes ``Zaid``.

        Parameters:
                z: ZAID atomic number.
                a: ZAID mass number.
                abx: ZAID cross-section evaluation & class information.

        Returns:
                ``Zaid``.

        Raises:
                McnpError: SEMANTICS_ZAID_Z.
                McnpError: SEMANTICS_ZAID_A.
                McnpError: SEMANTICS_ZAID_ABX.
        """

        if z is None or not (000 <= z <= 999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_ZAID_Z, z)

        if a is None or not (000 <= a <= 999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_ZAID_A, a)

        self.z: typing.Final[int] = z
        self.a: typing.Final[int] = a
        self.abx: typing.Final[str] = abx

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Zaid`` objects from MCNP.

        Parameters:
                source: MCNP for ``Zaid``.

        Returns:
                ``Zaid`` object.

        Raises:
                McnpError: SYNTAX_ZAID.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Zaid._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_ZAID, source)

        return Zaid(int(tokens[1]), int(tokens[2]), tokens[3])

    def to_mcnp(self) -> str:
        """
        Generates MCNP from ``Zaid``.

        Returns:
                MCNP Zaid.
        """

        if self.abx:
            return f'{self.z:03}{self.a:03}.{self.abx}'
        else:
            return f'{self.z:03}{self.a:03}'


class Particle(_object.McnpElement_, enum.StrEnum):
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
                McnpError: SYNTAX_PARTICLE.
        """

        source, comments = _parser.preprocess_inp(source)

        try:
            return Particle(source)
        except ValueError:
            raise errors.McnpError(errors.McnpCode.SYNTAX_PARTICLE, source)

    def to_mcnp(self):
        """
        Generates MCNP from ``Particle``.

        Returns:
                MCNP particle.
        """

        return str(self.value)


class Designator(_object.McnpElement_):
    """
    Represents MCNP particle designators.

    Attributes:
            particles: Designator particles.
    """

    def __init__(self, particles: tuple[Particle]):
        """
        Initializes ``Designator``.

        Parameters:
                particles: Tuple of particles.

        Returns:
                ``Designator``.

        Raises:
                McnpError: SEMANTICS_DESIGNATOR_PARTICLES.
        """

        if particles is None or None in particles:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DESIGNATOR_PARTICLES, particles)

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
                McnpError: SYNTAX_DESIGNATOR.
        """

        source, comments = _parser.preprocess_inp(source)

        try:
            return Designator(tuple(Particle.from_mcnp(token) for token in source.split(',')))
        except Exception:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DESIGNATOR, source)

    def to_mcnp(self) -> str:
        """
        Generates MCNP from ``Designator``.

        Returns:
                MCNP designator.
        """

        return ','.join(particle.to_mcnp() for particle in self.particles)
