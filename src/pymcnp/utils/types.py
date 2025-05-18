import re
import typing
import decimal
import dataclasses

from . import errors
from . import _parser
from . import _object


class Tuple(tuple, _object.McnpNonterminal):
    """
    Represents generic MCNP collections.

    Attributes:
        value: Tuple value.
    """

    def __init__(self, value: tuple):
        """
        Initializes ``Tuple``.

        Parameters:
            value: Tuple value.

        Returns:
            ``Tuple``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if value is None or not (value != tuple()):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, value)

        self.value: typing.Final[tuple[type]] = value

    @classmethod
    def from_mcnp(cls, source: str, type: type):
        """
        Generates ``Tuple`` from MCNP.

        Parameters:
            source: MCNP tuple.

        Returns:
            ``Tuple``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = type._REGEX.finditer(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        return Tuple([type.from_mcnp(token[0]) for token in tokens])

    def to_mcnp(self):
        """
        Generates MCNP from ``Tuple``.

        Returns:
            MCNP for ``Tuple``.
        """

        return ' '.join(val.to_mcnp() if val is not None else '' for val in self.value)


class Integer(int, _object.McnpNonterminal):
    """
    Represents MCNP integers.

    Attributes:
        value: Integer value.
    """

    _REGEX = re.compile(r'[-+0-9.eE]+')

    def __init__(self, value: int):
        """
        Initializes ``Integer``.

        Parameters:
            value: Integer value.

        Returns:
            ``Integer``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if value is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, value)

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
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)

        if '-' in source[1:] and 'e' not in source:
            source = source[0] + 'e-'.join(source[1:].split('-'))
        if '+' in source[1:] and 'e' not in source:
            source = source[0] + 'e+'.join(source[1:].split('+'))

        try:
            return Integer(int(float(source)))
        except ValueError:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

    def to_mcnp(self):
        """
        Generates MCNP from ``Integer``.

        Returns:
            MCNP integer.
        """

        return str(self.value)


class Real(float, _object.McnpNonterminal):
    """
    Represents MCNP reals.

    Attributes:
        value: Real value.
    """

    _REGEX = re.compile(r'[-+0-9.eE]+')

    def __init__(self, value: float | decimal.Decimal):
        """
        Initializes ``Real``.

        Parameters:
            value: Real value.

        Returns:
            ``Real``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if value is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, value)

        self.value: typing.Final[float | decimal.Decimal] = value

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Real`` from MCNP.

        Praameters:
            source: MCNP real.

        Returns:
            ``Real``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)

        if '-' in source[1:] and 'e' not in source:
            source = source[0] + 'e-'.join(source[1:].split('-'))
        if '+' in source[1:] and 'e' not in source:
            source = source[0] + 'e+'.join(source[1:].split('+'))

        try:
            return Real(decimal.Decimal(source))
        except ValueError:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

    def to_mcnp(self):
        """
        Generates MCNP from ``Real``.

        Returns:
            MCNP real.
        """

        return str(self.value)


class String(str, _object.McnpNonterminal):
    """
    Represents MCNP strings.

    Attributes:
        value: String value.
    """

    _REGEX = re.compile(r'\S+')

    def __init__(self, value: str):
        """
        Initializes ``String``.

        Parameters:
            value: String value.

        Returns:
            ``String``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if value is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, value)

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
            McnpError: SYNTAX_TYPE.
        """

        return String(source)

    def to_mcnp(self):
        """
        Generates MCNP from ``String``.

        Returns:
            MCNP string.
        """

        return self


class Repeat(_object.McnpNonterminal):
    """
    Represents MCNP repeats.

    Attributes:
        n: Repetition number.
    """

    _REGEX = re.compile(r'(\d+)?r')

    def __init__(self, n: int = None):
        """
        Initializes ``Repeat``.

        Parameters:
            n: Repetition number.

        Returns:
            ``Repeat``

        Raises
            McnpError: SEMANTICS_TYPE.
        """

        if n is not None and not (n >= 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, n)

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
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Repeat._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        n = int(tokens[1])

        return Repeat(n)

    def to_mcnp(self):
        """
        Genereates MCNP repeats from ``Repeat``.

        Returns:
            MCNP repeats.
        """

        return f'{self.n}r'


class Insert(_object.McnpNonterminal):
    """
    Represents MCNP inserts.

    Attributes:
        n: Repetition number.
    """

    _REGEX = re.compile(r'(\d+)?i')

    def __init__(self, n: int = None):
        """
        Initializes ``Insert``.

        Parameters:
            n: Repetition number.

        Returns:
            ``Insert``

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if n is not None and not (n >= 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, n)

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
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Insert._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        n = int(tokens[1])

        return Insert(n)

    def to_mcnp(self):
        """
        Genereates MCNP inserts from ``Insert``.

        Returns:
            MCNP inserts.
        """

        return f'{self.n}i'


class Multiply(_object.McnpNonterminal):
    """
    Represents MCNP multiply.

    Attributes:
        x: Multiply number.
    """

    _REGEX = re.compile(r'(\d+)m')

    def __init__(self, x: float):
        """
        Initializes ``Multiply``.

        Parameters:
            x: Multiply number.

        Returns:
            ``Multiply``

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if x is not None and not x:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, x)

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
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Multiply._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        x = float(tokens[1])

        return Multiply(x)

    def to_mcnp(self):
        """
        Genereates MCNP multiplies. from ``Multiply``.

        Returns:
            MCNP multiply.
        """

        return f'{self.x}m'


class Jump(_object.McnpNonterminal):
    """
    Represents MCNP jumps.

    Attributes:
        n: Repetition number.
    """

    _REGEX = re.compile(r'(\d+)?j')

    def __init__(self, n: int = None):
        """
        Initializes ``Jump``.

        Parameters:
            n: Repetition number.

        Returns:
            ``Jump``

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if n is not None and not (n >= 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, n)

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
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Jump._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        n = int(tokens[1]) if tokens[1] else None

        return Jump(n)

    def to_mcnp(self):
        """
        Genereates MCNP from ``Jump``.

        Returns:
            MCNP jumps.
        """

        return f'{self.n}j'


class Log(_object.McnpNonterminal):
    """
    Represents MCNP logs.

    Attributes:
        n: Repetition number.
    """

    _REGEX = re.compile(r'(\d+)?(log|ilog)')

    def __init__(self, n: int = None):
        """
        Initializes ``Log``.

        Parameters:
            n: Repetition number.

        Returns:
            ``Log``

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if n is not None and not (n >= 0):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, n)

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
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Log._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        n = int(tokens[1])

        return Jump(n)

    def to_mcnp(self):
        """
        Genereates MCNP logs. from ``Logs``.

        Returns:
            MCNP logs.
        """

        return f'{self.n}j'


