"""
Contains the ``Var`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ..data_option import DataOption
from ..data_keyword import DataKeyword
from ...utils import errors
from ...utils import _parser


class VarKeyword(DataKeyword):
    """
    Represents INP var data card option keywords.

    ``VarKeyword`` implements ``DataKeyword``.
    """

    RR = 'rr'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``VarKeyword`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``VarKeyword``.

        Returns:
            ``VarKeyword`` object.

        Raises:
            McnpError: INVALID_DATUM_KEYWORD.
        """

        source = _parser.Preprocessor.process_inp(source)

        try:
            return VarKeyword
        except ValueError:
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD)


class Rr(DataOption):
    """
    Represents INP rr data card rr options.

    ``Rr`` implements ``DataOption``.

    Attributes:
        setting: Roulette game for weight windows and cell/energy/time importance off/no.
    """

    def __init__(self, setting: str):
        """
        Initializes ``Var``.

        Parameters:
            setting: Roulette game for weight windows and cell/energy/time importance off/no.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if setting is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[VarKeyword] = VarKeyword.RR
        self.value: Final[str] = setting
        self.setting: Final[str] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Rr`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Rr``.

        Returns:
            ``Rr`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'rr':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Rr(value)


class Var(Data):
    """
    Represents INP var data cards.

    ``Var`` implements ``Data``.

    Attributes:
        pairs: Dictionary of options.
    """

    def __init__(self, pairs: dict[DataOption]):
        """
        Initializes ``Var``.

        Parameters:
            pairs: Dictionary of options.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if pairs is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(pairs))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.VAR
        self.parameters: Final[tuple[any]] = tuple([pairs])
        self.pairs: Final[dict[DataOption]] = pairs
        self.ident: Final[str] = 'var'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Var`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for var data cards.

        Returns:
            ``Var`` object.

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
        if mnemonic != 'var':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        pairs = {}
        keywords = re.findall(r'rr', ' '.join(tokens.deque))
        values = re.split(r'rr', ' '.join(tokens.deque))[1:]
        for keyword, value in zip(keywords, values):
            match keyword:
                case 'rr':
                    pairs['rr'] = Rr.from_mcnp(f'{keyword}={value}')

        data = Var(pairs)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Var`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Var``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()} {' '.join(entry.to_mcnp() for entry in self.pairs.values())}"
        )
