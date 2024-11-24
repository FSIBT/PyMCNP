"""
Contains the ``M`` subclass of ``Data``.
"""

import re
from typing import Final

from ..data import Data
from ..data import DataMnemonic
from ..data import DataEntry
from ..data import DataOption
from ..data import DataKeyword
from ....utils import types, errors, _parser


class MEntry(DataEntry):
    """
    Represents INP m data card entry.

    ``MEntry`` implements ``DataEntry``.

    Attributes:
            zaid: Substance ZAID alias.
            fraction: Substance fraction.
    """

    def __init__(self, zaid: types.Zaid, fraction: types.McnpReal):
        """
        Initializes ``MEntry``.

        Parameters:
                zaid: Substance ZAID alias.
                fraction: Substance fraction.

        Raises:
            McnpError: INVALID_DATA_ENTRY_PARAMETER.
            McnpError: INVALID_DATA_ENTRY_PARAMETER.
        """

        if zaid is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATA_ENTRY_PARAMETER)

        if fraction is None or not (-1 <= fraction <= 1):
            raise errors.McnpError(errors.McnpCode.INVALID_DATA_ENTRY_PARAMETER)

        self.zaid: Final[types.Zaid] = zaid
        self.fraction: Final[types.McnpReal] = fraction

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``MEntry`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``MEntry``.

        Returns:
            ``MEntry`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            source.split(' '), errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source)
        )

        zaid = types.Zaid.from_mcnp(tokens.popl())
        fraction = types.McnpReal.from_mcnp(tokens.popl())

        if tokens:
            raise errors.McnpError(errors.McnpCode.UNEXPECTED_TOKEN)

        return MEntry(zaid, fraction)

    def to_mcnp(self):
        """
        Generates INP from ``MEntry`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``MEntry``.
        """

        return f'{self.zaid.to_mcnp()} {self.fraction.to_mcnp()}'


