"""
Contains the ``Kopts`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data_mnemonic import DataMnemonic
from ..data_option import DataOption
from ..data_keyword import DataKeyword
from ...utils import types, errors, _parser


class KoptsKeyword(DataKeyword):
    """
    Represents INP kopts data card option keywords.

    ``KoptsKeyword`` implements ``DataKeyword``.
    """

    BLOCKSIZE = 'blocksize'
    KINETICS = 'kinetics'
    PRECURSOR = 'precursor'
    KSENTAL = 'ksental'
    FMAT = 'fmat'
    FMATSKPT = 'fmatskpt'
    FMATNCYC = 'fmatncyc'
    FMATSPACE = 'fmatspace'
    FMATACCEL = 'fmataccel'
    FMATREDUCE = 'fmatreduce'
    FMATNX = 'fmatnx'
    FMATNY = 'fmatny'
    FMATNZ = 'fmatnz'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``KoptsKeyword`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``KoptsKeyword``.

        Returns:
            ``KoptsKeyword`` object.

        Raises:
            McnpError: INVALID_DATUM_KEYWORD.
        """

        source = _parser.Preprocessor.process_inp(source)

        try:
            return KoptsKeyword
        except ValueError:
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD)


class Blocksize(DataOption):
    """
    Represents INP blocksize data card blocksize options.

    ``Blocksize`` implements ``DataOption``.

    Attributes:
        ncy: Number of cycles in every outer iteration.
    """

    def __init__(self, ncy: types.McnpInteger):
        """
        Initializes ``Kopts``.

        Parameters:
            ncy: Number of cycles in every outer iteration.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if ncy is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[KoptsKeyword] = KoptsKeyword.BLOCKSIZE
        self.value: Final[types.McnpInteger] = ncy
        self.ncy: Final[types.McnpInteger] = ncy

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Blocksize`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Blocksize``.

        Returns:
            ``Blocksize`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'blocksize':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpInteger.from_mcnp(tokens.popl())

        return Blocksize(value)


class Kinetics(DataOption):
    """
    Represents INP kinetics data card kinetics options.

    ``Kinetics`` implements ``DataOption``.

    Attributes:
        setting: Yes/No calculate point-kinetics parameters.
    """

    def __init__(self, setting: str):
        """
        Initializes ``Kopts``.

        Parameters:
            setting: Yes/No calculate point-kinetics parameters.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if setting is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[KoptsKeyword] = KoptsKeyword.KINETICS
        self.value: Final[str] = setting
        self.setting: Final[str] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Kinetics`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Kinetics``.

        Returns:
            ``Kinetics`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'kinetics':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Kinetics(value)


class Precursor(DataOption):
    """
    Represents INP precursor data card precursor options.

    ``Precursor`` implements ``DataOption``.

    Attributes:
        setting: Yes/No detailed precursor information.
    """

    def __init__(self, setting: str):
        """
        Initializes ``Kopts``.

        Parameters:
            setting: Yes/No detailed precursor information.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if setting is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[KoptsKeyword] = KoptsKeyword.PRECURSOR
        self.value: Final[str] = setting
        self.setting: Final[str] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Precursor`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Precursor``.

        Returns:
            ``Precursor`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'precursor':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Precursor(value)


class Ksental(DataOption):
    """
    Represents INP ksental data card ksental options.

    ``Ksental`` implements ``DataOption``.

    Attributes:
        fileopt: Format of sensity profiles output file.
    """

    def __init__(self, fileopt: str):
        """
        Initializes ``Kopts``.

        Parameters:
            fileopt: Format of sensity profiles output file.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if fileopt is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[KoptsKeyword] = KoptsKeyword.KSENTAL
        self.value: Final[str] = fileopt
        self.fileopt: Final[str] = fileopt

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Ksental`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Ksental``.

        Returns:
            ``Ksental`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'ksental':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Ksental(value)