class DistributionNumber(_object.McnpNonterminal):
    """
    Represents MCNP distribution numbers.

    Attributes:
        n: Distribution identifier.
    """

    _REGEX = re.compile(r'[dD]\d+')

    def __init__(self, n: int):
        """
        Initializes ``DistributionNumber``.

        Parameters:
            n: Distribution identifier.

        Returns:
            ``DistributionNumber``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if n is None or not (1 <= n <= 999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, n)

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
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        match = re.match(r'\A[dD](\d|\d\d|\d\d\d)\Z', source)

        if match is None:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        return DistributionNumber(int(match[1]))

    def to_mcnp(self):
        """
        Generates MCNP from ``DistributionNumber``.

        Returns:
            MCNP for ``DistributionNumber``.
        """

        return f'd{self.n}'


class EmbeddedDistributionNumber(_object.McnpNonterminal):
    """
    Represents MCNP embedded distribution numbers.

    Attributes:
        numbers: Distribution numbers.
    """

    _REGEX = re.compile(r'[dD0-1<]+')

    def __init__(self, numbers: tuple[DistributionNumber]):
        """
        Initializes ``EmbeddedDistributionNumber``.

        Parameters:
            numbers: Distribution numbers.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if numbers is None or None in numbers:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, numbers)

        self.numbers: typing.Final[tuple[DistributionNumber]] = numbers

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``EmbeddedDistributionNumber`` from MCNP.

        Parameters:
            source: MCNP for ``EmbeddedDistributionNumber``.

        Returns:
            ``EmbeddedDistributionNumber`` object.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)

        try:
            return EmbeddedDistributionNumber(
                DistributionNumber.from_mcnp(token) for token in source.split('>')
            )
        except errors.McnpError:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

    def to_mcnp(self):
        """
        Generates MCNP from ``EmbeddedDistributionNumber``.

        Returns:
            MCNP for ``EmbeddedDistributionNumber``.
        """

        return '>'.join(number.to_mcnp() for number in self.numbers)


class Zaid(_object.McnpNonterminal):
    """
    Represents MCNP nuclide information numbers.

    Attributes:
        z: Atomic number.
        a: Mass number.
        abx: Cross-section evaluation & class information.
    """

    _REGEX = re.compile(r'(?:\A)(\d{1,3})(\d\d\d)((?:[.])\S+)?')

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
            McnpError: SEMANTICS_TYPE.
            McnpError: SEMANTICS_TYPE.
            McnpError: SEMANTICS_TYPE.
        """

        if z is None or not (000 <= z <= 999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, z)

        if a is None or not (000 <= a <= 999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, a)

        self.z: typing.Final[int] = z
        self.a: typing.Final[int] = a
        self.abx: typing.Final[str] = abx

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Zaid`` from MCNP.

        Parameters:
            source: MCNP for ``Zaid``.

        Returns:
            ``Zaid`` object.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Zaid._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

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
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)

        try:
            return Particle(source)
        except Exception:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

    def to_mcnp(self):
        """
        Generates MCNP from ``Particle``.

        Returns:
            MCNP particle.
        """

        return str(self.value)


class Designator(_object.McnpNonterminal):
    """
    Represents MCNP particle designators.

    Attributes:
        particles: Designator particles.
    """

    _REGEX = re.compile(
        r'[nqpef|!u<v>hglb+_-~xcywo@/*zk?%^dtsa#]((?:,)[nqpef|!u<v>hglb+_-~xcywo@/*zk?%^dtsa#])*'
    )

    def __init__(self, particles: tuple[Particle]):
        """
        Initializes ``Designator``.

        Parameters:
            particles: Tuple of particles.

        Returns:
            ``Designator``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if particles is None or None in particles:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, particles)

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
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)

        try:
            return Designator(tuple(Particle.from_mcnp(token) for token in source.split(',')))
        except ValueError:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

    def to_mcnp(self) -> str:
        """
        Generates MCNP from ``Designator``.

        Returns:
            MCNP designator.
        """

        return ','.join(particle.to_mcnp() for particle in self.particles)


class Geometry(_object.McnpNonterminal):
    """
    Represents MCNP geometries.

    Attributes:
        infix: Geometry infix formula.
    """

    _REGEX = re.compile(r'((?:).+)')

    def __init__(self, infix: String):
        """
        Initializes ``Geometry``.

        Parameters:
            infix: Geometry infix formula.

        Returns:
            ``Geometry``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        temp = re.sub(r' 0+', '', infix)
        temp = re.sub(r' +', ' ', temp)
        temp = re.sub(r'\+', '', temp)
        temp = re.sub(r' ?: ?', '+', temp)
        temp = re.sub(r' ', '*', temp)
        temp = re.sub(r'#', '-', temp)

        try:
            eval(temp)
        except SyntaxError:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, infix)

        self.infix: typing.typing.Final[String] = infix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Geometry`` from INP.

        Parameters:
            INP for ``Geometry``.

        Returns:
            ``Geometry``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Geometry._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        infix = String.from_mcnp(tokens[1])

        return Geometry(infix)

    def to_mcnp(self):
        """
        Generates INP from ``Geometry``.

        Returns:
            INP for ``Geometry``.
        """

        return self.infix


@dataclasses.dataclass
class GeometryBuilder:
    """
    Builds ``Geometry``.

    Attributes:
        infix: Geometry infix formula.
    """

    infix: str

    def __and__(a, b):
        """
        Unites ``GeometryBuilder``.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            ``GeometryBuilder`` union.
        """

        return GeometryBuilder(infix=f'({a.infix}):({b.infix})')

    def __or__(a, b):
        """
        Intersects ``GeometryBuilder``.

        Parameters:
            a: Operand #1.
            b: Operand #2.

        Returns:
            ``GeometryBuilder`` intersection.
        """

        return GeometryBuilder(infix=f'({a.infix}) ({b.infix})')

    def __neg__(self):
        """
        Negatives ``GeometryBuilder``.

        Returns:
            ``GeometryBuilder`` negative.
        """

        return GeometryBuilder(infix=f'-({self.infix})')

    def __pos__(self):
        """
        Positives ``GeometryBuilder``.

        Returns:
            ``GeometryBuilder`` positive.
        """

        return GeometryBuilder(infix=f'+({self.infix})')

    def __invert__(self):
        """
        Inverts ``GeometryBuilder``.

        Returns:
            ``GeometryBuilder`` complement.
        """

        return GeometryBuilder(infix=f'#({self.infix})')

    def build(self):
        """
        Builds ``GeometryBuilder`` into ``Geometry``.

        Returns:
            ``Geometry`` for ``GeometryBuilder``.
        """

        return Geometry(infix=String(self.infix))


class Substance(_object.McnpNonterminal):
    """
    Represents MCNP substances.

    Attributes:
        zaid: Zaid alias for nuclide.
        weight_ratio: Atomic weight ratios.
    """

    _REGEX = re.compile(r'(\S+) (\S+)')

    def __init__(self, zaid: Zaid, weight_ratio: Real):
        """
        Initializes ``Substance``.

        Parameters:
            zaid: Zaid alias for nuclide.
            weight_ratio: Atomic weight ratios.

        Returns:
            ``Substance``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if zaid is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, zaid)
        if weight_ratio is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, weight_ratio)

        self.zaid: typing.Final[Zaid] = zaid
        self.weight_ratio: typing.Final[Real] = weight_ratio

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Substance`` from MCNP.

        Parameters:
            MCNP for ``Substance``.

        Returns:
            ``Substance``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Substance._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE)

        zaid = Zaid.from_mcnp(tokens[1])
        weight_ratio = Real.from_mcnp(tokens[2])

        return Substance(zaid, weight_ratio)

    def to_mcnp(self):
        """
        Generates INP from ``Substance``.

        Returns:
            INP for ``Substance``.
        """

        return f'{self.zaid} {self.weight_ratio}'


