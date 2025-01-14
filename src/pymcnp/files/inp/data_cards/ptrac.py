"""
Contains the ``Ptrac`` subclass of ``Data``.
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


class PtracKeyword(DataKeyword):
    """
    Represents INP ptrac data card option keywords.

    ``PtracKeyword`` implements ``DataKeyword``.
    """

    BUFFER = 'buffer'
    FILE = 'file'
    MAX = 'max'
    MEPH = 'meph'
    WRITE = 'write'
    CONIC = 'conic'
    EVENT = 'event'
    TYPE = 'type'
    NPS = 'nps'
    CELL = 'cell'
    SURFACE = 'surface'
    TALLY = 'tally'
    VALUE = 'value'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``PtracKeyword`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``PtracKeyword``.

        Returns:
            ``PtracKeyword`` object.

        Raises:
            McnpError: INVALID_DATUM_KEYWORD.
        """

        source = _parser.Preprocessor.process_inp(source)

        try:
            return PtracKeyword
        except ValueError:
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD)


class Buffer(DataOption):
    """
    Represents INP buffer data card buffer options.

    ``Buffer`` implements ``DataOption``.

    Attributes:
        storage: Amount of storage available for filtered events.
    """

    def __init__(self, storage: types.McnpInteger):
        """
        Initializes ``Ptrac``.

        Parameters:
            storage: Amount of storage available for filtered events.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if storage is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[PtracKeyword] = PtracKeyword.BUFFER
        self.value: Final[types.McnpInteger] = storage
        self.storage: Final[types.McnpInteger] = storage

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Buffer`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Buffer``.

        Returns:
            ``Buffer`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'buffer':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpInteger.from_mcnp(tokens.popl())

        return Buffer(value)


class File(DataOption):
    """
    Represents INP file data card file options.

    ``File`` implements ``DataOption``.

    Attributes:
        setting: PTRAC file type.
    """

    def __init__(self, setting: str):
        """
        Initializes ``Ptrac``.

        Parameters:
            setting: PTRAC file type.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if setting is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[PtracKeyword] = PtracKeyword.FILE
        self.value: Final[str] = setting
        self.setting: Final[str] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``File`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``File``.

        Returns:
            ``File`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'file':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return File(value)


class Max(DataOption):
    """
    Represents INP max data card max options.

    ``Max`` implements ``DataOption``.

    Attributes:
        events: Maximum number of events to write.
    """

    def __init__(self, events: types.McnpInteger):
        """
        Initializes ``Ptrac``.

        Parameters:
            events: Maximum number of events to write.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if events is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[PtracKeyword] = PtracKeyword.MAX
        self.value: Final[types.McnpInteger] = events
        self.events: Final[types.McnpInteger] = events

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Max`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Max``.

        Returns:
            ``Max`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'max':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpInteger.from_mcnp(tokens.popl())

        return Max(value)


class Meph(DataOption):
    """
    Represents INP meph data card meph options.

    ``Meph`` implements ``DataOption``.

    Attributes:
        events: Maximum number of events per history to write.
    """

    def __init__(self, events: types.McnpInteger):
        """
        Initializes ``Ptrac``.

        Parameters:
            events: Maximum number of events per history to write.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if events is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[PtracKeyword] = PtracKeyword.MEPH
        self.value: Final[types.McnpInteger] = events
        self.events: Final[types.McnpInteger] = events

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Meph`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Meph``.

        Returns:
            ``Meph`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'meph':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpInteger.from_mcnp(tokens.popl())

        return Meph(value)


