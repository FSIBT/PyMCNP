"""
Contains the ``Kpert`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ..data_option import DataOption
from ..data_keyword import DataKeyword
from ...utils import types
from ...utils import errors
from ...utils import _parser


class KpertKeyword(DataKeyword):
    """
    Represents INP kpert data card option keywords.

    ``KpertKeyword`` implements ``DataKeyword``.
    """

    CELL = 'cell'
    MAT = 'mat'
    RHO = 'rho'
    ISO = 'iso'
    RXN = 'rxn'
    ERG = 'erg'
    LINEAR = 'linear'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``KpertKeyword`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``KpertKeyword``.

        Returns:
            ``KpertKeyword`` object.

        Raises:
            McnpError: INVALID_DATUM_KEYWORD.
        """

        source = _parser.Preprocessor.process_inp(source)

        try:
            return KpertKeyword
        except ValueError:
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD)


class Cell(DataOption):
    """
    Represents INP cell data card cell options.

    ``Cell`` implements ``DataOption``.

    Attributes:
        numbers: List of cells.
    """

    def __init__(self, numbers: tuple[types.McnpInteger]):
        """
        Initializes ``Kpert``.

        Parameters:
            numbers: List of cells.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if numbers is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in numbers:
            if entry is None or not (1 <= entry <= 99_999_999):
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(numbers))

        self.keyword: Final[KpertKeyword] = KpertKeyword.CELL
        self.value: Final[tuple[types.McnpInteger]] = numbers
        self.numbers: Final[tuple[types.McnpInteger]] = numbers

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Cell`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Cell``.

        Returns:
            ``Cell`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'cell':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tuple([types.McnpInteger.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return Cell(value)


class Mat(DataOption):
    """
    Represents INP mat data card mat options.

    ``Mat`` implements ``DataOption``.

    Attributes:
        numbers: List of materials.
    """

    def __init__(self, numbers: tuple[types.McnpInteger]):
        """
        Initializes ``Kpert``.

        Parameters:
            numbers: List of materials.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if numbers is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in numbers:
            if entry is None or not (0 <= entry <= 99_999_999):
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(numbers))

        self.keyword: Final[KpertKeyword] = KpertKeyword.MAT
        self.value: Final[tuple[types.McnpInteger]] = numbers
        self.numbers: Final[tuple[types.McnpInteger]] = numbers

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

        value = tuple([types.McnpInteger.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return Mat(value)


class Rho(DataOption):
    """
    Represents INP rho data card rho options.

    ``Rho`` implements ``DataOption``.

    Attributes:
        densities: List of densities.
    """

    def __init__(self, densities: tuple[types.Zaid]):
        """
        Initializes ``Kpert``.

        Parameters:
            densities: List of densities.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if densities is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in densities:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(densities))

        self.keyword: Final[KpertKeyword] = KpertKeyword.RHO
        self.value: Final[tuple[types.Zaid]] = densities
        self.densities: Final[tuple[types.Zaid]] = densities

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Rho`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Rho``.

        Returns:
            ``Rho`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'rho':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tuple([types.Zaid.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return Rho(value)


class Iso(DataOption):
    """
    Represents INP iso data card iso options.

    ``Iso`` implements ``DataOption``.

    Attributes:
        zaids: List of ZAIDs for pertubation.
    """

    def __init__(self, zaids: tuple[types.McnpReal]):
        """
        Initializes ``Kpert``.

        Parameters:
            zaids: List of ZAIDs for pertubation.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if zaids is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in zaids:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(zaids))

        self.keyword: Final[KpertKeyword] = KpertKeyword.ISO
        self.value: Final[tuple[types.McnpReal]] = zaids
        self.zaids: Final[tuple[types.McnpReal]] = zaids

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Iso`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Iso``.

        Returns:
            ``Iso`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'iso':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tuple([types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return Iso(value)


class Rxn(DataOption):
    """
    Represents INP rxn data card rxn options.

    ``Rxn`` implements ``DataOption``.

    Attributes:
        numbers: List of reaction numbers for pertubation.
    """

    def __init__(self, numbers: tuple[types.McnpInteger]):
        """
        Initializes ``Kpert``.

        Parameters:
            numbers: List of reaction numbers for pertubation.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if numbers is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in numbers:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(numbers))

        self.keyword: Final[KpertKeyword] = KpertKeyword.RXN
        self.value: Final[tuple[types.McnpInteger]] = numbers
        self.numbers: Final[tuple[types.McnpInteger]] = numbers

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Rxn`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Rxn``.

        Returns:
            ``Rxn`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'rxn':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tuple([types.McnpInteger.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return Rxn(value)


class Erg(DataOption):
    """
    Represents INP erg data card erg options.

    ``Erg`` implements ``DataOption``.

    Attributes:
        energies: List of energies.
    """

    def __init__(self, energies: tuple[types.McnpReal]):
        """
        Initializes ``Kpert``.

        Parameters:
            energies: List of energies.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if energies is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in energies:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(energies))

        self.keyword: Final[KpertKeyword] = KpertKeyword.ERG
        self.value: Final[tuple[types.McnpReal]] = energies
        self.energies: Final[tuple[types.McnpReal]] = energies

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Erg`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Erg``.

        Returns:
            ``Erg`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'erg':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tuple([types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return Erg(value)


class Linear(DataOption):
    """
    Represents INP linear data card linear options.

    ``Linear`` implements ``DataOption``.

    Attributes:
        setting: Pertubated fission source on/off.
    """

    def __init__(self, setting: str):
        """
        Initializes ``Kpert``.

        Parameters:
            setting: Pertubated fission source on/off.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if setting is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[KpertKeyword] = KpertKeyword.LINEAR
        self.value: Final[str] = setting
        self.setting: Final[str] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Linear`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Linear``.

        Returns:
            ``Linear`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'linear':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Linear(value)


class Kpert(Data):
    """
    Represents INP kpert data cards.

    ``Kpert`` implements ``Data``.

    Attributes:
        pairs: Dictionary of options.
        suffix: Data card suffix.
    """

    def __init__(self, pairs: dict[DataOption], suffix: types.McnpInteger):
        """
        Initializes ``Kpert``.

        Parameters:
            pairs: Dictionary of options.
            suffix: Data card suffix.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if pairs is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(pairs))

        if suffix is None or not (0 < suffix <= 10_000):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(suffix))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.KPERT
        self.parameters: Final[tuple[any]] = tuple([pairs] + [suffix])
        self.pairs: Final[dict[DataOption]] = pairs
        self.suffix: Final[types.McnpInteger] = suffix
        self.ident: Final[str] = f'kpert{self.suffix}'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Kpert`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for kpert data cards.

        Returns:
            ``Kpert`` object.

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
        if mnemonic != 'kpert':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        suffix = types.McnpInteger.from_mcnp(tokens.popl()[5:])

        pairs = {}
        keywords = re.findall(r'cell|mat|rho|iso|rxn|erg|linear', ' '.join(tokens.deque))
        values = re.split(r'cell|mat|rho|iso|rxn|erg|linear', ' '.join(tokens.deque))[1:]
        for keyword, value in zip(keywords, values):
            match keyword:
                case 'cell':
                    pairs['cell'] = Cell.from_mcnp(f'{keyword}={value}')
                case 'mat':
                    pairs['mat'] = Mat.from_mcnp(f'{keyword}={value}')
                case 'rho':
                    pairs['rho'] = Rho.from_mcnp(f'{keyword}={value}')
                case 'iso':
                    pairs['iso'] = Iso.from_mcnp(f'{keyword}={value}')
                case 'rxn':
                    pairs['rxn'] = Rxn.from_mcnp(f'{keyword}={value}')
                case 'erg':
                    pairs['erg'] = Erg.from_mcnp(f'{keyword}={value}')
                case 'linear':
                    pairs['linear'] = Linear.from_mcnp(f'{keyword}={value}')

        data = Kpert(pairs, suffix)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Kpert`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Kpert``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()}{self.suffix.to_mcnp()} {' '.join(entry.to_mcnp() for entry in self.pairs.values())}"
        )