class Bias(_object.McnpNonterminal):
    """
    Represents generic MCNP biases.

    Attributes:
        weight: Weight for bias.
        energy: Energy boundary for bias.
    """

    _REGEX = re.compile(r'(\S+) (\S+)')

    def __init__(self, weight: Real, energy: Real):
        """
        Initializes ``Bias``.

        Parameters:
            weight: Weight for bias.
            energy: Energy boundary for bias.

        Returns:
            ``Bias``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if weight is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, weight)
        if energy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, energy)

        self.weight: typing.Final[Real] = weight
        self.energy: typing.Final[Real] = energy

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Bias`` from MCNP.

        Parameters:
            MCNP for ``Bias``.

        Returns:
            ``Bias``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Bias._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE)

        weight = Real.from_mcnp(tokens[1])
        energy = Real.from_mcnp(tokens[2])

        return Bias(weight, energy)

    def to_mcnp(self):
        """
        Generates INP from ``Bias``.

        Returns:
            INP for ``Bias``.
        """

        return f'{self.weight} {self.energy}'


class Transformation_0(_object.McnpNonterminal):
    """
    Represents MCNP transformations.

    Attributes:
        o1: Transformation displacement vector x-coordinate.
        o2: Transformation displacement vector y-coordinate.
        o3: Transformation displacement vector z-coordinate.
        xx: Transformation rotation matrix xx-entry.
        xy: Transformation rotation matrix xy-entry.
        xz: Transformation rotation matrix xz-entry.
        yx: Transformation rotation matrix yx-entry.
        yy: Transformation rotation matrix yy-entry.
        yz: Transformation rotation matrix yz-entry.
        zx: Transformation rotation matrix zx-entry.
        zy: Transformation rotation matrix zy-entry.
        zz: Transformation rotation matrix zz-entry.
        m: Transformation coordinate system setting.
    """

    _REGEX = re.compile(
        r'(\S+) (\S+) (\S+) (\S+) (\S+) (\S+) (\S+) (\S+) (\S+) (\S+) (\S+) (\S+)( \S+)?'
    )

    def __init__(
        self,
        o1: Real,
        o2: Real,
        o3: Real,
        xx: Real,
        xy: Real,
        xz: Real,
        yx: Real,
        yy: Real,
        yz: Real,
        zx: Real,
        zy: Real,
        zz: Real,
        m: Real = None,
    ):
        """
        Initializes ``Transformation_0``.

        Parameters:
            o1: Transformation displacement vector x-coordinate.
            o2: Transformation displacement vector y-coordinate.
            o3: Transformation displacement vector z-coordinate.
            xx: Transformation rotation matrix xx-entry.
            xy: Transformation rotation matrix xy-entry.
            xz: Transformation rotation matrix xz-entry.
            yx: Transformation rotation matrix yx-entry.
            yy: Transformation rotation matrix yy-entry.
            yz: Transformation rotation matrix yz-entry.
            zx: Transformation rotation matrix zx-entry.
            zy: Transformation rotation matrix zy-entry.
            zz: Transformation rotation matrix zz-entry.
            m: Transformation coordinate system setting.

        Returns:
            ``Transformation_0``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if o1 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, o1)
        if o2 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, o2)
        if o3 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, o3)
        if xx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, xx)
        if xy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, xy)
        if xz is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, xz)
        if yx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, yx)
        if yy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, yy)
        if yz is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, yz)
        if zx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, zx)
        if zy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, zy)
        if zz is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, zz)
        if m is not None and m not in {-1, 1}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, m)

        self.o1: typing.Final[Real] = o1
        self.o2: typing.Final[Real] = o2
        self.o3: typing.Final[Real] = o3
        self.xx: typing.Final[Real] = xx
        self.xy: typing.Final[Real] = xy
        self.xz: typing.Final[Real] = xz
        self.yx: typing.Final[Real] = yx
        self.yy: typing.Final[Real] = yy
        self.yz: typing.Final[Real] = yz
        self.zx: typing.Final[Real] = zx
        self.zy: typing.Final[Real] = zy
        self.zz: typing.Final[Real] = zz
        self.m: typing.Final[Real] = m

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Transformation_0`` from INP.

        Parameters:
            INP for ``Transformation_0``.

        Returns:
            ``Transformation_0``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Transformation_0._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        o1 = Real.from_mcnp(tokens[1])
        o2 = Real.from_mcnp(tokens[2])
        o3 = Real.from_mcnp(tokens[3])
        xx = Real.from_mcnp(tokens[4])
        xy = Real.from_mcnp(tokens[5])
        xz = Real.from_mcnp(tokens[6])
        yx = Real.from_mcnp(tokens[7])
        yy = Real.from_mcnp(tokens[8])
        yz = Real.from_mcnp(tokens[9])
        zx = Real.from_mcnp(tokens[10])
        zy = Real.from_mcnp(tokens[11])
        zz = Real.from_mcnp(tokens[12])
        m = Real.from_mcnp(tokens[13]) if tokens[13] else None

        return Transformation_0(o1, o2, o3, xx, xy, xz, yx, yy, yz, zx, zy, zz, m)

    def to_mcnp(self):
        """
        Generates INP from ``Transformation_0``.

        Returns:
            INP for ``Transformation_0``.
        """

        return f'{self.o1} {self.o2} {self.o3} {self.xx} {self.xy} {self.xz} {self.yx} {self.yy} {self.yz} {self.zx} {self.zy} {self.zz} {self.m}'


