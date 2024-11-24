"""
Contains the ``Embed`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data import DataMnemonic
from ..data import DataOption
from ..data import DataKeyword
from ....utils import types, errors, _parser


class EmbedKeyword(DataKeyword):
    """
    Represents INP embed data card option keywords.

    ``EmbedKeyword`` implements ``DataKeyword``.
    """

    BACKGROUND = 'background'
    MESHGEO = 'meshgeo'
    MGEOIN = 'mgeoin'
    MEEOUT = 'meeout'
    MEEIN = 'meein'
    CALCVOLS = 'calcvols'
    DEBUG = 'debug'
    FILETYPE = 'filetype'
    GMVFILE = 'gmvfile'
    LENGTH = 'length'
    MCNPUMFILE = 'mcnpumfile'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``EmbedKeyword`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``EmbedKeyword``.

        Returns:
            ``EmbedKeyword`` object.

        Raises:
            McnpError: INVALID_DATUM_KEYWORD.
        """

        source = _parser.Preprocessor.process_inp(source)

        try:
            return EmbedKeyword
        except ValueError:
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD)


class Background(DataOption):
    """
    Represents INP background data card background options.

    ``Background`` implements ``DataOption``.

    Attributes:
        number: Background pseudo-cell number.
    """

    def __init__(self, number: types.McnpInteger):
        """
        Initializes ``Embed``.

        Parameters:
            number: Background pseudo-cell number.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if number is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[EmbedKeyword] = EmbedKeyword.BACKGROUND
        self.value: Final[types.McnpInteger] = number
        self.number: Final[types.McnpInteger] = number

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Background`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Background``.

        Returns:
            ``Background`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'background':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpInteger.from_mcnp(tokens.popl())

        return Background(value)


class Meshgeo(DataOption):
    """
    Represents INP meshgeo data card meshgeo options.

    ``Meshgeo`` implements ``DataOption``.

    Attributes:
        form: Format specification of the embedded mesh input file.
    """

    def __init__(self, form: str):
        """
        Initializes ``Embed``.

        Parameters:
            form: Format specification of the embedded mesh input file.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if form is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[EmbedKeyword] = EmbedKeyword.MESHGEO
        self.value: Final[str] = form
        self.form: Final[str] = form

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Meshgeo`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Meshgeo``.

        Returns:
            ``Meshgeo`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'meshgeo':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Meshgeo(value)


class Mgeoin(DataOption):
    """
    Represents INP mgeoin data card mgeoin options.

    ``Mgeoin`` implements ``DataOption``.

    Attributes:
        filename: Name of the input file containing the mesh description.
    """

    def __init__(self, filename: str):
        """
        Initializes ``Embed``.

        Parameters:
            filename: Name of the input file containing the mesh description.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if filename is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[EmbedKeyword] = EmbedKeyword.MGEOIN
        self.value: Final[str] = filename
        self.filename: Final[str] = filename

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Mgeoin`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Mgeoin``.

        Returns:
            ``Mgeoin`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'mgeoin':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Mgeoin(value)


class Meeout(DataOption):
    """
    Represents INP meeout data card meeout options.

    ``Meeout`` implements ``DataOption``.

    Attributes:
        filename: Name assigned to EEOUT, the elemental edit output file.
    """

    def __init__(self, filename: str):
        """
        Initializes ``Embed``.

        Parameters:
            filename: Name assigned to EEOUT, the elemental edit output file.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if filename is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[EmbedKeyword] = EmbedKeyword.MEEOUT
        self.value: Final[str] = filename
        self.filename: Final[str] = filename

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Meeout`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Meeout``.

        Returns:
            ``Meeout`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'meeout':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Meeout(value)


class Meein(DataOption):
    """
    Represents INP meein data card meein options.

    ``Meein`` implements ``DataOption``.

    Attributes:
        filename: Name of the EEOUT results file to read.
    """

    def __init__(self, filename: str):
        """
        Initializes ``Embed``.

        Parameters:
            filename: Name of the EEOUT results file to read.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if filename is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[EmbedKeyword] = EmbedKeyword.MEEIN
        self.value: Final[str] = filename
        self.filename: Final[str] = filename

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Meein`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Meein``.

        Returns:
            ``Meein`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'meein':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Meein(value)


class Calcvols(DataOption):
    """
    Represents INP calcvols data card calcvols options.

    ``Calcvols`` implements ``DataOption``.

    Attributes:
        setting: Yes/no calculate the inferred geometry cell information.
    """

    def __init__(self, setting: str):
        """
        Initializes ``Embed``.

        Parameters:
            setting: Yes/no calculate the inferred geometry cell information.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if setting is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[EmbedKeyword] = EmbedKeyword.CALCVOLS
        self.value: Final[str] = setting
        self.setting: Final[str] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Calcvols`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Calcvols``.

        Returns:
            ``Calcvols`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'calcvols':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Calcvols(value)