class Write(DataOption):
    """
    Represents INP write data card write options.

    ``Write`` implements ``DataOption``.

    Attributes:
        setting: Controls what particle parameters are written.
    """

    def __init__(self, setting: str):
        """
        Initializes ``Ptrac``.

        Parameters:
            setting: Controls what particle parameters are written.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if setting is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[PtracKeyword] = PtracKeyword.WRITE
        self.value: Final[str] = setting
        self.setting: Final[str] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Write`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Write``.

        Returns:
            ``Write`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'write':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Write(value)


class Conic(DataOption):
    """
    Represents INP conic data card conic options.

    ``Conic`` implements ``DataOption``.

    Attributes:
        setting: Activates a PTRAC file format specifically for coincidence tally scoring.
    """

    def __init__(self, setting: str):
        """
        Initializes ``Ptrac``.

        Parameters:
            setting: Activates a PTRAC file format specifically for coincidence tally scoring.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if setting is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[PtracKeyword] = PtracKeyword.CONIC
        self.value: Final[str] = setting
        self.setting: Final[str] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Conic`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Conic``.

        Returns:
            ``Conic`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'conic':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Conic(value)


class Event(DataOption):
    """
    Represents INP event data card event options.

    ``Event`` implements ``DataOption``.

    Attributes:
        setting: Specifies the type of events written to the PTRAC file.
    """

    def __init__(self, setting: str):
        """
        Initializes ``Ptrac``.

        Parameters:
            setting: Specifies the type of events written to the PTRAC file.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if setting is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[PtracKeyword] = PtracKeyword.EVENT
        self.value: Final[str] = setting
        self.setting: Final[str] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Event`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Event``.

        Returns:
            ``Event`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'event':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Event(value)


class Type(DataOption):
    """
    Represents INP type data card type options.

    ``Type`` implements ``DataOption``.

    Attributes:
        particles: Filters events based on one or more particle types.
    """

    def __init__(self, particles: tuple[types.Designator]):
        """
        Initializes ``Ptrac``.

        Parameters:
            particles: Filters events based on one or more particle types.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if particles is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in particles:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(particles))

        self.keyword: Final[PtracKeyword] = PtracKeyword.TYPE
        self.value: Final[tuple[types.Designator]] = particles
        self.particles: Final[tuple[types.Designator]] = particles

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Type`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Type``.

        Returns:
            ``Type`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'type':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tuple([types.Designator.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return Type(value)


class Nps(DataOption):
    """
    Represents INP nps data card nps options.

    ``Nps`` implements ``DataOption``.

    Attributes:
        particles: Sets the range of particle histories for which events will be output.
    """

    def __init__(self, particles: tuple[types.McnpInteger]):
        """
        Initializes ``Ptrac``.

        Parameters:
            particles: Sets the range of particle histories for which events will be output.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if particles is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in particles:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(particles))

        self.keyword: Final[PtracKeyword] = PtracKeyword.NPS
        self.value: Final[tuple[types.McnpInteger]] = particles
        self.particles: Final[tuple[types.McnpInteger]] = particles

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Nps`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Nps``.

        Returns:
            ``Nps`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'nps':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tuple([types.McnpInteger.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return Nps(value)


class Cell(DataOption):
    """
    Represents INP cell data card cell options.

    ``Cell`` implements ``DataOption``.

    Attributes:
        numbers: List of cell numbers for filtering.
    """

    def __init__(self, numbers: tuple[types.McnpInteger]):
        """
        Initializes ``Ptrac``.

        Parameters:
            numbers: List of cell numbers for filtering.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if numbers is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in numbers:
            if entry is None or not (1 <= entry <= 99_999_999):
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(numbers))

        self.keyword: Final[PtracKeyword] = PtracKeyword.CELL
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


class Surface(DataOption):
    """
    Represents INP surface data card surface options.

    ``Surface`` implements ``DataOption``.

    Attributes:
        numbers: List of surface numbers for filtering.
    """

    def __init__(self, numbers: tuple[types.McnpInteger]):
        """
        Initializes ``Ptrac``.

        Parameters:
            numbers: List of surface numbers for filtering.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if numbers is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in numbers:
            if entry is None or not (1 <= entry <= 99_999_999):
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(numbers))

        self.keyword: Final[PtracKeyword] = PtracKeyword.SURFACE
        self.value: Final[tuple[types.McnpInteger]] = numbers
        self.numbers: Final[tuple[types.McnpInteger]] = numbers

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Surface`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Surface``.

        Returns:
            ``Surface`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'surface':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tuple([types.McnpInteger.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return Surface(value)


class Tally(DataOption):
    """
    Represents INP tally data card tally options.

    ``Tally`` implements ``DataOption``.

    Attributes:
        numbers: List of tally numbers for filtering.
    """

    def __init__(self, numbers: tuple[types.McnpInteger]):
        """
        Initializes ``Ptrac``.

        Parameters:
            numbers: List of tally numbers for filtering.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if numbers is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in numbers:
            if entry is None or not (entry != 0):
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(numbers))

        self.keyword: Final[PtracKeyword] = PtracKeyword.TALLY
        self.value: Final[tuple[types.McnpInteger]] = numbers
        self.numbers: Final[tuple[types.McnpInteger]] = numbers

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Tally`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Tally``.

        Returns:
            ``Tally`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'tally':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tuple([types.McnpInteger.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return Tally(value)


class Value(DataOption):
    """
    Represents INP value data card value options.

    ``Value`` implements ``DataOption``.

    Attributes:
        cutoff: Specifies tally cutoff above which history events will be written..
    """

    def __init__(self, cutoff: types.McnpReal):
        """
        Initializes ``Ptrac``.

        Parameters:
            cutoff: Specifies tally cutoff above which history events will be written..

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if cutoff is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[PtracKeyword] = PtracKeyword.VALUE
        self.value: Final[types.McnpReal] = cutoff
        self.cutoff: Final[types.McnpReal] = cutoff

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Value`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Value``.

        Returns:
            ``Value`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'value':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Value(value)


class Ptrac(Data):
    """
    Represents INP ptrac data cards.

    ``Ptrac`` implements ``Data``.

    Attributes:
        pairs: Dictionary of options.
    """

    def __init__(self, pairs: dict[DataOption]):
        """
        Initializes ``Ptrac``.

        Parameters:
            pairs: Dictionary of options.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if pairs is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(pairs))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.PTRAC
        self.parameters: Final[tuple[any]] = tuple([pairs])
        self.pairs: Final[dict[DataOption]] = pairs
        self.ident: Final[str] = 'ptrac'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Ptrac`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ptrac data cards.

        Returns:
            ``Ptrac`` object.

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
        if mnemonic != 'ptrac':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        pairs = {}
        keywords = re.findall(
            r'buffer|file|max|meph|write|conic|event|type|nps|cell|surface|tally|value',
            ' '.join(tokens.deque),
        )
        values = re.split(
            r'buffer|file|max|meph|write|conic|event|type|nps|cell|surface|tally|value',
            ' '.join(tokens.deque),
        )[1:]
        for keyword, value in zip(keywords, values):
            match keyword:
                case 'buffer':
                    pairs['buffer'] = Buffer.from_mcnp(f'{keyword}={value}')
                case 'file':
                    pairs['file'] = File.from_mcnp(f'{keyword}={value}')
                case 'max':
                    pairs['max'] = Max.from_mcnp(f'{keyword}={value}')
                case 'meph':
                    pairs['meph'] = Meph.from_mcnp(f'{keyword}={value}')
                case 'write':
                    pairs['write'] = Write.from_mcnp(f'{keyword}={value}')
                case 'conic':
                    pairs['conic'] = Conic.from_mcnp(f'{keyword}={value}')
                case 'event':
                    pairs['event'] = Event.from_mcnp(f'{keyword}={value}')
                case 'type':
                    pairs['type'] = Type.from_mcnp(f'{keyword}={value}')
                case 'nps':
                    pairs['nps'] = Nps.from_mcnp(f'{keyword}={value}')
                case 'cell':
                    pairs['cell'] = Cell.from_mcnp(f'{keyword}={value}')
                case 'surface':
                    pairs['surface'] = Surface.from_mcnp(f'{keyword}={value}')
                case 'tally':
                    pairs['tally'] = Tally.from_mcnp(f'{keyword}={value}')
                case 'value':
                    pairs['value'] = Value.from_mcnp(f'{keyword}={value}')

        data = Ptrac(pairs)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Ptrac`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Ptrac``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()} {' '.join(entry.to_mcnp() for entry in self.pairs.values())}"
        )