class Transformation_1(_object.McnpNonterminal):
    """
    Represents MCNP transformations.

    Attributes:
        o1: Transformation displacement vector x-coordinate.
        o2: Transformation displacement vector y-coordinate.
        o3: Transformation displacement vector z-coordinate.
        xx: Transformation rotation matrix xx-entry.
        xy: Transformation rotation matrix xy-entry.
        xz: Transformation rotation matrix xz-entry.
        yx: Transformation rotation matrix yx-entry.
        yy: Transformation rotation matrix yy-entry.
        yz: Transformation rotation matrix yz-entry.
        m: Transformation coordinate system setting.
    """

    _REGEX = re.compile(r'(\S+) (\S+) (\S+) (\S+) (\S+) (\S+) (\S+) (\S+) (\S+)( \S+)?')

    def __init__(
        self,
        o1: Real,
        o2: Real,
        o3: Real,
        xx: Real,
        xy: Real,
        xz: Real,
        yx: Real,
        yy: Real,
        yz: Real,
        m: Real = None,
    ):
        """
        Initializes ``Transformation_1``.

        Parameters:
            o1: Transformation displacement vector x-coordinate.
            o2: Transformation displacement vector y-coordinate.
            o3: Transformation displacement vector z-coordinate.
            xx: Transformation rotation matrix xx-entry.
            xy: Transformation rotation matrix xy-entry.
            xz: Transformation rotation matrix xz-entry.
            yx: Transformation rotation matrix yx-entry.
            yy: Transformation rotation matrix yy-entry.
            yz: Transformation rotation matrix yz-entry.
            m: Transformation coordinate system setting.

        Returns:
            ``Transformation_1``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if o1 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, o1)
        if o2 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, o2)
        if o3 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, o3)
        if xx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, xx)
        if xy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, xy)
        if xz is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, xz)
        if yx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, yx)
        if yy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, yy)
        if yz is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, yz)
        if m is not None and m not in {-1, 1}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, m)

        self.o1: typing.Final[Real] = o1
        self.o2: typing.Final[Real] = o2
        self.o3: typing.Final[Real] = o3
        self.xx: typing.Final[Real] = xx
        self.xy: typing.Final[Real] = xy
        self.xz: typing.Final[Real] = xz
        self.yx: typing.Final[Real] = yx
        self.yy: typing.Final[Real] = yy
        self.yz: typing.Final[Real] = yz
        self.m: typing.Final[Real] = m

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Transformation_1`` from INP.

        Parameters:
            INP for ``Transformation_1``.

        Returns:
            ``Transformation_1``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Transformation_1._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        o1 = Real.from_mcnp(tokens[1])
        o2 = Real.from_mcnp(tokens[2])
        o3 = Real.from_mcnp(tokens[3])
        xx = Real.from_mcnp(tokens[4])
        xy = Real.from_mcnp(tokens[5])
        xz = Real.from_mcnp(tokens[6])
        yx = Real.from_mcnp(tokens[7])
        yy = Real.from_mcnp(tokens[8])
        yz = Real.from_mcnp(tokens[9])
        m = Real.from_mcnp(tokens[10]) if tokens[10] else None

        return Transformation_1(o1, o2, o3, xx, xy, xz, yx, yy, yz, m)

    def to_mcnp(self):
        """
        Generates INP from ``Transformation_1``.

        Returns:
            INP for ``Transformation_1``.
        """

        return f'{self.o1} {self.o2} {self.o3} {self.xx} {self.xy} {self.xz} {self.yx} {self.yy} {self.yz} {self.m}'


class Transformation_2(_object.McnpNonterminal):
    """
    Represents MCNP transformations.

    Attributes:
        o1: Transformation displacement vector x-coordinate.
        o2: Transformation displacement vector y-coordinate.
        o3: Transformation displacement vector z-coordinate.
        xx: Transformation rotation matrix xx-entry.
        xy: Transformation rotation matrix xy-entry.
        xz: Transformation rotation matrix xz-entry.
        yx: Transformation rotation matrix yx-entry.
        yy: Transformation rotation matrix yy-entry.
        m: Transformation coordinate system setting.
    """

    _REGEX = re.compile(r'(\S+) (\S+) (\S+) (\S+) (\S+) (\S+) (\S+) (\S+)( \S+)?')

    def __init__(
        self,
        o1: Real,
        o2: Real,
        o3: Real,
        xx: Real,
        xy: Real,
        xz: Real,
        yx: Real,
        yy: Real,
        m: Real = None,
    ):
        """
        Initializes ``Transformation_2``.

        Parameters:
            o1: Transformation displacement vector x-coordinate.
            o2: Transformation displacement vector y-coordinate.
            o3: Transformation displacement vector z-coordinate.
            xx: Transformation rotation matrix xx-entry.
            xy: Transformation rotation matrix xy-entry.
            xz: Transformation rotation matrix xz-entry.
            yx: Transformation rotation matrix yx-entry.
            yy: Transformation rotation matrix yy-entry.
            m: Transformation coordinate system setting.

        Returns:
            ``Transformation_2``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if o1 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, o1)
        if o2 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, o2)
        if o3 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, o3)
        if xx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, xx)
        if xy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, xy)
        if xz is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, xz)
        if yx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, yx)
        if yy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, yy)
        if m is not None and m not in {-1, 1}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, m)

        self.o1: typing.Final[Real] = o1
        self.o2: typing.Final[Real] = o2
        self.o3: typing.Final[Real] = o3
        self.xx: typing.Final[Real] = xx
        self.xy: typing.Final[Real] = xy
        self.xz: typing.Final[Real] = xz
        self.yx: typing.Final[Real] = yx
        self.yy: typing.Final[Real] = yy
        self.m: typing.Final[Real] = m

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Transformation_2`` from INP.

        Parameters:
            INP for ``Transformation_2``.

        Returns:
            ``Transformation_2``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Transformation_2._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        o1 = Real.from_mcnp(tokens[1])
        o2 = Real.from_mcnp(tokens[2])
        o3 = Real.from_mcnp(tokens[3])
        xx = Real.from_mcnp(tokens[4])
        xy = Real.from_mcnp(tokens[5])
        xz = Real.from_mcnp(tokens[6])
        yx = Real.from_mcnp(tokens[7])
        yy = Real.from_mcnp(tokens[8])
        m = Real.from_mcnp(tokens[9]) if tokens[9] else None

        return Transformation_2(o1, o2, o3, xx, xy, xz, yx, yy, m)

    def to_mcnp(self):
        """
        Generates INP from ``Transformation_2``.

        Returns:
            INP for ``Transformation_2``.
        """

        return f'{self.o1} {self.o2} {self.o3} {self.xx} {self.xy} {self.xz} {self.yx} {self.yy} {self.m}'