class Debug(DataOption):
    """
    Represents INP debug data card debug options.

    ``Debug`` implements ``DataOption``.

    Attributes:
        parameter: Debug parameter.
    """

    def __init__(self, parameter: str):
        """
        Initializes ``Embed``.

        Parameters:
            parameter: Debug parameter.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if parameter is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[EmbedKeyword] = EmbedKeyword.DEBUG
        self.value: Final[str] = parameter
        self.parameter: Final[str] = parameter

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Debug`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Debug``.

        Returns:
            ``Debug`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'debug':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Debug(value)


class Filetype(DataOption):
    """
    Represents INP filetype data card filetype options.

    ``Filetype`` implements ``DataOption``.

    Attributes:
        kind: File type for the elemental edit output file.
    """

    def __init__(self, kind: str):
        """
        Initializes ``Embed``.

        Parameters:
            kind: File type for the elemental edit output file.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if kind is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[EmbedKeyword] = EmbedKeyword.FILETYPE
        self.value: Final[str] = kind
        self.kind: Final[str] = kind

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Filetype`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Filetype``.

        Returns:
            ``Filetype`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'filetype':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Filetype(value)


class Gmvfile(DataOption):
    """
    Represents INP gmvfile data card gmvfile options.

    ``Gmvfile`` implements ``DataOption``.

    Attributes:
        filename: Name of the GMV output file.
    """

    def __init__(self, filename: str):
        """
        Initializes ``Embed``.

        Parameters:
            filename: Name of the GMV output file.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if filename is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[EmbedKeyword] = EmbedKeyword.GMVFILE
        self.value: Final[str] = filename
        self.filename: Final[str] = filename

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Gmvfile`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Gmvfile``.

        Returns:
            ``Gmvfile`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'gmvfile':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Gmvfile(value)


class Length(DataOption):
    """
    Represents INP length data card length options.

    ``Length`` implements ``DataOption``.

    Attributes:
        factor: Conversion factor to centimeters for all mesh dimentions.
    """

    def __init__(self, factor: types.McnpReal):
        """
        Initializes ``Embed``.

        Parameters:
            factor: Conversion factor to centimeters for all mesh dimentions.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if factor is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[EmbedKeyword] = EmbedKeyword.LENGTH
        self.value: Final[types.McnpReal] = factor
        self.factor: Final[types.McnpReal] = factor

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Length`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Length``.

        Returns:
            ``Length`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'length':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Length(value)


class Mcnpumfile(DataOption):
    """
    Represents INP mcnpumfile data card mcnpumfile options.

    ``Mcnpumfile`` implements ``DataOption``.

    Attributes:
        filename: Name of the MCNPUM output file.
    """

    def __init__(self, filename: str):
        """
        Initializes ``Embed``.

        Parameters:
            filename: Name of the MCNPUM output file.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if filename is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[EmbedKeyword] = EmbedKeyword.MCNPUMFILE
        self.value: Final[str] = filename
        self.filename: Final[str] = filename

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Mcnpumfile`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Mcnpumfile``.

        Returns:
            ``Mcnpumfile`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'mcnpumfile':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Mcnpumfile(value)


class Embed(Data):
    """
    Represents INP embed data cards.

    ``Embed`` implements ``Data``.

    Attributes:
        pairs: Dictionary of options.
    """

    def __init__(self, pairs: dict[DataOption]):
        """
        Initializes ``Embed``.

        Parameters:
            pairs: Dictionary of options.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if pairs is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(pairs))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.EMBED
        self.parameters: Final[tuple[any]] = tuple([pairs])
        self.pairs: Final[dict[DataOption]] = pairs
        self.ident: Final[str] = 'embed'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Embed`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for embed data cards.

        Returns:
            ``Embed`` object.

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
        if mnemonic != 'embed':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        pairs = {}
        keywords = re.findall(
            r'background|meshgeo|mgeoin|meeout|meein|calcvols|debug|filetype|gmvfile|length|mcnpumfile',
            ' '.join(tokens.deque),
        )
        values = re.split(
            r'background|meshgeo|mgeoin|meeout|meein|calcvols|debug|filetype|gmvfile|length|mcnpumfile',
            ' '.join(tokens.deque),
        )[1:]
        for keyword, value in zip(keywords, values):
            match keyword:
                case 'background':
                    pairs['background'] = Background.from_mcnp(f'{keyword}={value}')
                case 'meshgeo':
                    pairs['meshgeo'] = Meshgeo.from_mcnp(f'{keyword}={value}')
                case 'mgeoin':
                    pairs['mgeoin'] = Mgeoin.from_mcnp(f'{keyword}={value}')
                case 'meeout':
                    pairs['meeout'] = Meeout.from_mcnp(f'{keyword}={value}')
                case 'meein':
                    pairs['meein'] = Meein.from_mcnp(f'{keyword}={value}')
                case 'calcvols':
                    pairs['calcvols'] = Calcvols.from_mcnp(f'{keyword}={value}')
                case 'debug':
                    pairs['debug'] = Debug.from_mcnp(f'{keyword}={value}')
                case 'filetype':
                    pairs['filetype'] = Filetype.from_mcnp(f'{keyword}={value}')
                case 'gmvfile':
                    pairs['gmvfile'] = Gmvfile.from_mcnp(f'{keyword}={value}')
                case 'length':
                    pairs['length'] = Length.from_mcnp(f'{keyword}={value}')
                case 'mcnpumfile':
                    pairs['mcnpumfile'] = Mcnpumfile.from_mcnp(f'{keyword}={value}')

        data = Embed(pairs)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Embed`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Embed``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()} {" ".join(entry.to_mcnp() for entry in self.pairs.values())}"
        )
