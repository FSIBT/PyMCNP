"""
Contains the ``Embee`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data import DataMnemonic
from ..data import DataOption
from ..data import DataKeyword
from ...utils import types, errors, _parser


class EmbeeKeyword(DataKeyword):
    """
    Represents INP embee data card option keywords.

    ``EmbeeKeyword`` implements ``DataKeyword``.
    """

    EMBED = 'embed'
    ENERGY = 'energy'
    TIME = 'time'
    ATOM = 'atom'
    FACTOR = 'factor'
    MAT = 'mat'
    MTYPE = 'mtype'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``EmbeeKeyword`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``EmbeeKeyword``.

        Returns:
            ``EmbeeKeyword`` object.

        Raises:
            McnpError: INVALID_DATUM_KEYWORD.
        """

        source = _parser.Preprocessor.process_inp(source)

        try:
            return EmbeeKeyword
        except ValueError:
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD)


class Embed(DataOption):
    """
    Represents INP embed data card embed options.

    ``Embed`` implements ``DataOption``.

    Attributes:
        number: Embedded mesh universe number.
    """

    def __init__(self, number: types.McnpInteger):
        """
        Initializes ``Embee``.

        Parameters:
            number: Embedded mesh universe number.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if number is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[EmbeeKeyword] = EmbeeKeyword.EMBED
        self.value: Final[types.McnpInteger] = number
        self.number: Final[types.McnpInteger] = number

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Embed`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Embed``.

        Returns:
            ``Embed`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'embed':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpInteger.from_mcnp(tokens.popl())

        return Embed(value)


class Energy(DataOption):
    """
    Represents INP energy data card energy options.

    ``Energy`` implements ``DataOption``.

    Attributes:
        factor: Multiplicative conversion factor for energy-related output.
    """

    def __init__(self, factor: types.McnpReal):
        """
        Initializes ``Embee``.

        Parameters:
            factor: Multiplicative conversion factor for energy-related output.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if factor is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[EmbeeKeyword] = EmbeeKeyword.ENERGY
        self.value: Final[types.McnpReal] = factor
        self.factor: Final[types.McnpReal] = factor

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Energy`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Energy``.

        Returns:
            ``Energy`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'energy':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Energy(value)


class Time(DataOption):
    """
    Represents INP time data card time options.

    ``Time`` implements ``DataOption``.

    Attributes:
        factor: Multiplicative conversion factor for time-related output.
    """

    def __init__(self, factor: types.McnpReal):
        """
        Initializes ``Embee``.

        Parameters:
            factor: Multiplicative conversion factor for time-related output.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if factor is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[EmbeeKeyword] = EmbeeKeyword.TIME
        self.value: Final[types.McnpReal] = factor
        self.factor: Final[types.McnpReal] = factor

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Time`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Time``.

        Returns:
            ``Time`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'time':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Time(value)


class Atom(DataOption):
    """
    Represents INP atom data card atom options.

    ``Atom`` implements ``DataOption``.

    Attributes:
        setting: Flag to multiply by atom density.
    """

    def __init__(self, setting: str):
        """
        Initializes ``Embee``.

        Parameters:
            setting: Flag to multiply by atom density.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if setting is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[EmbeeKeyword] = EmbeeKeyword.ATOM
        self.value: Final[str] = setting
        self.setting: Final[str] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Atom`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Atom``.

        Returns:
            ``Atom`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'atom':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Atom(value)