class Transformation_3(_object.McnpNonterminal):
    """
    Represents MCNP transformations.

    Attributes:
        o1: Transformation displacement vector x-coordinate.
        o2: Transformation displacement vector y-coordinate.
        o3: Transformation displacement vector z-coordinate.
        xx: Transformation rotation matrix xx-entry.
        xy: Transformation rotation matrix xy-entry.
        xz: Transformation rotation matrix xz-entry.
        m: Transformation coordinate system setting.
    """

    _REGEX = re.compile(r'(\S+) (\S+) (\S+) (\S+) (\S+) (\S+)( \S+)?')

    def __init__(
        self,
        o1: Real,
        o2: Real,
        o3: Real,
        xx: Real,
        xy: Real,
        xz: Real,
        m: Real = None,
    ):
        """
        Initializes ``Transformation_3``.

        Parameters:
            o1: Transformation displacement vector x-coordinate.
            o2: Transformation displacement vector y-coordinate.
            o3: Transformation displacement vector z-coordinate.
            xx: Transformation rotation matrix xx-entry.
            xy: Transformation rotation matrix xy-entry.
            xz: Transformation rotation matrix xz-entry.
            m: Transformation coordinate system setting.

        Returns:
            ``Transformation_3``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if o1 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, o1)
        if o2 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, o2)
        if o3 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, o3)
        if xx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, xx)
        if xy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, xy)
        if xz is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, xz)
        if m is not None and m not in {-1, 1}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, m)

        self.o1: typing.Final[Real] = o1
        self.o2: typing.Final[Real] = o2
        self.o3: typing.Final[Real] = o3
        self.xx: typing.Final[Real] = xx
        self.xy: typing.Final[Real] = xy
        self.xz: typing.Final[Real] = xz
        self.m: typing.Final[Real] = m

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Transformation_3`` from INP.

        Parameters:
            INP for ``Transformation_3``.

        Returns:
            ``Transformation_3``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Transformation_3._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        o1 = Real.from_mcnp(tokens[1])
        o2 = Real.from_mcnp(tokens[2])
        o3 = Real.from_mcnp(tokens[3])
        xx = Real.from_mcnp(tokens[4])
        xy = Real.from_mcnp(tokens[5])
        xz = Real.from_mcnp(tokens[6])
        m = Real.from_mcnp(tokens[7]) if tokens[7] else None

        return Transformation_3(o1, o2, o3, xx, xy, xz, m)

    def to_mcnp(self):
        """
        Generates INP from ``Transformation_3``.

        Returns:
            INP for ``Transformation_3``.
        """

        return f'{self.o1} {self.o2} {self.o3} {self.xx} {self.xy} {self.xz} {self.m}'


class Transformation_4(_object.McnpNonterminal):
    """
    Represents MCNP transformations.

    Attributes:
        o1: Transformation displacement vector x-coordinate.
        o2: Transformation displacement vector y-coordinate.
        o3: Transformation displacement vector z-coordinate.
        m: Transformation coordinate system setting.
    """

    _REGEX = re.compile(r'(\S+) (\S+) (\S+)( \S+)?')

    def __init__(
        self,
        o1: Real,
        o2: Real,
        o3: Real,
        m: Real = None,
    ):
        """
        Initializes ``Transformation_4``.

        Parameters:
            o1: Transformation displacement vector x-coordinate.
            o2: Transformation displacement vector y-coordinate.
            o3: Transformation displacement vector z-coordinate.
            m: Transformation coordinate system setting.

        Returns:
            ``Transformation_4``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if o1 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, o1)
        if o2 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, o2)
        if o3 is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, o3)
        if m is not None and m not in {-1, 1}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, m)

        self.o1: typing.Final[Real] = o1
        self.o2: typing.Final[Real] = o2
        self.o3: typing.Final[Real] = o3
        self.m: typing.Final[Real] = m

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Transformation_4`` from INP.

        Parameters:
            INP for ``Transformation_4``.

        Returns:
            ``Transformation_4``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Transformation_4._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        o1 = Real.from_mcnp(tokens[1])
        o2 = Real.from_mcnp(tokens[2])
        o3 = Real.from_mcnp(tokens[3])
        m = Real.from_mcnp(tokens[4]) if tokens[4] else None

        return Transformation_4(o1, o2, o3, m)

    def to_mcnp(self):
        """
        Generates INP from ``Transformation_4``.

        Returns:
            INP for ``Transformation_4``.
        """

        return f'{self.o1} {self.o2} {self.o3} {self.m}'