class Fmat(DataOption):
    """
    Represents INP fmat data card fmat options.

    ``Fmat`` implements ``DataOption``.

    Attributes:
        setting: Yes/No FMAT.
    """

    def __init__(self, setting: str):
        """
        Initializes ``Kopts``.

        Parameters:
            setting: Yes/No FMAT.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if setting is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[KoptsKeyword] = KoptsKeyword.FMAT
        self.value: Final[str] = setting
        self.setting: Final[str] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Fmat`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Fmat``.

        Returns:
            ``Fmat`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'fmat':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Fmat(value)


class Fmatskpt(DataOption):
    """
    Represents INP fmatskpt data card fmatskpt options.

    ``Fmatskpt`` implements ``DataOption``.

    Attributes:
        fmat_skip: fmat_skip.
    """

    def __init__(self, fmat_skip: types.McnpReal):
        """
        Initializes ``Kopts``.

        Parameters:
            fmat_skip: fmat_skip.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if fmat_skip is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[KoptsKeyword] = KoptsKeyword.FMATSKPT
        self.value: Final[types.McnpReal] = fmat_skip
        self.fmat_skip: Final[types.McnpReal] = fmat_skip

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Fmatskpt`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Fmatskpt``.

        Returns:
            ``Fmatskpt`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'fmatskpt':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Fmatskpt(value)


class Fmatncyc(DataOption):
    """
    Represents INP fmatncyc data card fmatncyc options.

    ``Fmatncyc`` implements ``DataOption``.

    Attributes:
        fmat_ncyc: fmat_ncyc.
    """

    def __init__(self, fmat_ncyc: types.McnpReal):
        """
        Initializes ``Kopts``.

        Parameters:
            fmat_ncyc: fmat_ncyc.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if fmat_ncyc is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[KoptsKeyword] = KoptsKeyword.FMATNCYC
        self.value: Final[types.McnpReal] = fmat_ncyc
        self.fmat_ncyc: Final[types.McnpReal] = fmat_ncyc

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Fmatncyc`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Fmatncyc``.

        Returns:
            ``Fmatncyc`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'fmatncyc':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Fmatncyc(value)


class Fmatspace(DataOption):
    """
    Represents INP fmatspace data card fmatspace options.

    ``Fmatspace`` implements ``DataOption``.

    Attributes:
        fmat_space: fmat_space.
    """

    def __init__(self, fmat_space: types.McnpReal):
        """
        Initializes ``Kopts``.

        Parameters:
            fmat_space: fmat_space.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if fmat_space is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[KoptsKeyword] = KoptsKeyword.FMATSPACE
        self.value: Final[types.McnpReal] = fmat_space
        self.fmat_space: Final[types.McnpReal] = fmat_space

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Fmatspace`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Fmatspace``.

        Returns:
            ``Fmatspace`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'fmatspace':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Fmatspace(value)


class Fmataccel(DataOption):
    """
    Represents INP fmataccel data card fmataccel options.

    ``Fmataccel`` implements ``DataOption``.

    Attributes:
        setting: fmataccel.
    """

    def __init__(self, setting: str):
        """
        Initializes ``Kopts``.

        Parameters:
            setting: fmataccel.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if setting is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[KoptsKeyword] = KoptsKeyword.FMATACCEL
        self.value: Final[str] = setting
        self.setting: Final[str] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Fmataccel`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Fmataccel``.

        Returns:
            ``Fmataccel`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'fmataccel':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Fmataccel(value)


class Fmatreduce(DataOption):
    """
    Represents INP fmatreduce data card fmatreduce options.

    ``Fmatreduce`` implements ``DataOption``.

    Attributes:
        setting: fmatreduce.
    """

    def __init__(self, setting: str):
        """
        Initializes ``Kopts``.

        Parameters:
            setting: fmatreduce.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if setting is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[KoptsKeyword] = KoptsKeyword.FMATREDUCE
        self.value: Final[str] = setting
        self.setting: Final[str] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Fmatreduce`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Fmatreduce``.

        Returns:
            ``Fmatreduce`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'fmatreduce':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Fmatreduce(value)


class Fmatnx(DataOption):
    """
    Represents INP fmatnx data card fmatnx options.

    ``Fmatnx`` implements ``DataOption``.

    Attributes:
        fmat_nx: fmat_nx.
    """

    def __init__(self, fmat_nx: types.McnpReal):
        """
        Initializes ``Kopts``.

        Parameters:
            fmat_nx: fmat_nx.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if fmat_nx is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[KoptsKeyword] = KoptsKeyword.FMATNX
        self.value: Final[types.McnpReal] = fmat_nx
        self.fmat_nx: Final[types.McnpReal] = fmat_nx

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Fmatnx`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Fmatnx``.

        Returns:
            ``Fmatnx`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'fmatnx':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Fmatnx(value)


class Fmatny(DataOption):
    """
    Represents INP fmatny data card fmatny options.

    ``Fmatny`` implements ``DataOption``.

    Attributes:
        fmat_ny: fmat_ny.
    """

    def __init__(self, fmat_ny: types.McnpReal):
        """
        Initializes ``Kopts``.

        Parameters:
            fmat_ny: fmat_ny.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if fmat_ny is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[KoptsKeyword] = KoptsKeyword.FMATNY
        self.value: Final[types.McnpReal] = fmat_ny
        self.fmat_ny: Final[types.McnpReal] = fmat_ny

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Fmatny`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Fmatny``.

        Returns:
            ``Fmatny`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'fmatny':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Fmatny(value)


