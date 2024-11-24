"""
Contains the ``Tropt`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data import DataMnemonic
from ..data import DataOption
from ..data import DataKeyword
from ....utils import errors, _parser


class TroptKeyword(DataKeyword):
    """
    Represents INP tropt data card option keywords.

    ``TroptKeyword`` implements ``DataKeyword``.
    """

    MCSCAT = 'mcscat'
    ELOSS = 'eloss'
    NREACT = 'nreact'
    NESCAT = 'nescat'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``TroptKeyword`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``TroptKeyword``.

        Returns:
            ``TroptKeyword`` object.

        Raises:
            McnpError: INVALID_DATUM_KEYWORD.
        """

        source = _parser.Preprocessor.process_inp(source)

        try:
            return TroptKeyword
        except ValueError:
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD)


class Mcscat(DataOption):
    """
    Represents INP mcscat data card mcscat options.

    ``Mcscat`` implements ``DataOption``.

    Attributes:
        setting: Multiple coulomb scattering setting.
    """

    def __init__(self, setting: str):
        """
        Initializes ``Tropt``.

        Parameters:
            setting: Multiple coulomb scattering setting.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if setting is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[TroptKeyword] = TroptKeyword.MCSCAT
        self.value: Final[str] = setting
        self.setting: Final[str] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Mcscat`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Mcscat``.

        Returns:
            ``Mcscat`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'mcscat':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Mcscat(value)


class Eloss(DataOption):
    """
    Represents INP eloss data card eloss options.

    ``Eloss`` implements ``DataOption``.

    Attributes:
        setting: Slowing down energy losses setting.
    """

    def __init__(self, setting: str):
        """
        Initializes ``Tropt``.

        Parameters:
            setting: Slowing down energy losses setting.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if setting is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[TroptKeyword] = TroptKeyword.ELOSS
        self.value: Final[str] = setting
        self.setting: Final[str] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Eloss`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Eloss``.

        Returns:
            ``Eloss`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'eloss':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Eloss(value)


class Nreact(DataOption):
    """
    Represents INP nreact data card nreact options.

    ``Nreact`` implements ``DataOption``.

    Attributes:
        setting: Nuclear reactions setting.
    """

    def __init__(self, setting: str):
        """
        Initializes ``Tropt``.

        Parameters:
            setting: Nuclear reactions setting.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if setting is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[TroptKeyword] = TroptKeyword.NREACT
        self.value: Final[str] = setting
        self.setting: Final[str] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Nreact`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Nreact``.

        Returns:
            ``Nreact`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'nreact':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Nreact(value)


class Nescat(DataOption):
    """
    Represents INP nescat data card nescat options.

    ``Nescat`` implements ``DataOption``.

    Attributes:
        setting: Nuclear elastic scattering setting.
    """

    def __init__(self, setting: str):
        """
        Initializes ``Tropt``.

        Parameters:
            setting: Nuclear elastic scattering setting.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if setting is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[TroptKeyword] = TroptKeyword.NESCAT
        self.value: Final[str] = setting
        self.setting: Final[str] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Nescat`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Nescat``.

        Returns:
            ``Nescat`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'nescat':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Nescat(value)


class Tropt(Data):
    """
    Represents INP tropt data cards.

    ``Tropt`` implements ``Data``.

    Attributes:
        pairs: Dictionary of options.
    """

    def __init__(self, pairs: dict[DataOption]):
        """
        Initializes ``Tropt``.

        Parameters:
            pairs: Dictionary of options.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if pairs is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(pairs))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.TROPT
        self.parameters: Final[tuple[any]] = tuple([pairs])
        self.pairs: Final[dict[DataOption]] = pairs
        self.ident: Final[str] = 'tropt'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Tropt`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for tropt data cards.

        Returns:
            ``Tropt`` object.

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
        if mnemonic != 'tropt':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        pairs = {}
        keywords = re.findall(r'mcscat|eloss|nreact|nescat', ' '.join(tokens.deque))
        values = re.split(r'mcscat|eloss|nreact|nescat', ' '.join(tokens.deque))[1:]
        for keyword, value in zip(keywords, values):
            match keyword:
                case 'mcscat':
                    pairs['mcscat'] = Mcscat.from_mcnp(f'{keyword}={value}')
                case 'eloss':
                    pairs['eloss'] = Eloss.from_mcnp(f'{keyword}={value}')
                case 'nreact':
                    pairs['nreact'] = Nreact.from_mcnp(f'{keyword}={value}')
                case 'nescat':
                    pairs['nescat'] = Nescat.from_mcnp(f'{keyword}={value}')

        data = Tropt(pairs)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Tropt`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Tropt``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()} {" ".join(entry.to_mcnp() for entry in self.pairs.values())}"
        )
