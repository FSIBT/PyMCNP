"""
Contains the ``Ksen`` subclass of ``Data``.
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


class KsenKeyword(DataKeyword):
    """
    Represents INP ksen data card option keywords.

    ``KsenKeyword`` implements ``DataKeyword``.
    """

    ISO = 'iso'
    RXN = 'rxn'
    MT = 'mt'
    ERG = 'erg'
    EIN = 'ein'
    COS = 'cos'
    CONSTRAIN = 'constrain'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``KsenKeyword`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``KsenKeyword``.

        Returns:
            ``KsenKeyword`` object.

        Raises:
            McnpError: INVALID_DATUM_KEYWORD.
        """

        source = _parser.Preprocessor.process_inp(source)

        try:
            return KsenKeyword
        except ValueError:
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD)


class Iso(DataOption):
    """
    Represents INP iso data card iso options.

    ``Iso`` implements ``DataOption``.

    Attributes:
        zaids: List of ZAIDs for pertubation.
    """

    def __init__(self, zaids: tuple[types.McnpReal]):
        """
        Initializes ``Ksen``.

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

        self.keyword: Final[KsenKeyword] = KsenKeyword.ISO
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
        Initializes ``Ksen``.

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

        self.keyword: Final[KsenKeyword] = KsenKeyword.RXN
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


class Mt(DataOption):
    """
    Represents INP mt data card mt options.

    ``Mt`` implements ``DataOption``.

    Attributes:
        numbers: List of reaction numbers for pertubation.
    """

    def __init__(self, numbers: tuple[types.McnpInteger]):
        """
        Initializes ``Ksen``.

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

        self.keyword: Final[KsenKeyword] = KsenKeyword.MT
        self.value: Final[tuple[types.McnpInteger]] = numbers
        self.numbers: Final[tuple[types.McnpInteger]] = numbers

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Mt`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Mt``.

        Returns:
            ``Mt`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'mt':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tuple([types.McnpInteger.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return Mt(value)


class Erg(DataOption):
    """
    Represents INP erg data card erg options.

    ``Erg`` implements ``DataOption``.

    Attributes:
        energies: List of energies.
    """

    def __init__(self, energies: tuple[types.McnpReal]):
        """
        Initializes ``Ksen``.

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

        self.keyword: Final[KsenKeyword] = KsenKeyword.ERG
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


class Ein(DataOption):
    """
    Represents INP ein data card ein options.

    ``Ein`` implements ``DataOption``.

    Attributes:
        energies: List of ranges for incident energies.
    """

    def __init__(self, energies: tuple[types.McnpReal]):
        """
        Initializes ``Ksen``.

        Parameters:
            energies: List of ranges for incident energies.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if energies is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in energies:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(energies))

        self.keyword: Final[KsenKeyword] = KsenKeyword.EIN
        self.value: Final[tuple[types.McnpReal]] = energies
        self.energies: Final[tuple[types.McnpReal]] = energies

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Ein`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Ein``.

        Returns:
            ``Ein`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'ein':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tuple([types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return Ein(value)


class Cos(DataOption):
    """
    Represents INP cos data card cos options.

    ``Cos`` implements ``DataOption``.

    Attributes:
        cosines: Range of direction-change cosines.
    """

    def __init__(self, cosines: tuple[types.McnpReal]):
        """
        Initializes ``Ksen``.

        Parameters:
            cosines: Range of direction-change cosines.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if cosines is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in cosines:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(cosines))

        self.keyword: Final[KsenKeyword] = KsenKeyword.COS
        self.value: Final[tuple[types.McnpReal]] = cosines
        self.cosines: Final[tuple[types.McnpReal]] = cosines

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Cos`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Cos``.

        Returns:
            ``Cos`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'cos':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tuple([types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return Cos(value)


class Constrain(DataOption):
    """
    Represents INP constrain data card constrain options.

    ``Constrain`` implements ``DataOption``.

    Attributes:
        setting: Renormalize sensitivity distribution on/off.
    """

    def __init__(self, setting: str):
        """
        Initializes ``Ksen``.

        Parameters:
            setting: Renormalize sensitivity distribution on/off.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if setting is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[KsenKeyword] = KsenKeyword.CONSTRAIN
        self.value: Final[str] = setting
        self.setting: Final[str] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Constrain`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Constrain``.

        Returns:
            ``Constrain`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'constrain':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Constrain(value)


class Ksen(Data):
    """
    Represents INP ksen data cards.

    ``Ksen`` implements ``Data``.

    Attributes:
        sen: Type of sensitivity.
        pairs: Dictionary of options.
        suffix: Data card suffix.
    """

    def __init__(self, sen: str, pairs: dict[DataOption], suffix: types.McnpInteger):
        """
        Initializes ``Ksen``.

        Parameters:
            sen: Type of sensitivity.
            pairs: Dictionary of options.
            suffix: Data card suffix.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if sen is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(sen))

        if pairs is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(pairs))

        if suffix is None or not (0 < suffix <= 999):
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(suffix))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.KSEN
        self.parameters: Final[tuple[any]] = tuple([sen] + [pairs] + [suffix])
        self.sen: Final[str] = sen
        self.pairs: Final[dict[DataOption]] = pairs
        self.suffix: Final[types.McnpInteger] = suffix
        self.ident: Final[str] = f'ksen{self.suffix}'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Ksen`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ksen data cards.

        Returns:
            ``Ksen`` object.

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
        if mnemonic != 'ksen':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        suffix = types.McnpInteger.from_mcnp(tokens.popl()[4:])

        sen = tokens.popl()
        pairs = {}
        keywords = re.findall(r'iso|rxn|mt|erg|ein|cos|constrain', ' '.join(tokens.deque))
        values = re.split(r'iso|rxn|mt|erg|ein|cos|constrain', ' '.join(tokens.deque))[1:]
        for keyword, value in zip(keywords, values):
            match keyword:
                case 'iso':
                    pairs['iso'] = Iso.from_mcnp(f'{keyword}={value}')
                case 'rxn':
                    pairs['rxn'] = Rxn.from_mcnp(f'{keyword}={value}')
                case 'mt':
                    pairs['mt'] = Mt.from_mcnp(f'{keyword}={value}')
                case 'erg':
                    pairs['erg'] = Erg.from_mcnp(f'{keyword}={value}')
                case 'ein':
                    pairs['ein'] = Ein.from_mcnp(f'{keyword}={value}')
                case 'cos':
                    pairs['cos'] = Cos.from_mcnp(f'{keyword}={value}')
                case 'constrain':
                    pairs['constrain'] = Constrain.from_mcnp(f'{keyword}={value}')

        data = Ksen(sen, pairs, suffix)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Ksen`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Ksen``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()}{self.suffix.to_mcnp()} {self.sen.to_mcnp()} {' '.join(entry.to_mcnp() for entry in self.pairs.values())}"
        )