class Factor(DataOption):
    """
    Represents INP factor data card factor options.

    ``Factor`` implements ``DataOption``.

    Attributes:
        constant: Multiplicative constant.
    """

    def __init__(self, constant: types.McnpReal):
        """
        Initializes ``Embee``.

        Parameters:
            constant: Multiplicative constant.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if constant is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[EmbeeKeyword] = EmbeeKeyword.FACTOR
        self.value: Final[types.McnpReal] = constant
        self.constant: Final[types.McnpReal] = constant

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Factor`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Factor``.

        Returns:
            ``Factor`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'factor':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Factor(value)


class Mat(DataOption):
    """
    Represents INP mat data card mat options.

    ``Mat`` implements ``DataOption``.

    Attributes:
        number: Material number.
    """

    def __init__(self, number: types.McnpInteger):
        """
        Initializes ``Embee``.

        Parameters:
            number: Material number.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if number is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[EmbeeKeyword] = EmbeeKeyword.MAT
        self.value: Final[types.McnpInteger] = number
        self.number: Final[types.McnpInteger] = number

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Mat`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Mat``.

        Returns:
            ``Mat`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'mat':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpInteger.from_mcnp(tokens.popl())

        return Mat(value)


class Mtype(DataOption):
    """
    Represents INP mtype data card mtype options.

    ``Mtype`` implements ``DataOption``.

    Attributes:
        kind: Multiplier type.
    """

    def __init__(self, kind: str):
        """
        Initializes ``Embee``.

        Parameters:
            kind: Multiplier type.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if kind is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[EmbeeKeyword] = EmbeeKeyword.MTYPE
        self.value: Final[str] = kind
        self.kind: Final[str] = kind

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Mtype`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Mtype``.

        Returns:
            ``Mtype`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'mtype':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Mtype(value)


class Embee(Data):
    """
    Represents INP embee data cards.

    ``Embee`` implements ``Data``.

    Attributes:
        suffix: Data card suffix..
        pairs: Dictionary of options.
    """

    def __init__(self, suffix: types.McnpInteger, pairs: dict[DataOption]):
        """
        Initializes ``Embee``.

        Parameters:
            suffix: Data card suffix..
            pairs: Dictionary of options.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if suffix is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(suffix))

        if pairs is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(pairs))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.EMBEE
        self.parameters: Final[tuple[any]] = tuple([suffix] + [pairs])
        self.suffix: Final[types.McnpInteger] = suffix
        self.pairs: Final[dict[DataOption]] = pairs
        self.ident: Final[str] = f'embee{self.suffix}'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Embee`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for embee data cards.

        Returns:
            ``Embee`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN, KEYWORD_DATUM_MNEMONIC.
        """

        source = _parser.Preprocessor.process_inp(source)
        source, comments = _parser.Preprocessor.process_inp_comments(source)
        tokens = _parser.Parser(
            re.split(r' |:|=', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        mnemonic = re.search(r'^[a-zA-Z*]+', tokens.peekl())
        mnemonic = mnemonic[0] if mnemonic else ''
        if mnemonic != 'embee':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        suffix = types.McnpInteger.from_mcnp(tokens.popl()[5:])

        pairs = {}
        keywords = re.findall(r'embed|energy|time|atom|factor|mat|mtype', ' '.join(tokens.deque))
        values = re.split(r'embed|energy|time|atom|factor|mat|mtype', ' '.join(tokens.deque))[1:]
        for keyword, value in zip(keywords, values):
            match keyword:
                case 'embed':
                    pairs['embed'] = Embed.from_mcnp(f'{keyword}={value}')
                case 'energy':
                    pairs['energy'] = Energy.from_mcnp(f'{keyword}={value}')
                case 'time':
                    pairs['time'] = Time.from_mcnp(f'{keyword}={value}')
                case 'atom':
                    pairs['atom'] = Atom.from_mcnp(f'{keyword}={value}')
                case 'factor':
                    pairs['factor'] = Factor.from_mcnp(f'{keyword}={value}')
                case 'mat':
                    pairs['mat'] = Mat.from_mcnp(f'{keyword}={value}')
                case 'mtype':
                    pairs['mtype'] = Mtype.from_mcnp(f'{keyword}={value}')

        data = Embee(suffix, pairs)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Embee`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Embee``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()}{self.suffix.to_mcnp()} {" ".join(entry.to_mcnp() for entry in self.pairs.values())}"
        )