class Stochastic(_object.McnpNonterminal):
    """
    Represents MCNP stochastic transformation entries.

    Attributes:
        universe: Universe number.
        maximum_x: Maximum x displacement.
        maximum_y: Maximum y displacement.
        maximum_z: Maximum z displacement.
    """

    _REGEX = re.compile(r'(\S+) (\S+) (\S+) (\S+)')

    def __init__(
        self,
        universe: Integer,
        maximum_x: Real,
        maximum_y: Real,
        maximum_z: Real,
    ):
        """
        Initializes ``Stochastic``.

        Parameters:
            universe: Universe number.
            maximum_x: Maximum x displacement.
            maximum_y: Maximum y displacement.
            maximum_z: Maximum z displacement.

        Returns:
            ``Stochastic``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if universe is None or not (0 <= universe <= 99_999_999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, universe)
        if maximum_x is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, maximum_x)
        if maximum_y is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, maximum_y)
        if maximum_z is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, maximum_z)

        self.universe: typing.Final[Integer] = universe
        self.maximum_x: typing.Final[Real] = maximum_x
        self.maximum_y: typing.Final[Real] = maximum_y
        self.maximum_z: typing.Final[Real] = maximum_z

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Stochastic`` from INP.

        Parameters:
            INP for ``Stochastic``.

        Returns:
            ``Stochastic``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Stochastic._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        number = Integer.from_mcnp(tokens[1])
        maximum_x = Real.from_mcnp(tokens[2])
        maximum_y = Real.from_mcnp(tokens[3])
        maximum_z = Real.from_mcnp(tokens[4])

        return Stochastic(number, maximum_x, maximum_y, maximum_z)

    def to_mcnp(self):
        """
        Generates INP from ``Stochastic``.

        Returns:
            INP for ``Stochastic``.
        """

        return f'{self.number} {self.maximum_x} {self.maximum_y} {self.maximum_z}'


class IndependentDependent(_object.McnpNonterminal):
    """
    Represents INP inpependent-dependent entries.

    Attributes:
        independent: Independent source dependent variable.
        dependent: Dependent source dependent variable.
    """

    _REGEX = re.compile(r'(\S+) (\S+)')

    def __init__(self, independent: Real, dependent: Real):
        """
        Initializes ``IndependentDependent``.

        Parameters:
            independent: Independent source dependent variable.
            dependent: Dependent source dependent variable.

        Returns:
            ``IndependentDependent``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if independent is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, independent)
        if dependent is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, dependent)

        self.independent: typing.Final[Real] = independent
        self.dependent: typing.Final[Real] = dependent

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``IndependentDependent`` from INP.

        Parameters:
            INP for ``IndependentDependent``.

        Returns:
            ``IndependentDependent``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = IndependentDependent._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        independent = Real.from_mcnp(tokens[1])
        dependent = Real.from_mcnp(tokens[2])

        return IndependentDependent(independent, dependent)

    def to_mcnp(self):
        """
        Generates INP from ``IndependentDependent``.

        Returns:
            INP for ``IndependentDependent``.
        """

        return f'{self.independent} {self.dependent}'


class Location(_object.McnpNonterminal):
    """
    Represents INP location entries.

    Attributes:
        x: Location x-coordinate.
        y: Location y-coordinate.
        z: Location z-coordinate.
    """

    _REGEX = re.compile(r'(\S+) (\S+) (\S+)')

    def __init__(self, x: Real, y: Real, z: Real):
        """
        Initializes ``Location``.

        Parameters:
            x: Location x-coordinate.
            y: Location y-coordinate.
            z: Location z-coordinate.

        Returns:
            ``Location``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if x is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, x)
        if y is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, y)
        if z is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, z)

        self.x: typing.Final[Real] = x
        self.y: typing.Final[Real] = y
        self.z: typing.Final[Real] = z

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Location`` from INP.

        Parameters:
            INP for ``Location``.

        Returns:
            ``Location``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Location._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        x = Real.from_mcnp(tokens[1])
        y = Real.from_mcnp(tokens[2])
        z = Real.from_mcnp(tokens[3])

        return Location(x, y, z)

    def to_mcnp(self):
        """
        Generates INP from ``Location``.

        Returns:
            INP for ``Location``.
        """

        return f'{self.x} {self.y} {self.z}'


class File(_object.McnpNonterminal):
    """
    Represents INP file entries.

    Attributes:
        unit: Unit number of file to create.
        filename: Name of file to create.
        access: access of file to create.
        form: Format of file to create.
        length: Record length of file to create.
    """

    _REGEX = re.compile(r'(\S+) (\S+) (\S+) (\S+) (\S+)')

    def __init__(
        self,
        unit: Integer,
        filename: String,
        access: String,
        form: String,
        length: Integer,
    ):
        """
        Initializes ``File``.

        Parameters:
            unit: Unit number of file to create.
            filename: Name of file to create.
            access: access of file to create.
            form: Format of file to create.
            length: Record length of file to create.

        Returns:
            ``File``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if unit is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, unit)
        if filename is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, filename)
        if access is None or access not in {'sequential', 'direct'}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, access)
        if form is None or format not in {'formatted', 'unformatted'}:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, form)
        if length is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, length)

        self.unit: typing.Final[Integer] = unit
        self.filename: typing.Final[String] = filename
        self.access: typing.Final[String] = access
        self.form: typing.Final[String] = form
        self.length: typing.Final[Integer] = length

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``File`` from INP.

        Parameters:
            INP for ``File``.

        Returns:
            ``File``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = File._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        unit = Integer.from_mcnp(tokens[1])
        filename = String.from_mcnp(tokens[2])
        access = String.from_mcnp(tokens[3])
        form = String.from_mcnp(tokens[4])
        length = Integer.from_mcnp(tokens[5])

        return File(unit, filename, access, form, length)

    def to_mcnp(self):
        """
        Generates INP from ``File``.

        Returns:
            INP for ``File``.
        """

        return f'{self.unit} {self.filename} {self.access} {self.form} {self.length}'


class Diagnostic(_object.McnpNonterminal):
    """
    Represents INP diagnostic entries.

    Attributes:
        playing_setting: Criterion for playing Russian roulette for DXTRAN.
        printing_setting: Criterion for printing diagnostics for large contributions for DXTRAN.
    """

    _REGEX = re.compile(r'(\S+) (\S+)')

    def __init__(self, playing_setting: Real, printing_setting: Real):
        """
        Initializes ``Diagnostic``.

        Parameters:
            playing_setting: Criterion for playing Russian roulette for DXTRAN.
            printing_setting: Criterion for printing diagnostics for large contributions for DXTRAN.

        Returns:
            ``Diagnostic``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if playing_setting is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, playing_setting)
        if printing_setting is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, printing_setting)

        self.playing_setting: typing.Final[Real] = playing_setting
        self.printing_setting: typing.Final[Real] = printing_setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Diagnostic`` from INP.

        Parameters:
            INP for ``Diagnostic``.

        Returns:
            ``Diagnostic``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Diagnostic._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        playing_setting = Real.from_mcnp(tokens[1])
        printing_setting = Real.from_mcnp(tokens[2])

        return Diagnostic(playing_setting, printing_setting)

    def to_mcnp(self):
        """
        Generates INP from ``Diagnostic``.

        Returns:
            INP for ``Diagnostic``.
        """

        return f'{self.playing_setting} {self.printing_setting}'


class Ring(_object.McnpNonterminal):
    """
    Represents INP ring detector entries.

    Attributes:
        distance: Ring position.
        radius: Ring radius.
        excludion_radius: Ring radius.
    """

    _REGEX = re.compile(r'(\S+) (\S+) (\S+)')

    def __init__(
        self,
        distance: Real,
        radius: Real,
        ro: Real,
    ):
        """
        Initializes ``Ring``.

        Parameters:
            distance: Ring position.
            radius: Ring radius.
            ro: Ring exclusion radius.

        Returns:
            ``Ring``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if distance is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, distance)
        if radius is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, radius)
        if ro is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, ro)

        self.distance: typing.Final[Real] = distance
        self.radius: typing.Final[Real] = radius
        self.ro: typing.Final[Real] = ro

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Ring`` from INP.

        Parameters:
            INP for ``Ring``.

        Returns:
            ``Ring``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Ring._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        distance = Real.from_mcnp(tokens[1])
        radius = Real.from_mcnp(tokens[2])
        ro = Real.from_mcnp(tokens[3])

        return Ring(distance, radius, ro)

    def to_mcnp(self):
        """
        Generates INP from ``Sphere``.

        Returns:
            INP for ``Sphere``.
        """

        return f'{self.distance} {self.radius} {self.ro}'


