"""
Contains the ``Rand`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ..data_option import DataOption
from ..data_keyword import DataKeyword
from ...utils import types, errors, _parser


class RandKeyword(DataKeyword):
    """
    Represents INP rand data card option keywords.

    ``RandKeyword`` implements ``DataKeyword``.
    """

    GEN = 'gen'
    SEED = 'seed'
    STRIDE = 'stride'
    HIST = 'hist'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``RandKeyword`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``RandKeyword``.

        Returns:
            ``RandKeyword`` object.

        Raises:
            McnpError: INVALID_DATUM_KEYWORD.
        """

        source = _parser.Preprocessor.process_inp(source)

        try:
            return RandKeyword
        except ValueError:
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD)


class Gen(DataOption):
    """
    Represents INP gen data card gen options.

    ``Gen`` implements ``DataOption``.

    Attributes:
        setting: Type of pseudorandom number generator.
    """

    def __init__(self, setting: types.McnpInteger):
        """
        Initializes ``Rand``.

        Parameters:
            setting: Type of pseudorandom number generator.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if setting is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[RandKeyword] = RandKeyword.GEN
        self.value: Final[types.McnpInteger] = setting
        self.setting: Final[types.McnpInteger] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Gen`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Gen``.

        Returns:
            ``Gen`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'gen':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpInteger.from_mcnp(tokens.popl())

        return Gen(value)


class Seed(DataOption):
    """
    Represents INP seed data card seed options.

    ``Seed`` implements ``DataOption``.

    Attributes:
        seed: Random number generator seed.
    """

    def __init__(self, seed: types.McnpInteger):
        """
        Initializes ``Rand``.

        Parameters:
            seed: Random number generator seed.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if seed is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[RandKeyword] = RandKeyword.SEED
        self.value: Final[types.McnpInteger] = seed
        self.seed: Final[types.McnpInteger] = seed

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Seed`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Seed``.

        Returns:
            ``Seed`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'seed':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpInteger.from_mcnp(tokens.popl())

        return Seed(value)


class Stride(DataOption):
    """
    Represents INP stride data card stride options.

    ``Stride`` implements ``DataOption``.

    Attributes:
        stride: Number of random numbers between source particle.
    """

    def __init__(self, stride: types.McnpInteger):
        """
        Initializes ``Rand``.

        Parameters:
            stride: Number of random numbers between source particle.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if stride is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[RandKeyword] = RandKeyword.STRIDE
        self.value: Final[types.McnpInteger] = stride
        self.stride: Final[types.McnpInteger] = stride

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Stride`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Stride``.

        Returns:
            ``Stride`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'stride':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpInteger.from_mcnp(tokens.popl())

        return Stride(value)


class Hist(DataOption):
    """
    Represents INP hist data card hist options.

    ``Hist`` implements ``DataOption``.

    Attributes:
        hist: Starting pseudorandom number.
    """

    def __init__(self, hist: types.McnpInteger):
        """
        Initializes ``Rand``.

        Parameters:
            hist: Starting pseudorandom number.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if hist is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[RandKeyword] = RandKeyword.HIST
        self.value: Final[types.McnpInteger] = hist
        self.hist: Final[types.McnpInteger] = hist

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Hist`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Hist``.

        Returns:
            ``Hist`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'hist':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpInteger.from_mcnp(tokens.popl())

        return Hist(value)


class Rand(Data):
    """
    Represents INP rand data cards.

    ``Rand`` implements ``Data``.

    Attributes:
        pairs: Dictionary of options.
    """

    def __init__(self, pairs: dict[DataOption]):
        """
        Initializes ``Rand``.

        Parameters:
            pairs: Dictionary of options.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if pairs is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(pairs))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.RAND
        self.parameters: Final[tuple[any]] = tuple([pairs])
        self.pairs: Final[dict[DataOption]] = pairs
        self.ident: Final[str] = 'rand'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Rand`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for rand data cards.

        Returns:
            ``Rand`` object.

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
        if mnemonic != 'rand':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        pairs = {}
        keywords = re.findall(r'gen|seed|stride|hist', ' '.join(tokens.deque))
        values = re.split(r'gen|seed|stride|hist', ' '.join(tokens.deque))[1:]
        for keyword, value in zip(keywords, values):
            match keyword:
                case 'gen':
                    pairs['gen'] = Gen.from_mcnp(f'{keyword}={value}')
                case 'seed':
                    pairs['seed'] = Seed.from_mcnp(f'{keyword}={value}')
                case 'stride':
                    pairs['stride'] = Stride.from_mcnp(f'{keyword}={value}')
                case 'hist':
                    pairs['hist'] = Hist.from_mcnp(f'{keyword}={value}')

        data = Rand(pairs)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Rand`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Rand``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()} {' '.join(entry.to_mcnp() for entry in self.pairs.values())}"
        )
