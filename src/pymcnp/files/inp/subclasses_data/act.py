"""
Contains the ``Act`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data import DataMnemonic
from ..data import DataOption
from ..data import DataKeyword
from ....utils import types, errors, _parser


class ActKeyword(DataKeyword):
    """
    Represents INP act data card option keywords.

    ``ActKeyword`` implements ``DataKeyword``.
    """

    FISSION = 'fission'
    NONFISS = 'nonfiss'
    DN = 'dn'
    DG = 'dg'
    THRESH = 'thresh'
    DNBAIS = 'dnbais'
    NAP = 'nap'
    PECUT = 'pecut'
    HLCUT = 'hlcut'
    SAMPLE = 'sample'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``ActKeyword`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``ActKeyword``.

        Returns:
            ``ActKeyword`` object.

        Raises:
            McnpError: INVALID_DATUM_KEYWORD.
        """

        source = _parser.Preprocessor.process_inp(source)

        try:
            return ActKeyword
        except ValueError:
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD)


class Fission(DataOption):
    """
    Represents INP fission data card fission options.

    ``Fission`` implements ``DataOption``.

    Attributes:
        kind: Type of delayed particle(s) to be produced from residuals created by fission.
    """

    def __init__(self, kind: str):
        """
        Initializes ``Act``.

        Parameters:
            kind: Type of delayed particle(s) to be produced from residuals created by fission.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if kind is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[ActKeyword] = ActKeyword.FISSION
        self.value: Final[str] = kind
        self.kind: Final[str] = kind

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Fission`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Fission``.

        Returns:
            ``Fission`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'fission':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Fission(value)


class Nonfiss(DataOption):
    """
    Represents INP nonfiss data card nonfiss options.

    ``Nonfiss`` implements ``DataOption``.

    Attributes:
        kind: Type of delayed particle(s) to be produced by simple multi-particle reaction.
    """

    def __init__(self, kind: str):
        """
        Initializes ``Act``.

        Parameters:
            kind: Type of delayed particle(s) to be produced by simple multi-particle reaction.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if kind is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[ActKeyword] = ActKeyword.NONFISS
        self.value: Final[str] = kind
        self.kind: Final[str] = kind

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Nonfiss`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Nonfiss``.

        Returns:
            ``Nonfiss`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'nonfiss':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Nonfiss(value)


class Dn(DataOption):
    """
    Represents INP dn data card dn options.

    ``Dn`` implements ``DataOption``.

    Attributes:
        source: Delayed neutron data source.
    """

    def __init__(self, source: str):
        """
        Initializes ``Act``.

        Parameters:
            source: Delayed neutron data source.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if source is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[ActKeyword] = ActKeyword.DN
        self.value: Final[str] = source
        self.source: Final[str] = source

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Dn`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Dn``.

        Returns:
            ``Dn`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'dn':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Dn(value)


class Dg(DataOption):
    """
    Represents INP dg data card dg options.

    ``Dg`` implements ``DataOption``.

    Attributes:
        source: Delayed gamma data source.
    """

    def __init__(self, source: str):
        """
        Initializes ``Act``.

        Parameters:
            source: Delayed gamma data source.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if source is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[ActKeyword] = ActKeyword.DG
        self.value: Final[str] = source
        self.source: Final[str] = source

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Dg`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Dg``.

        Returns:
            ``Dg`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'dg':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Dg(value)


class Thresh(DataOption):
    """
    Represents INP thresh data card thresh options.

    ``Thresh`` implements ``DataOption``.

    Attributes:
        fraction: Fraction of highest-amplitude discrete delayed-gamma lines retained.
    """

    def __init__(self, fraction: types.McnpReal):
        """
        Initializes ``Act``.

        Parameters:
            fraction: Fraction of highest-amplitude discrete delayed-gamma lines retained.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if fraction is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[ActKeyword] = ActKeyword.THRESH
        self.value: Final[types.McnpReal] = fraction
        self.fraction: Final[types.McnpReal] = fraction

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Thresh`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Thresh``.

        Returns:
            ``Thresh`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'thresh':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Thresh(value)


class Dnbais(DataOption):
    """
    Represents INP dnbais data card dnbais options.

    ``Dnbais`` implements ``DataOption``.

    Attributes:
        count: Maximum number of neutrons generated per reaction.
    """

    def __init__(self, count: types.McnpInteger):
        """
        Initializes ``Act``.

        Parameters:
            count: Maximum number of neutrons generated per reaction.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if count is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[ActKeyword] = ActKeyword.DNBAIS
        self.value: Final[types.McnpInteger] = count
        self.count: Final[types.McnpInteger] = count

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Dnbais`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Dnbais``.

        Returns:
            ``Dnbais`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'dnbais':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpInteger.from_mcnp(tokens.popl())

        return Dnbais(value)