class MKeyword(DataKeyword):
    """
    Represents INP m data card option keywords.

    ``MKeyword`` implements ``DataKeyword``.
    """

    GAS = 'gas'
    ESTEP = 'estep'
    HSTEP = 'hstep'
    NLIB = 'nlib'
    PLIB = 'plib'
    PNLIB = 'pnlib'
    ELIB = 'elib'
    HLIB = 'hlib'
    ALIB = 'alib'
    SLIB = 'slib'
    TLIB = 'tlib'
    DLIB = 'dlib'
    COND = 'cond'
    REFI = 'refi'
    REFC = 'refc'
    REFS = 'refs'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``MKeyword`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``MKeyword``.

        Returns:
            ``MKeyword`` object.

        Raises:
            McnpError: INVALID_DATUM_KEYWORD.
        """

        source = _parser.Preprocessor.process_inp(source)

        try:
            return MKeyword
        except ValueError:
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD)


class Gas(DataOption):
    """
    Represents INP gas data card gas options.

    ``Gas`` implements ``DataOption``.

    Attributes:
        setting: Flag for density-effect correction to electron stopping power.
    """

    def __init__(self, setting: str):
        """
        Initializes ``M``.

        Parameters:
            setting: Flag for density-effect correction to electron stopping power.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if setting is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[MKeyword] = MKeyword.GAS
        self.value: Final[str] = setting
        self.setting: Final[str] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Gas`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Gas``.

        Returns:
            ``Gas`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'gas':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Gas(value)


class Estep(DataOption):
    """
    Represents INP estep data card estep options.

    ``Estep`` implements ``DataOption``.

    Attributes:
        step: Number of electron sub-step per energy step.
    """

    def __init__(self, step: types.McnpInteger):
        """
        Initializes ``M``.

        Parameters:
            step: Number of electron sub-step per energy step.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if step is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[MKeyword] = MKeyword.ESTEP
        self.value: Final[types.McnpInteger] = step
        self.step: Final[types.McnpInteger] = step

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Estep`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Estep``.

        Returns:
            ``Estep`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'estep':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpInteger.from_mcnp(tokens.popl())

        return Estep(value)


class Hstep(DataOption):
    """
    Represents INP hstep data card hstep options.

    ``Hstep`` implements ``DataOption``.

    Attributes:
        step: Number of proton sub-step per energy step.
    """

    def __init__(self, step: types.McnpInteger):
        """
        Initializes ``M``.

        Parameters:
            step: Number of proton sub-step per energy step.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if step is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[MKeyword] = MKeyword.HSTEP
        self.value: Final[types.McnpInteger] = step
        self.step: Final[types.McnpInteger] = step

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Hstep`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Hstep``.

        Returns:
            ``Hstep`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'hstep':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpInteger.from_mcnp(tokens.popl())

        return Hstep(value)


class Nlib(DataOption):
    """
    Represents INP nlib data card nlib options.

    ``Nlib`` implements ``DataOption``.

    Attributes:
        abx: Default neutron table identifier.
    """

    def __init__(self, abx: str):
        """
        Initializes ``M``.

        Parameters:
            abx: Default neutron table identifier.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if abx is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[MKeyword] = MKeyword.NLIB
        self.value: Final[str] = abx
        self.abx: Final[str] = abx

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Nlib`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Nlib``.

        Returns:
            ``Nlib`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'nlib':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Nlib(value)


class Plib(DataOption):
    """
    Represents INP plib data card plib options.

    ``Plib`` implements ``DataOption``.

    Attributes:
        abx: Default photoatomic table identifier.
    """

    def __init__(self, abx: str):
        """
        Initializes ``M``.

        Parameters:
            abx: Default photoatomic table identifier.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if abx is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[MKeyword] = MKeyword.PLIB
        self.value: Final[str] = abx
        self.abx: Final[str] = abx

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Plib`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Plib``.

        Returns:
            ``Plib`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'plib':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Plib(value)


class Pnlib(DataOption):
    """
    Represents INP pnlib data card pnlib options.

    ``Pnlib`` implements ``DataOption``.

    Attributes:
        abx: Default photonuclear table identifier.
    """

    def __init__(self, abx: str):
        """
        Initializes ``M``.

        Parameters:
            abx: Default photonuclear table identifier.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if abx is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[MKeyword] = MKeyword.PNLIB
        self.value: Final[str] = abx
        self.abx: Final[str] = abx

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Pnlib`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Pnlib``.

        Returns:
            ``Pnlib`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'pnlib':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Pnlib(value)


class Elib(DataOption):
    """
    Represents INP elib data card elib options.

    ``Elib`` implements ``DataOption``.

    Attributes:
        abx: Default electron table identifier.
    """

    def __init__(self, abx: str):
        """
        Initializes ``M``.

        Parameters:
            abx: Default electron table identifier.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if abx is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[MKeyword] = MKeyword.ELIB
        self.value: Final[str] = abx
        self.abx: Final[str] = abx

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Elib`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Elib``.

        Returns:
            ``Elib`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'elib':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Elib(value)


class Hlib(DataOption):
    """
    Represents INP hlib data card hlib options.

    ``Hlib`` implements ``DataOption``.

    Attributes:
        abx: Default proton table identifier.
    """

    def __init__(self, abx: str):
        """
        Initializes ``M``.

        Parameters:
            abx: Default proton table identifier.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if abx is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[MKeyword] = MKeyword.HLIB
        self.value: Final[str] = abx
        self.abx: Final[str] = abx

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Hlib`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Hlib``.

        Returns:
            ``Hlib`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'hlib':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Hlib(value)


class Alib(DataOption):
    """
    Represents INP alib data card alib options.

    ``Alib`` implements ``DataOption``.

    Attributes:
        abx: Default alpha table identifier.
    """

    def __init__(self, abx: str):
        """
        Initializes ``M``.

        Parameters:
            abx: Default alpha table identifier.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if abx is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[MKeyword] = MKeyword.ALIB
        self.value: Final[str] = abx
        self.abx: Final[str] = abx

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Alib`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Alib``.

        Returns:
            ``Alib`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'alib':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Alib(value)


class Slib(DataOption):
    """
    Represents INP slib data card slib options.

    ``Slib`` implements ``DataOption``.

    Attributes:
        abx: Default helion table identifier.
    """

    def __init__(self, abx: str):
        """
        Initializes ``M``.

        Parameters:
            abx: Default helion table identifier.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if abx is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[MKeyword] = MKeyword.SLIB
        self.value: Final[str] = abx
        self.abx: Final[str] = abx

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Slib`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Slib``.

        Returns:
            ``Slib`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'slib':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Slib(value)


class Tlib(DataOption):
    """
    Represents INP tlib data card tlib options.

    ``Tlib`` implements ``DataOption``.

    Attributes:
        abx: Default triton table identifier.
    """

    def __init__(self, abx: str):
        """
        Initializes ``M``.

        Parameters:
            abx: Default triton table identifier.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if abx is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[MKeyword] = MKeyword.TLIB
        self.value: Final[str] = abx
        self.abx: Final[str] = abx

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Tlib`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Tlib``.

        Returns:
            ``Tlib`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'tlib':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Tlib(value)


class Dlib(DataOption):
    """
    Represents INP dlib data card dlib options.

    ``Dlib`` implements ``DataOption``.

    Attributes:
        abx: Default deuteron table identifier.
    """

    def __init__(self, abx: str):
        """
        Initializes ``M``.

        Parameters:
            abx: Default deuteron table identifier.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if abx is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[MKeyword] = MKeyword.DLIB
        self.value: Final[str] = abx
        self.abx: Final[str] = abx

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Dlib`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Dlib``.

        Returns:
            ``Dlib`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'dlib':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Dlib(value)


class Cond(DataOption):
    """
    Represents INP cond data card cond options.

    ``Cond`` implements ``DataOption``.

    Attributes:
        setting: Conduction state for EL03 electron-transport evaluation.
    """

    def __init__(self, setting: types.McnpReal):
        """
        Initializes ``M``.

        Parameters:
            setting: Conduction state for EL03 electron-transport evaluation.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if setting is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[MKeyword] = MKeyword.COND
        self.value: Final[types.McnpReal] = setting
        self.setting: Final[types.McnpReal] = setting

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Cond`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Cond``.

        Returns:
            ``Cond`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'cond':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Cond(value)


class Refi(DataOption):
    """
    Represents INP refi data card refi options.

    ``Refi`` implements ``DataOption``.

    Attributes:
        refractive_index: Refractive index constant.
    """

    def __init__(self, refractive_index: types.McnpReal):
        """
        Initializes ``M``.

        Parameters:
            refractive_index: Refractive index constant.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if refractive_index is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[MKeyword] = MKeyword.REFI
        self.value: Final[types.McnpReal] = refractive_index
        self.refractive_index: Final[types.McnpReal] = refractive_index

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Refi`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Refi``.

        Returns:
            ``Refi`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'refi':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Refi(value)


class Refc(DataOption):
    """
    Represents INP refc data card refc options.

    ``Refc`` implements ``DataOption``.

    Attributes:
        coefficents: Cauchy coefficents.
    """

    def __init__(self, coefficents: tuple[types.McnpReal]):
        """
        Initializes ``M``.

        Parameters:
            coefficents: Cauchy coefficents.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if coefficents is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in coefficents:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(coefficents))

        self.keyword: Final[MKeyword] = MKeyword.REFC
        self.value: Final[tuple[types.McnpReal]] = coefficents
        self.coefficents: Final[tuple[types.McnpReal]] = coefficents

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Refc`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Refc``.

        Returns:
            ``Refc`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'refc':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tuple([types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return Refc(value)


class Refs(DataOption):
    """
    Represents INP refs data card refs options.

    ``Refs`` implements ``DataOption``.

    Attributes:
        coefficents: Sellmeier coefficents.
    """

    def __init__(self, coefficents: tuple[types.McnpReal]):
        """
        Initializes ``M``.

        Parameters:
            coefficents: Sellmeier coefficents.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if coefficents is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in coefficents:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(coefficents))

        self.keyword: Final[MKeyword] = MKeyword.REFS
        self.value: Final[tuple[types.McnpReal]] = coefficents
        self.coefficents: Final[tuple[types.McnpReal]] = coefficents

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Refs`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Refs``.

        Returns:
            ``Refs`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'refs':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tuple([types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return Refs(value)


class M(Data):
    """
    Represents INP m data cards.

    ``M`` implements ``Data``.

    Attributes:
        substances: Tuple of material constituents.
        suffix: Data card suffix..
        pairs: Dictionary of options.
    """

    def __init__(
        self, substances: tuple[MEntry], suffix: types.McnpInteger, pairs: dict[DataOption]
    ):
        """
        Initializes ``M``.

        Parameters:
            substances: Tuple of material constituents.
            suffix: Data card suffix..
            pairs: Dictionary of options.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if substances is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(substances))

        for entry in substances:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(substances))

        if suffix is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(suffix))

        if pairs is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(pairs))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.M
        self.parameters: Final[tuple[any]] = tuple(list(substances) + [suffix] + [pairs])
        self.substances: Final[tuple[MEntry]] = substances
        self.suffix: Final[types.McnpInteger] = suffix
        self.pairs: Final[dict[DataOption]] = pairs
        self.ident: Final[str] = f'm{self.suffix}'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``M`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for m data cards.

        Returns:
            ``M`` object.

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
        if mnemonic != 'm':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        suffix = types.McnpInteger.from_mcnp(tokens.popl()[1:])

        substances = [
            MEntry.from_mcnp(' '.join([tokens.popl() for __ in range(0, 2)]))
            for _ in range(0, len(tokens), 2)
        ]
        suffix = types.McnpInteger.from_mcnp(tokens.popl())
        pairs = {}
        keywords = re.findall(
            r'gas|estep|hstep|nlib|plib|pnlib|elib|hlib|alib|slib|tlib|dlib|cond|refi|refc|refs',
            ' '.join(tokens.deque),
        )
        values = re.split(
            r'gas|estep|hstep|nlib|plib|pnlib|elib|hlib|alib|slib|tlib|dlib|cond|refi|refc|refs',
            ' '.join(tokens.deque),
        )[1:]
        for keyword, value in zip(keywords, values):
            match keyword:
                case 'gas':
                    pairs['gas'] = Gas.from_mcnp(f'{keyword}={value}')
                case 'estep':
                    pairs['estep'] = Estep.from_mcnp(f'{keyword}={value}')
                case 'hstep':
                    pairs['hstep'] = Hstep.from_mcnp(f'{keyword}={value}')
                case 'nlib':
                    pairs['nlib'] = Nlib.from_mcnp(f'{keyword}={value}')
                case 'plib':
                    pairs['plib'] = Plib.from_mcnp(f'{keyword}={value}')
                case 'pnlib':
                    pairs['pnlib'] = Pnlib.from_mcnp(f'{keyword}={value}')
                case 'elib':
                    pairs['elib'] = Elib.from_mcnp(f'{keyword}={value}')
                case 'hlib':
                    pairs['hlib'] = Hlib.from_mcnp(f'{keyword}={value}')
                case 'alib':
                    pairs['alib'] = Alib.from_mcnp(f'{keyword}={value}')
                case 'slib':
                    pairs['slib'] = Slib.from_mcnp(f'{keyword}={value}')
                case 'tlib':
                    pairs['tlib'] = Tlib.from_mcnp(f'{keyword}={value}')
                case 'dlib':
                    pairs['dlib'] = Dlib.from_mcnp(f'{keyword}={value}')
                case 'cond':
                    pairs['cond'] = Cond.from_mcnp(f'{keyword}={value}')
                case 'refi':
                    pairs['refi'] = Refi.from_mcnp(f'{keyword}={value}')
                case 'refc':
                    pairs['refc'] = Refc.from_mcnp(f'{keyword}={value}')
                case 'refs':
                    pairs['refs'] = Refs.from_mcnp(f'{keyword}={value}')

        data = M(substances, suffix, pairs)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``M`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``M``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()}{self.suffix.to_mcnp()} {" ".join(entry.to_mcnp() for entry in self.substances)} {self.suffix.to_mcnp()} {" ".join(entry.to_mcnp() for entry in self.pairs.values())}"
        )