class Sphere(_object.McnpNonterminal):
    """
    Represents INP sphere detector entries.

    Attributes:
        x: Vector x coordinate.
        y: Vector y coordinate.
        z: Vector z coordinate.
        ro: Sphere exclusion radius.
    """

    _REGEX = re.compile(r'(\S+) (\S+) (\S+) (\S+)')

    def __init__(
        self,
        x: Real,
        y: Real,
        z: Real,
        ro: Integer,
    ):
        """
        Initializes ``Sphere``.

        Parameters:
            x: Vector x coordinate.
            y: Vector y coordinate.
            z: Vector z coordinate.
            ro: Sphere exclusion radius.

        Returns:
            ``Sphere``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if x is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, x)
        if y is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, y)
        if z is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, z)
        if ro is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, ro)

        self.x: typing.Final[Real] = x
        self.y: typing.Final[Real] = y
        self.z: typing.Final[Real] = z
        self.ro: typing.Final[Integer] = ro

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Sphere`` from INP.

        Parameters:
            INP for ``Sphere``.

        Returns:
            ``Sphere``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Sphere._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        x = Real.from_mcnp(tokens[1])
        y = Real.from_mcnp(tokens[2])
        z = Real.from_mcnp(tokens[3])
        ro = Integer.from_mcnp(tokens[4])

        return Sphere(x, y, z, ro)

    def to_mcnp(self):
        """
        Generates INP from ``Sphere``.

        Returns:
            INP for ``Sphere``.
        """

        return f'{self.x} {self.y} {self.z} {self.ro}'


class Shell(_object.McnpNonterminal):
    """
    Represents INP shell detector entries.

    Attributes:
        x: Vector x coordinate.
        y: Vector y coordinate.
        z: Vector z coordinate.
        inner_radius: Inner sphere radius.
        outer_radius: Outer sphere radius.
    """

    _REGEX = re.compile(r'(\S+) (\S+) (\S+) (\S+) (\S+)')

    def __init__(
        self,
        x: Real,
        y: Real,
        z: Real,
        inner_radius: Integer,
        outer_radius: Integer,
    ):
        """
        Initializes ``Shell``.

        Parameters:
            x: Vector x coordinate.
            y: Vector y coordinate.
            z: Vector z coordinate.
            inner_radius: Inner sphere radius.
            outer_radius: Outer sphere radius.

        Returns:
            ``Shell``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if x is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, x)
        if y is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, y)
        if z is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, z)
        if inner_radius is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, inner_radius)
        if outer_radius is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, outer_radius)

        self.x: typing.Final[Real] = x
        self.y: typing.Final[Real] = y
        self.z: typing.Final[Real] = z
        self.inner_radius: typing.Final[Integer] = inner_radius
        self.outer_radius: typing.Final[Integer] = outer_radius

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Shell`` from INP.

        Parameters:
            INP for ``Shell``.

        Returns:
            ``Shell``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Shell._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        x = Real.from_mcnp(tokens[1])
        y = Real.from_mcnp(tokens[2])
        z = Real.from_mcnp(tokens[3])
        inner_radius = Integer.from_mcnp(tokens[4])
        outer_radius = Integer.from_mcnp(tokens[5])

        return Shell(x, y, z, inner_radius, outer_radius)

    def to_mcnp(self):
        """
        Generates INP from ``Shell``.

        Returns:
            INP for ``Shell``.
        """

        return f'{self.x} {self.y} {self.z} {self.inner_radius} {self.outer_radius}'


class Reaction(_object.McnpNonterminal):
    """
    Represents INP reaction entries.

    Attributes:
        mt: MT reaction identifiers.
        pmt: MT reaction frequency control.
    """

    _REGEX = re.compile(r'(\S+) (\S+)')

    def __init__(self, mt: Zaid, pmt: Integer):
        """
        Initializes ``Reaction``.

        Parameters:
            mt: MT reaction identifiers.
            pmt: MT reaction frequency control.

        Returns:
            ``Reaction``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if mt is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, mt)
        if pmt is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, pmt)

        self.mt: typing.Final[Zaid] = mt
        self.pmt: typing.Final[Integer] = pmt

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Reaction`` from INP.

        Parameters:
            INP for ``Reaction``.

        Returns:
            ``Reaction``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Reaction._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        mt = Zaid.from_mcnp(tokens[1])
        pmt = Integer.from_mcnp(tokens[2])

        return Reaction(mt, pmt)

    def to_mcnp(self):
        """
        Generates INP from ``Reaction``.

        Returns:
            INP for ``Reaction``.
        """

        return f'{self.mt} {self.pmt}'


class PtracFilter(_object.McnpNonterminal):
    """
    Represents INP ptrac filters entries.

    Attributes:
        lower: Lower bound for filtering.
        upper: Upper bound for filtering.
        variable: Variable name for PBL derived structure.
    """

    _REGEX = re.compile(r'(\S+),(\S+)(,\S+)?')

    def __init__(self, lower: Real, variable: String, upper: Real = None):
        """
        Initializes ``PtracFilter``.

        Parameters:
            lower: Lower bound for filtering.
            upper: Upper bound for filtering.
            variable: Variable name for PBL derived structure.

        Returns:
            ``PtracFilter``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if lower is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, lower)
        if variable is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, variable)
        if upper is not None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, upper)

        self.lower: typing.Final[Real] = lower
        self.upper: typing.Final[Real] = upper
        self.variable: typing.Final[String] = variable

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``PtracFilter`` from INP.

        Parameters:
            INP for ``PtracFilter``.

        Returns:
            ``PtracFilter``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = PtracFilter._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        lower = Real.from_mcnp(tokens[1])
        variable = String.from_mcnp(tokens[2])
        upper = String.from_mcnp(tokens[3]) if tokens[3] else None

        return PtracFilter(lower, variable, upper)

    def to_mcnp(self):
        """
        Generates INP from ``PtracFilter``.

        Returns:
            INP for ``PtracFilter``.
        """

        return f'{self.lower} {self.upper} {self.variable}'


