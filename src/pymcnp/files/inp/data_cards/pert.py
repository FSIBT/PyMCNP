"""
Contains the ``Pert`` subclass of ``Data``.
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


class PertKeyword(DataKeyword):
    """
    Represents INP pert data card option keywords.

    ``PertKeyword`` implements ``DataKeyword``.
    """

    CELL = 'cell'
    MAT = 'mat'
    RHO = 'rho'
    METHOD = 'method'
    RXN = 'rxn'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``PertKeyword`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``PertKeyword``.

        Returns:
            ``PertKeyword`` object.

        Raises:
            McnpError: INVALID_DATUM_KEYWORD.
        """

        source = _parser.Preprocessor.process_inp(source)

        try:
            return PertKeyword
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
        Initializes ``Pert``.

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

        self.keyword: Final[PertKeyword] = PertKeyword.CELL
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
        material: Material number to fill cells.
    """

    def __init__(self, material: types.McnpInteger):
        """
        Initializes ``Pert``.

        Parameters:
            material: Material number to fill cells.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if material is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[PertKeyword] = PertKeyword.MAT
        self.value: Final[types.McnpInteger] = material
        self.material: Final[types.McnpInteger] = material

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


class Rho(DataOption):
    """
    Represents INP rho data card rho options.

    ``Rho`` implements ``DataOption``.

    Attributes:
        density: Perturbed density.
    """

    def __init__(self, density: types.McnpReal):
        """
        Initializes ``Pert``.

        Parameters:
            density: Perturbed density.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if density is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[PertKeyword] = PertKeyword.RHO
        self.value: Final[types.McnpReal] = density
        self.density: Final[types.McnpReal] = density

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

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Rho(value)


class Method(DataOption):
    """
    Represents INP method data card method options.

    ``Method`` implements ``DataOption``.

    Attributes:
        setting: Printing and specifies setting.
    """

    def __init__(self, setting: types.McnpInteger):
        """
        Initializes ``Pert``.

        Parameters:
            setting: Printing and specifies setting.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if setting is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[PertKeyword] = PertKeyword.METHOD
        self.value: Final[types.McnpInteger] = setting
        self.setting: Final[types.McnpInteger] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Method`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Method``.

        Returns:
            ``Method`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'method':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpInteger.from_mcnp(tokens.popl())

        return Method(value)


class Rxn(DataOption):
    """
    Represents INP rxn data card rxn options.

    ``Rxn`` implements ``DataOption``.

    Attributes:
        numbers: ENDF/B reaction number.
    """

    def __init__(self, numbers: tuple[types.McnpInteger]):
        """
        Initializes ``Pert``.

        Parameters:
            numbers: ENDF/B reaction number.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if numbers is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in numbers:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(numbers))

        self.keyword: Final[PertKeyword] = PertKeyword.RXN
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


class Pert(Data):
    """
    Represents INP pert data cards.

    ``Pert`` implements ``Data``.

    Attributes:
        pairs: Dictionary of options.
        suffix: Data card suffix.
        designator: Data card particle designator.
    """

    def __init__(
        self, pairs: dict[DataOption], suffix: types.McnpInteger, designator: types.Designator
    ):
        """
        Initializes ``Pert``.

        Parameters:
            pairs: Dictionary of options.
            suffix: Data card suffix.
            designator: Data card particle designator.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if pairs is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(pairs))

        if suffix is None or not (suffix <= 99_999_999):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(suffix))

        if designator is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(designator))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.PERT
        self.parameters: Final[tuple[any]] = tuple([pairs] + [suffix] + [designator])
        self.pairs: Final[dict[DataOption]] = pairs
        self.suffix: Final[types.McnpInteger] = suffix
        self.designator: Final[types.Designator] = designator
        self.ident: Final[str] = f'pert{self.suffix}:{self.designator}'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Pert`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for pert data cards.

        Returns:
            ``Pert`` object.

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
        if mnemonic != 'pert':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        designator = types.Designator.from_mcnp(tokens.popl())
        suffix = types.McnpInteger.from_mcnp(tokens.popl()[4:])

        pairs = {}
        keywords = re.findall(r'cell|mat|rho|method|rxn', ' '.join(tokens.deque))
        values = re.split(r'cell|mat|rho|method|rxn', ' '.join(tokens.deque))[1:]
        for keyword, value in zip(keywords, values):
            match keyword:
                case 'cell':
                    pairs['cell'] = Cell.from_mcnp(f'{keyword}={value}')
                case 'mat':
                    pairs['mat'] = Mat.from_mcnp(f'{keyword}={value}')
                case 'rho':
                    pairs['rho'] = Rho.from_mcnp(f'{keyword}={value}')
                case 'method':
                    pairs['method'] = Method.from_mcnp(f'{keyword}={value}')
                case 'rxn':
                    pairs['rxn'] = Rxn.from_mcnp(f'{keyword}={value}')

        data = Pert(pairs, suffix, designator)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Pert`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Pert``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()}{self.suffix.to_mcnp()}:{self.designator.to_mcnp()} {' '.join(entry.to_mcnp() for entry in self.pairs.values())}"
        )
