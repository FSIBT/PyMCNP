"""
Contains the ``Ssr`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data import DataMnemonic
from ..data import DataOption
from ..data import DataKeyword
from ....utils import types, errors, _parser


class SsrKeyword(DataKeyword):
    """
    Represents INP ssr data card option keywords.

    ``SsrKeyword`` implements ``DataKeyword``.
    """

    OLD = 'old'
    CEL = 'cel'
    NEW = 'new'
    PTY = 'pty'
    COL = 'col'
    WGT = 'wgt'
    AXS = 'axs'
    EXT = 'ext'
    POA = 'poa'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SsrKeyword`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``SsrKeyword``.

        Returns:
            ``SsrKeyword`` object.

        Raises:
            McnpError: INVALID_DATUM_KEYWORD.
        """

        source = _parser.Preprocessor.process_inp(source)

        try:
            return SsrKeyword
        except ValueError:
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD)


class Old(DataOption):
    """
    Represents INP old data card old options.

    ``Old`` implements ``DataOption``.

    Attributes:
        numbers: Tuple of surface numbers from subset of surfaces on SSW card.
    """

    def __init__(self, numbers: tuple[types.McnpInteger]):
        """
        Initializes ``Ssr``.

        Parameters:
            numbers: Tuple of surface numbers from subset of surfaces on SSW card.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if numbers is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in numbers:
            if entry is None or not (1 <= entry <= 99_999_999):
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(numbers))

        self.keyword: Final[SsrKeyword] = SsrKeyword.OLD
        self.value: Final[tuple[types.McnpInteger]] = numbers
        self.numbers: Final[tuple[types.McnpInteger]] = numbers

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Old`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Old``.

        Returns:
            ``Old`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'old':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tuple([types.McnpInteger.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return Old(value)


class Cel(DataOption):
    """
    Represents INP cel data card cel options.

    ``Cel`` implements ``DataOption``.

    Attributes:
        numbers: Tuple of cell from subset of cells on SSW card.
    """

    def __init__(self, numbers: tuple[types.McnpInteger]):
        """
        Initializes ``Ssr``.

        Parameters:
            numbers: Tuple of cell from subset of cells on SSW card.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if numbers is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in numbers:
            if entry is None or not (1 <= entry <= 99_999_999):
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(numbers))

        self.keyword: Final[SsrKeyword] = SsrKeyword.CEL
        self.value: Final[tuple[types.McnpInteger]] = numbers
        self.numbers: Final[tuple[types.McnpInteger]] = numbers

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Cel`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Cel``.

        Returns:
            ``Cel`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'cel':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tuple([types.McnpInteger.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return Cel(value)


class New(DataOption):
    """
    Represents INP new data card new options.

    ``New`` implements ``DataOption``.

    Attributes:
        numbers: Tuple of surface numbers to start run.
    """

    def __init__(self, numbers: tuple[types.McnpInteger]):
        """
        Initializes ``Ssr``.

        Parameters:
            numbers: Tuple of surface numbers to start run.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if numbers is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in numbers:
            if entry is None or not (1 <= entry <= 99_999_999):
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(numbers))

        self.keyword: Final[SsrKeyword] = SsrKeyword.NEW
        self.value: Final[tuple[types.McnpInteger]] = numbers
        self.numbers: Final[tuple[types.McnpInteger]] = numbers

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``New`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``New``.

        Returns:
            ``New`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'new':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tuple([types.McnpInteger.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return New(value)


class Pty(DataOption):
    """
    Represents INP pty data card pty options.

    ``Pty`` implements ``DataOption``.

    Attributes:
        particles: Tuple of designators.
    """

    def __init__(self, particles: tuple[types.Designator]):
        """
        Initializes ``Ssr``.

        Parameters:
            particles: Tuple of designators.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if particles is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in particles:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(particles))

        self.keyword: Final[SsrKeyword] = SsrKeyword.PTY
        self.value: Final[tuple[types.Designator]] = particles
        self.particles: Final[tuple[types.Designator]] = particles

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Pty`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Pty``.

        Returns:
            ``Pty`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'pty':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tuple([types.Designator.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return Pty(value)


class Col(DataOption):
    """
    Represents INP col data card col options.

    ``Col`` implements ``DataOption``.

    Attributes:
        setting: Collision option setting.
    """

    def __init__(self, setting: types.McnpInteger):
        """
        Initializes ``Ssr``.

        Parameters:
            setting: Collision option setting.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if setting is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[SsrKeyword] = SsrKeyword.COL
        self.value: Final[types.McnpInteger] = setting
        self.setting: Final[types.McnpInteger] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Col`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Col``.

        Returns:
            ``Col`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'col':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpInteger.from_mcnp(tokens.popl())

        return Col(value)


class Wgt(DataOption):
    """
    Represents INP wgt data card wgt options.

    ``Wgt`` implements ``DataOption``.

    Attributes:
        constant: Particle weight multiplier.
    """

    def __init__(self, constant: types.McnpReal):
        """
        Initializes ``Ssr``.

        Parameters:
            constant: Particle weight multiplier.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if constant is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[SsrKeyword] = SsrKeyword.WGT
        self.value: Final[types.McnpReal] = constant
        self.constant: Final[types.McnpReal] = constant

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Wgt`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Wgt``.

        Returns:
            ``Wgt`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'wgt':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Wgt(value)


class Axs(DataOption):
    """
    Represents INP axs data card axs options.

    ``Axs`` implements ``DataOption``.

    Attributes:
        cosines: Direction cosines defining.
    """

    def __init__(self, cosines: tuple[types.McnpReal]):
        """
        Initializes ``Ssr``.

        Parameters:
            cosines: Direction cosines defining.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if cosines is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in cosines:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(cosines))

        self.keyword: Final[SsrKeyword] = SsrKeyword.AXS
        self.value: Final[tuple[types.McnpReal]] = cosines
        self.cosines: Final[tuple[types.McnpReal]] = cosines

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Axs`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Axs``.

        Returns:
            ``Axs`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'axs':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tuple([types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return Axs(value)


class Ext(DataOption):
    """
    Represents INP ext data card ext options.

    ``Ext`` implements ``DataOption``.

    Attributes:
        number: Distribution number for baising sampling.
    """

    def __init__(self, number: types.DistributionNumber):
        """
        Initializes ``Ssr``.

        Parameters:
            number: Distribution number for baising sampling.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if number is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[SsrKeyword] = SsrKeyword.EXT
        self.value: Final[types.DistributionNumber] = number
        self.number: Final[types.DistributionNumber] = number

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Ext`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Ext``.

        Returns:
            ``Ext`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'ext':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.DistributionNumber.from_mcnp(tokens.popl())

        return Ext(value)


class Poa(DataOption):
    """
    Represents INP poa data card poa options.

    ``Poa`` implements ``DataOption``.

    Attributes:
        angle: Angle within which particles accepeted for transport.
    """

    def __init__(self, angle: types.McnpReal):
        """
        Initializes ``Ssr``.

        Parameters:
            angle: Angle within which particles accepeted for transport.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if angle is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[SsrKeyword] = SsrKeyword.POA
        self.value: Final[types.McnpReal] = angle
        self.angle: Final[types.McnpReal] = angle

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Poa`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Poa``.

        Returns:
            ``Poa`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'poa':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Poa(value)


class Ssr(Data):
    """
    Represents INP ssr data cards.

    ``Ssr`` implements ``Data``.

    Attributes:
        pairs: Dictionary of options.
    """

    def __init__(self, pairs: dict[DataOption]):
        """
        Initializes ``Ssr``.

        Parameters:
            pairs: Dictionary of options.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if pairs is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(pairs))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.SSR
        self.parameters: Final[tuple[any]] = tuple([pairs])
        self.pairs: Final[dict[DataOption]] = pairs
        self.ident: Final[str] = 'ssr'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Ssr`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ssr data cards.

        Returns:
            ``Ssr`` object.

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
        if mnemonic != 'ssr':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        pairs = {}
        keywords = re.findall(r'old|cel|new|pty|col|wgt|axs|ext|poa', ' '.join(tokens.deque))
        values = re.split(r'old|cel|new|pty|col|wgt|axs|ext|poa', ' '.join(tokens.deque))[1:]
        for keyword, value in zip(keywords, values):
            match keyword:
                case 'old':
                    pairs['old'] = Old.from_mcnp(f'{keyword}={value}')
                case 'cel':
                    pairs['cel'] = Cel.from_mcnp(f'{keyword}={value}')
                case 'new':
                    pairs['new'] = New.from_mcnp(f'{keyword}={value}')
                case 'pty':
                    pairs['pty'] = Pty.from_mcnp(f'{keyword}={value}')
                case 'col':
                    pairs['col'] = Col.from_mcnp(f'{keyword}={value}')
                case 'wgt':
                    pairs['wgt'] = Wgt.from_mcnp(f'{keyword}={value}')
                case 'axs':
                    pairs['axs'] = Axs.from_mcnp(f'{keyword}={value}')
                case 'ext':
                    pairs['ext'] = Ext.from_mcnp(f'{keyword}={value}')
                case 'poa':
                    pairs['poa'] = Poa.from_mcnp(f'{keyword}={value}')

        data = Ssr(pairs)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Ssr`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Ssr``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()} {" ".join(entry.to_mcnp() for entry in self.pairs.values())}"
        )