class Fmatnz(DataOption):
    """
    Represents INP fmatnz data card fmatnz options.

    ``Fmatnz`` implements ``DataOption``.

    Attributes:
        fmat_nz: fmat_nz.
    """

    def __init__(self, fmat_nz: types.McnpReal):
        """
        Initializes ``Kopts``.

        Parameters:
            fmat_nz: fmat_nz.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if fmat_nz is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[KoptsKeyword] = KoptsKeyword.FMATNZ
        self.value: Final[types.McnpReal] = fmat_nz
        self.fmat_nz: Final[types.McnpReal] = fmat_nz

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Fmatnz`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Fmatnz``.

        Returns:
            ``Fmatnz`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'fmatnz':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Fmatnz(value)


class Kopts(Data):
    """
    Represents INP kopts data cards.

    ``Kopts`` implements ``Data``.

    Attributes:
        pairs: Dictionary of options.
    """

    def __init__(self, pairs: dict[DataOption]):
        """
        Initializes ``Kopts``.

        Parameters:
            pairs: Dictionary of options.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if pairs is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(pairs))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.KOPTS
        self.parameters: Final[tuple[any]] = tuple([pairs])
        self.pairs: Final[dict[DataOption]] = pairs
        self.ident: Final[str] = 'kopts'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Kopts`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for kopts data cards.

        Returns:
            ``Kopts`` object.

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
        if mnemonic != 'kopts':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        pairs = {}
        keywords = re.findall(
            r'blocksize|kinetics|precursor|ksental|fmat|fmatskpt|fmatncyc|fmatspace|fmataccel|fmatreduce|fmatnx|fmatny|fmatnz',
            ' '.join(tokens.deque),
        )
        values = re.split(
            r'blocksize|kinetics|precursor|ksental|fmat|fmatskpt|fmatncyc|fmatspace|fmataccel|fmatreduce|fmatnx|fmatny|fmatnz',
            ' '.join(tokens.deque),
        )[1:]
        for keyword, value in zip(keywords, values):
            match keyword:
                case 'blocksize':
                    pairs['blocksize'] = Blocksize.from_mcnp(f'{keyword}={value}')
                case 'kinetics':
                    pairs['kinetics'] = Kinetics.from_mcnp(f'{keyword}={value}')
                case 'precursor':
                    pairs['precursor'] = Precursor.from_mcnp(f'{keyword}={value}')
                case 'ksental':
                    pairs['ksental'] = Ksental.from_mcnp(f'{keyword}={value}')
                case 'fmat':
                    pairs['fmat'] = Fmat.from_mcnp(f'{keyword}={value}')
                case 'fmatskpt':
                    pairs['fmatskpt'] = Fmatskpt.from_mcnp(f'{keyword}={value}')
                case 'fmatncyc':
                    pairs['fmatncyc'] = Fmatncyc.from_mcnp(f'{keyword}={value}')
                case 'fmatspace':
                    pairs['fmatspace'] = Fmatspace.from_mcnp(f'{keyword}={value}')
                case 'fmataccel':
                    pairs['fmataccel'] = Fmataccel.from_mcnp(f'{keyword}={value}')
                case 'fmatreduce':
                    pairs['fmatreduce'] = Fmatreduce.from_mcnp(f'{keyword}={value}')
                case 'fmatnx':
                    pairs['fmatnx'] = Fmatnx.from_mcnp(f'{keyword}={value}')
                case 'fmatny':
                    pairs['fmatny'] = Fmatny.from_mcnp(f'{keyword}={value}')
                case 'fmatnz':
                    pairs['fmatnz'] = Fmatnz.from_mcnp(f'{keyword}={value}')

        data = Kopts(pairs)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Kopts`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Kopts``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()} {' '.join(entry.to_mcnp() for entry in self.pairs.values())}"
        )
