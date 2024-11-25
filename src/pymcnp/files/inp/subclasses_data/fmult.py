"""
Contains the ``Fmult`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data import DataMnemonic
from ..data import DataOption
from ..data import DataKeyword
from ...utils import types, errors, _parser


class FmultKeyword(DataKeyword):
    """
    Represents INP fmult data card option keywords.

    ``FmultKeyword`` implements ``DataKeyword``.
    """

    SFNU = 'sfnu'
    WIDTH = 'width'
    SFYIELD = 'sfyield'
    METHOD = 'method'
    SHIFT = 'shift'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``FmultKeyword`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``FmultKeyword``.

        Returns:
            ``FmultKeyword`` object.

        Raises:
            McnpError: INVALID_DATUM_KEYWORD.
        """

        source = _parser.Preprocessor.process_inp(source)

        try:
            return FmultKeyword
        except ValueError:
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD)


class Sfnu(DataOption):
    """
    Represents INP sfnu data card sfnu options.

    ``Sfnu`` implements ``DataOption``.

    Attributes:
        nu: V bar for sampling spontaneous fission.
    """

    def __init__(self, nu: types.McnpReal):
        """
        Initializes ``Fmult``.

        Parameters:
            nu: V bar for sampling spontaneous fission.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if nu is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[FmultKeyword] = FmultKeyword.SFNU
        self.value: Final[types.McnpReal] = nu
        self.nu: Final[types.McnpReal] = nu

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Sfnu`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Sfnu``.

        Returns:
            ``Sfnu`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'sfnu':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Sfnu(value)


class Width(DataOption):
    """
    Represents INP width data card width options.

    ``Width`` implements ``DataOption``.

    Attributes:
        width: Width for sampling spontaneous fission.
    """

    def __init__(self, width: types.McnpReal):
        """
        Initializes ``Fmult``.

        Parameters:
            width: Width for sampling spontaneous fission.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if width is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[FmultKeyword] = FmultKeyword.WIDTH
        self.value: Final[types.McnpReal] = width
        self.width: Final[types.McnpReal] = width

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Width`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Width``.

        Returns:
            ``Width`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'width':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Width(value)


class Sfyield(DataOption):
    """
    Represents INP sfyield data card sfyield options.

    ``Sfyield`` implements ``DataOption``.

    Attributes:
        fission_yield: Spontaneous fission yield.
    """

    def __init__(self, fission_yield: types.McnpReal):
        """
        Initializes ``Fmult``.

        Parameters:
            fission_yield: Spontaneous fission yield.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if fission_yield is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[FmultKeyword] = FmultKeyword.SFYIELD
        self.value: Final[types.McnpReal] = fission_yield
        self.fission_yield: Final[types.McnpReal] = fission_yield

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Sfyield`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Sfyield``.

        Returns:
            ``Sfyield`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'sfyield':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Sfyield(value)


class Method(DataOption):
    """
    Represents INP method data card method options.

    ``Method`` implements ``DataOption``.

    Attributes:
        setting: Gaussian sampling algorithm setting.
    """

    def __init__(self, setting: types.McnpInteger):
        """
        Initializes ``Fmult``.

        Parameters:
            setting: Gaussian sampling algorithm setting.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if setting is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[FmultKeyword] = FmultKeyword.METHOD
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


class Shift(DataOption):
    """
    Represents INP shift data card shift options.

    ``Shift`` implements ``DataOption``.

    Attributes:
        setting: Shift method setting.
    """

    def __init__(self, setting: types.McnpInteger):
        """
        Initializes ``Fmult``.

        Parameters:
            setting: Shift method setting.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if setting is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[FmultKeyword] = FmultKeyword.SHIFT
        self.value: Final[types.McnpInteger] = setting
        self.setting: Final[types.McnpInteger] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Shift`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Shift``.

        Returns:
            ``Shift`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'shift':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpInteger.from_mcnp(tokens.popl())

        return Shift(value)


class Fmult(Data):
    """
    Represents INP fmult data cards.

    ``Fmult`` implements ``Data``.

    Attributes:
        zaid: Nuclide for which data are entered.
        pairs: Dictionary of options.
    """

    def __init__(self, zaid: types.Zaid, pairs: dict[DataOption]):
        """
        Initializes ``Fmult``.

        Parameters:
            zaid: Nuclide for which data are entered.
            pairs: Dictionary of options.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if zaid is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(zaid))

        if pairs is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(pairs))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.FMULT
        self.parameters: Final[tuple[any]] = tuple([zaid] + [pairs])
        self.zaid: Final[types.Zaid] = zaid
        self.pairs: Final[dict[DataOption]] = pairs
        self.ident: Final[str] = 'fmult'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Fmult`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for fmult data cards.

        Returns:
            ``Fmult`` object.

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
        if mnemonic != 'fmult':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        zaid = types.Zaid.from_mcnp(tokens.popl())
        pairs = {}
        keywords = re.findall(r'sfnu|width|sfyield|method|shift', ' '.join(tokens.deque))
        values = re.split(r'sfnu|width|sfyield|method|shift', ' '.join(tokens.deque))[1:]
        for keyword, value in zip(keywords, values):
            match keyword:
                case 'sfnu':
                    pairs['sfnu'] = Sfnu.from_mcnp(f'{keyword}={value}')
                case 'width':
                    pairs['width'] = Width.from_mcnp(f'{keyword}={value}')
                case 'sfyield':
                    pairs['sfyield'] = Sfyield.from_mcnp(f'{keyword}={value}')
                case 'method':
                    pairs['method'] = Method.from_mcnp(f'{keyword}={value}')
                case 'shift':
                    pairs['shift'] = Shift.from_mcnp(f'{keyword}={value}')

        data = Fmult(zaid, pairs)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Fmult`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Fmult``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()} {self.zaid.to_mcnp()} {" ".join(entry.to_mcnp() for entry in self.pairs.values())}"
        )