class PhotonBias(_object.McnpNonterminal):
    """
    Represents INP bias entries.

    Attributes:
        zaid: Bias nuclide identifier.
        ipiki: Bias controls.
        reactions: Bias MT reactions.
    """

    _REGEX = re.compile(r'(\S+) (\S+)((?: \S+ \S+)+)')

    def __init__(self, zaid: Zaid, ipiki: Integer, reactions: tuple[Reaction]):
        """
        Initializes ``PhotonBias``.

        Parameters:
            zaid: Bias nuclide identifier.
            ipiki: Bias controls.
            reactions: Bias MT reactions.

        Returns:
            ``PhotonBias``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if zaid is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, zaid)
        if ipiki is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, ipiki)
        if reactions is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, reactions)

        self.zaid: typing.Final[Zaid] = zaid
        self.ipiki: typing.Final[Integer] = ipiki
        self.reactions: typing.Final[tuple[Reaction]] = reactions

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``PhotonBias`` from INP.

        Parameters:
            INP for ``PhotonBias``.

        Returns:
            ``PhotonBias``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = PhotonBias._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        zaid = Zaid.from_mcnp(tokens[1])
        ipiki = Integer.from_mcnp(tokens[2])
        reactions = Tuple(
            [Reaction.from_mcnp(token[0]) for token in Reaction._REGEX.finditer(tokens[3])]
        )

        return PhotonBias(zaid, ipiki, reactions)

    def to_mcnp(self):
        """
        Generates INP from ``PhotonBias``.

        Returns:
            INP for ``PhotonBias``.
        """

        return f'{self.zaid} {self.ipiki} {self.reactions}'


class Index(_object.McnpNonterminal):
    """
    Represents INP lattice index entries.

    Attributes:
        lower: Lower index.
        upper: Upper index.
    """

    _REGEX = re.compile(r'(\S+):(\S+)')

    def __init__(self, lower: Integer, upper: Integer):
        """
        Initializes ``Index``.

        Parameters:
            lower: Lower index.
            upper: Upper index.

        Returns:
            ``Index``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if lower is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, lower)
        if upper is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, upper)

        self.lower: typing.Final[Integer] = lower
        self.upper: typing.Final[Integer] = upper

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Index`` from INP.

        Parameters:
            INP for ``Index``.

        Returns:
            ``Index``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = Index._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

        lower = Integer.from_mcnp(tokens[1])
        upper = Integer.from_mcnp(tokens[2])

        return Index(lower, upper)

    def to_mcnp(self):
        """
        Generates INP from ``Index``.

        Returns:
            INP for ``Index``.
        """

        return f'{self.lower}:{self.upper}'


class IntegerOrJump(_object.McnpNonterminal):
    """
    Represents MCNP integers or jump.

    Attributes:
        value: Integer value or jump.
    """

    _REGEX = re.compile(r'(?:[-+0-9.eE]+|\d*j|\d*log|\d*ilog|\d*m|\d*i|\d*r)')

    def __init__(self, value: int | Repeat | Insert | Multiply | Jump | Log):
        """
        Initializes ``IntegerOrJump``.

        Parameters:
            value: Integer or jump value.

        Returns:
            ``IntegerOrJump``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if value is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, value)

        self.value: typing.Final[int] = value

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``IntegerOrJump`` from MCNP.

        Parameters:
            source: MCNP integer or jump.

        Returns:
            ``IntegerOrJump``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)

        try:
            return IntegerOrJump(Repeat.from_mcnp(source))
        except errors.McnpError:
            pass

        try:
            return IntegerOrJump(Insert.from_mcnp(source))
        except errors.McnpError:
            pass

        try:
            return IntegerOrJump(Multiply.from_mcnp(source))
        except errors.McnpError:
            pass

        try:
            return IntegerOrJump(Jump.from_mcnp(source))
        except errors.McnpError:
            pass

        try:
            return IntegerOrJump(Log.from_mcnp(source))
        except errors.McnpError:
            pass

        try:
            return IntegerOrJump(Integer.from_mcnp(source).value)
        except errors.McnpError:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

    def to_mcnp(self):
        """
        Generates MCNP from ``IntegerOrJump``.

        Returns:
            MCNP integer.
        """

        return str(self.value)


class RealOrJump(_object.McnpNonterminal):
    """
    Represents MCNP integers or jump.

    Attributes:
        value: Real value or jump.
    """

    _REGEX = re.compile(r'(?:[-+0-9.eE]+|\d*j|\d*log|\d*ilog|\d*m|\d*i|\d*r)')

    def __init__(self, value: int | Repeat | Insert | Multiply | Jump | Log):
        """
        Initializes ``RealOrJump``.

        Parameters:
            value: Real or jump value.

        Returns:
            ``RealOrJump``.

        Raises:
            McnpError: SEMANTICS_TYPE.
        """

        if value is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_TYPE, value)

        self.value: typing.Final[int] = value

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``RealOrJump`` from MCNP.

        Parameters:
            source: MCNP real or jump.

        Returns:
            ``RealOrJump``.

        Raises:
            McnpError: SYNTAX_TYPE.
        """

        source, comments = _parser.preprocess_inp(source)

        try:
            return RealOrJump(Repeat.from_mcnp(source))
        except errors.McnpError:
            pass

        try:
            return RealOrJump(Insert.from_mcnp(source))
        except errors.McnpError:
            pass

        try:
            return RealOrJump(Multiply.from_mcnp(source))
        except errors.McnpError:
            pass

        try:
            return RealOrJump(Jump.from_mcnp(source))
        except errors.McnpError:
            pass

        try:
            return RealOrJump(Log.from_mcnp(source))
        except errors.McnpError:
            pass

        try:
            return RealOrJump(Real.from_mcnp(source).value)
        except errors.McnpError:
            raise errors.McnpError(errors.McnpCode.SYNTAX_TYPE, source)

    def to_mcnp(self):
        """
        Generates MCNP from ``RealOrJump``.

        Returns:
            MCNP real.
        """

        return str(self.value)