class Nap(DataOption):
    """
    Represents INP nap data card nap options.

    ``Nap`` implements ``DataOption``.

    Attributes:
        count: Number of activation products.
    """

    def __init__(self, count: types.McnpInteger):
        """
        Initializes ``Act``.

        Parameters:
            count: Number of activation products.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if count is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[ActKeyword] = ActKeyword.NAP
        self.value: Final[types.McnpInteger] = count
        self.count: Final[types.McnpInteger] = count

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Nap`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Nap``.

        Returns:
            ``Nap`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'nap':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpInteger.from_mcnp(tokens.popl())

        return Nap(value)


class Pecut(DataOption):
    """
    Represents INP pecut data card pecut options.

    ``Pecut`` implements ``DataOption``.

    Attributes:
        cutoff: Delayed-gamma energy cutoff.
    """

    def __init__(self, cutoff: types.McnpReal):
        """
        Initializes ``Act``.

        Parameters:
            cutoff: Delayed-gamma energy cutoff.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if cutoff is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[ActKeyword] = ActKeyword.PECUT
        self.value: Final[types.McnpReal] = cutoff
        self.cutoff: Final[types.McnpReal] = cutoff

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Pecut`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Pecut``.

        Returns:
            ``Pecut`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'pecut':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Pecut(value)


class Hlcut(DataOption):
    """
    Represents INP hlcut data card hlcut options.

    ``Hlcut`` implements ``DataOption``.

    Attributes:
        cutoff: Spontaneous-decay half-life threshold.
    """

    def __init__(self, cutoff: types.McnpReal):
        """
        Initializes ``Act``.

        Parameters:
            cutoff: Spontaneous-decay half-life threshold.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if cutoff is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[ActKeyword] = ActKeyword.HLCUT
        self.value: Final[types.McnpReal] = cutoff
        self.cutoff: Final[types.McnpReal] = cutoff

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Hlcut`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Hlcut``.

        Returns:
            ``Hlcut`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'hlcut':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Hlcut(value)


class Sample(DataOption):
    """
    Represents INP sample data card sample options.

    ``Sample`` implements ``DataOption``.

    Attributes:
        setting: Flag for correlated or uncorrelated.
    """

    def __init__(self, setting: str):
        """
        Initializes ``Act``.

        Parameters:
            setting: Flag for correlated or uncorrelated.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if setting is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[ActKeyword] = ActKeyword.SAMPLE
        self.value: Final[str] = setting
        self.setting: Final[str] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Sample`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Sample``.

        Returns:
            ``Sample`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'sample':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Sample(value)


class Act(Data):
    """
    Represents INP act data cards.

    ``Act`` implements ``Data``.

    Attributes:
        pairs: Dictionary of options.
    """

    def __init__(self, pairs: dict[DataOption]):
        """
        Initializes ``Act``.

        Parameters:
            pairs: Dictionary of options.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if pairs is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(pairs))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.ACT
        self.parameters: Final[tuple[any]] = tuple([pairs])
        self.pairs: Final[dict[DataOption]] = pairs
        self.ident: Final[str] = 'act'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Act`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for act data cards.

        Returns:
            ``Act`` object.

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
        if mnemonic != 'act':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        pairs = {}
        keywords = re.findall(
            r'fission|nonfiss|dn|dg|thresh|dnbais|nap|pecut|hlcut|sample', ' '.join(tokens.deque)
        )
        values = re.split(
            r'fission|nonfiss|dn|dg|thresh|dnbais|nap|pecut|hlcut|sample', ' '.join(tokens.deque)
        )[1:]
        for keyword, value in zip(keywords, values):
            match keyword:
                case 'fission':
                    pairs['fission'] = Fission.from_mcnp(f'{keyword}={value}')
                case 'nonfiss':
                    pairs['nonfiss'] = Nonfiss.from_mcnp(f'{keyword}={value}')
                case 'dn':
                    pairs['dn'] = Dn.from_mcnp(f'{keyword}={value}')
                case 'dg':
                    pairs['dg'] = Dg.from_mcnp(f'{keyword}={value}')
                case 'thresh':
                    pairs['thresh'] = Thresh.from_mcnp(f'{keyword}={value}')
                case 'dnbais':
                    pairs['dnbais'] = Dnbais.from_mcnp(f'{keyword}={value}')
                case 'nap':
                    pairs['nap'] = Nap.from_mcnp(f'{keyword}={value}')
                case 'pecut':
                    pairs['pecut'] = Pecut.from_mcnp(f'{keyword}={value}')
                case 'hlcut':
                    pairs['hlcut'] = Hlcut.from_mcnp(f'{keyword}={value}')
                case 'sample':
                    pairs['sample'] = Sample.from_mcnp(f'{keyword}={value}')

        data = Act(pairs)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Act`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Act``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()} {" ".join(entry.to_mcnp() for entry in self.pairs.values())}"
        )
