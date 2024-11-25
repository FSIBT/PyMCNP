"""
Contains the ``Sdef`` subclass of ``Data``.
"""

import re
from typing import Final, Union

from ..data import Data
from ..data import DataMnemonic
from ..data import DataOption
from ..data import DataKeyword
from ...utils import types, errors, _parser


class SdefKeyword(DataKeyword):
    """
    Represents INP sdef data card option keywords.

    ``SdefKeyword`` implements ``DataKeyword``.
    """

    CEL = 'cel'
    SUR = 'sur'
    ERG = 'erg'
    TME = 'tme'
    DIR = 'dir'
    VEC = 'vec'
    NRM = 'nrm'
    POS = 'pos'
    RAD = 'rad'
    EXT = 'ext'
    AXS = 'axs'
    X = 'x'
    Y = 'y'
    Z = 'z'
    CCC = 'ccc'
    ARA = 'ara'
    WGT = 'wgt'
    EFF = 'eff'
    PAR = 'par'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SdefKeyword`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``SdefKeyword``.

        Returns:
            ``SdefKeyword`` object.

        Raises:
            McnpError: INVALID_DATUM_KEYWORD.
        """

        source = _parser.Preprocessor.process_inp(source)

        try:
            return SdefKeyword
        except ValueError:
            raise errors.McnpError(errors.McnpCode.UNRECOGNIZED_KEYWORD)


class Cel(DataOption):
    """
    Represents INP cel data card cel options.

    ``Cel`` implements ``DataOption``.

    Attributes:
        number: Cell number.
    """

    def __init__(self, number: types.McnpInteger):
        """
        Initializes ``Sdef``.

        Parameters:
            number: Cell number.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if number is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[SdefKeyword] = SdefKeyword.CEL
        self.value: Final[types.McnpInteger] = number
        self.number: Final[types.McnpInteger] = number

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

        value = types.McnpInteger.from_mcnp(tokens.popl())

        return Cel(value)


class Sur(DataOption):
    """
    Represents INP sur data card sur options.

    ``Sur`` implements ``DataOption``.

    Attributes:
        number: Surface number.
    """

    def __init__(self, number: types.McnpInteger):
        """
        Initializes ``Sdef``.

        Parameters:
            number: Surface number.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if number is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[SdefKeyword] = SdefKeyword.SUR
        self.value: Final[types.McnpInteger] = number
        self.number: Final[types.McnpInteger] = number

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Sur`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Sur``.

        Returns:
            ``Sur`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'sur':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpInteger.from_mcnp(tokens.popl())

        return Sur(value)


class Erg(DataOption):
    """
    Represents INP erg data card erg options.

    ``Erg`` implements ``DataOption``.

    Attributes:
        energy: Kinetic energy.
    """

    def __init__(self, energy: types.McnpReal):
        """
        Initializes ``Sdef``.

        Parameters:
            energy: Kinetic energy.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if energy is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[SdefKeyword] = SdefKeyword.ERG
        self.value: Final[types.McnpReal] = energy
        self.energy: Final[types.McnpReal] = energy

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

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Erg(value)


class Tme(DataOption):
    """
    Represents INP tme data card tme options.

    ``Tme`` implements ``DataOption``.

    Attributes:
        time: Time in shakes.
    """

    def __init__(self, time: Union[types.McnpReal, types.EmbeddedDistributionNumber]):
        """
        Initializes ``Sdef``.

        Parameters:
            time: Time in shakes.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if time is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[SdefKeyword] = SdefKeyword.TME
        self.value: Final[Union[types.McnpReal, types.EmbeddedDistributionNumber]] = time
        self.time: Final[Union[types.McnpReal, types.EmbeddedDistributionNumber]] = time

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Tme`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Tme``.

        Returns:
            ``Tme`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'tme':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        try:
            value = types.McnpReal.from_mcnp(tokens.popl())
        except Exception:
            pass
        try:
            value = types.EmbeddedDistributionNumber.from_mcnp(tokens.popl())
        except Exception:
            pass

        return Tme(value)


class Dir(DataOption):
    """
    Represents INP dir data card dir options.

    ``Dir`` implements ``DataOption``.

    Attributes:
        cosine: Cosine of the angle between VEC and particle.
    """

    def __init__(self, cosine: types.McnpReal):
        """
        Initializes ``Sdef``.

        Parameters:
            cosine: Cosine of the angle between VEC and particle.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if cosine is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[SdefKeyword] = SdefKeyword.DIR
        self.value: Final[types.McnpReal] = cosine
        self.cosine: Final[types.McnpReal] = cosine

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Dir`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Dir``.

        Returns:
            ``Dir`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'dir':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Dir(value)


class Vec(DataOption):
    """
    Represents INP vec data card vec options.

    ``Vec`` implements ``DataOption``.

    Attributes:
        vector: Reference vector for DIR.
    """

    def __init__(self, vector: tuple[types.McnpReal]):
        """
        Initializes ``Sdef``.

        Parameters:
            vector: Reference vector for DIR.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if vector is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in vector:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(vector))

        self.keyword: Final[SdefKeyword] = SdefKeyword.VEC
        self.value: Final[tuple[types.McnpReal]] = vector
        self.vector: Final[tuple[types.McnpReal]] = vector

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Vec`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Vec``.

        Returns:
            ``Vec`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'vec':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tuple([types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return Vec(value)


class Nrm(DataOption):
    """
    Represents INP nrm data card nrm options.

    ``Nrm`` implements ``DataOption``.

    Attributes:
        sign: Sign of the surface normal.
    """

    def __init__(self, sign: types.McnpInteger):
        """
        Initializes ``Sdef``.

        Parameters:
            sign: Sign of the surface normal.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if sign is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[SdefKeyword] = SdefKeyword.NRM
        self.value: Final[types.McnpInteger] = sign
        self.sign: Final[types.McnpInteger] = sign

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Nrm`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Nrm``.

        Returns:
            ``Nrm`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'nrm':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpInteger.from_mcnp(tokens.popl())

        return Nrm(value)


class Pos(DataOption):
    """
    Represents INP pos data card pos options.

    ``Pos`` implements ``DataOption``.

    Attributes:
        vector: Reference point for position sampling in vector notation.
    """

    def __init__(self, vector: tuple[types.McnpReal]):
        """
        Initializes ``Sdef``.

        Parameters:
            vector: Reference point for position sampling in vector notation.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if vector is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in vector:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(vector))

        self.keyword: Final[SdefKeyword] = SdefKeyword.POS
        self.value: Final[tuple[types.McnpReal]] = vector
        self.vector: Final[tuple[types.McnpReal]] = vector

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Pos`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Pos``.

        Returns:
            ``Pos`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'pos':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tuple([types.McnpReal.from_mcnp(tokens.popl()) for _ in range(0, len(tokens))])

        return Pos(value)


class Rad(DataOption):
    """
    Represents INP rad data card rad options.

    ``Rad`` implements ``DataOption``.

    Attributes:
        radial_distance: Radial distance fo the position from POS or AXS.
    """

    def __init__(self, radial_distance: types.McnpReal):
        """
        Initializes ``Sdef``.

        Parameters:
            radial_distance: Radial distance fo the position from POS or AXS.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if radial_distance is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[SdefKeyword] = SdefKeyword.RAD
        self.value: Final[types.McnpReal] = radial_distance
        self.radial_distance: Final[types.McnpReal] = radial_distance

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Rad`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Rad``.

        Returns:
            ``Rad`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'rad':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Rad(value)


class Ext(DataOption):
    """
    Represents INP ext data card ext options.

    ``Ext`` implements ``DataOption``.

    Attributes:
        distance_cosine: Distance for POS along AXS or Cosine of angle from AXS.
    """

    def __init__(self, distance_cosine: types.McnpReal):
        """
        Initializes ``Sdef``.

        Parameters:
            distance_cosine: Distance for POS along AXS or Cosine of angle from AXS.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if distance_cosine is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[SdefKeyword] = SdefKeyword.EXT
        self.value: Final[types.McnpReal] = distance_cosine
        self.distance_cosine: Final[types.McnpReal] = distance_cosine

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

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Ext(value)


class Axs(DataOption):
    """
    Represents INP axs data card axs options.

    ``Axs`` implements ``DataOption``.

    Attributes:
        vector: Reference vector for EXT and RAD.
    """

    def __init__(self, vector: tuple[types.McnpReal]):
        """
        Initializes ``Sdef``.

        Parameters:
            vector: Reference vector for EXT and RAD.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if vector is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)
        for entry in vector:
            if entry is None:
                raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(vector))

        self.keyword: Final[SdefKeyword] = SdefKeyword.AXS
        self.value: Final[tuple[types.McnpReal]] = vector
        self.vector: Final[tuple[types.McnpReal]] = vector

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


class X(DataOption):
    """
    Represents INP x data card x options.

    ``X`` implements ``DataOption``.

    Attributes:
        x_coordinate: X-cordinate of position.
    """

    def __init__(self, x_coordinate: types.McnpReal):
        """
        Initializes ``Sdef``.

        Parameters:
            x_coordinate: X-cordinate of position.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if x_coordinate is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[SdefKeyword] = SdefKeyword.X
        self.value: Final[types.McnpReal] = x_coordinate
        self.x_coordinate: Final[types.McnpReal] = x_coordinate

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``X`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``X``.

        Returns:
            ``X`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'x':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpReal.from_mcnp(tokens.popl())

        return X(value)


class Y(DataOption):
    """
    Represents INP y data card y options.

    ``Y`` implements ``DataOption``.

    Attributes:
        y_coordinate: Y-cordinate of position.
    """

    def __init__(self, y_coordinate: types.McnpReal):
        """
        Initializes ``Sdef``.

        Parameters:
            y_coordinate: Y-cordinate of position.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if y_coordinate is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[SdefKeyword] = SdefKeyword.Y
        self.value: Final[types.McnpReal] = y_coordinate
        self.y_coordinate: Final[types.McnpReal] = y_coordinate

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Y`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Y``.

        Returns:
            ``Y`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'y':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Y(value)


class Z(DataOption):
    """
    Represents INP z data card z options.

    ``Z`` implements ``DataOption``.

    Attributes:
        z_coordinate: Z-cordinate of position.
    """

    def __init__(self, z_coordinate: types.McnpReal):
        """
        Initializes ``Sdef``.

        Parameters:
            z_coordinate: Z-cordinate of position.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if z_coordinate is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[SdefKeyword] = SdefKeyword.Z
        self.value: Final[types.McnpReal] = z_coordinate
        self.z_coordinate: Final[types.McnpReal] = z_coordinate

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Z`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Z``.

        Returns:
            ``Z`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'z':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Z(value)


class Ccc(DataOption):
    """
    Represents INP ccc data card ccc options.

    ``Ccc`` implements ``DataOption``.

    Attributes:
        number: Cookie-cutter cell number.
    """

    def __init__(self, number: types.McnpInteger):
        """
        Initializes ``Sdef``.

        Parameters:
            number: Cookie-cutter cell number.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if number is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[SdefKeyword] = SdefKeyword.CCC
        self.value: Final[types.McnpInteger] = number
        self.number: Final[types.McnpInteger] = number

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Ccc`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Ccc``.

        Returns:
            ``Ccc`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'ccc':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpInteger.from_mcnp(tokens.popl())

        return Ccc(value)


class Ara(DataOption):
    """
    Represents INP ara data card ara options.

    ``Ara`` implements ``DataOption``.

    Attributes:
        area: Area of surface.
    """

    def __init__(self, area: types.McnpReal):
        """
        Initializes ``Sdef``.

        Parameters:
            area: Area of surface.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if area is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[SdefKeyword] = SdefKeyword.ARA
        self.value: Final[types.McnpReal] = area
        self.area: Final[types.McnpReal] = area

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Ara`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Ara``.

        Returns:
            ``Ara`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'ara':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Ara(value)


class Wgt(DataOption):
    """
    Represents INP wgt data card wgt options.

    ``Wgt`` implements ``DataOption``.

    Attributes:
        weight: Particle weight.
    """

    def __init__(self, weight: types.McnpReal):
        """
        Initializes ``Sdef``.

        Parameters:
            weight: Particle weight.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if weight is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[SdefKeyword] = SdefKeyword.WGT
        self.value: Final[types.McnpReal] = weight
        self.weight: Final[types.McnpReal] = weight

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


class Eff(DataOption):
    """
    Represents INP eff data card eff options.

    ``Eff`` implements ``DataOption``.

    Attributes:
        criterion: Rejection efficiency criterion for position sampling.
    """

    def __init__(self, criterion: types.McnpReal):
        """
        Initializes ``Sdef``.

        Parameters:
            criterion: Rejection efficiency criterion for position sampling.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if criterion is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[SdefKeyword] = SdefKeyword.EFF
        self.value: Final[types.McnpReal] = criterion
        self.criterion: Final[types.McnpReal] = criterion

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Eff`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Eff``.

        Returns:
            ``Eff`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'eff':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = types.McnpReal.from_mcnp(tokens.popl())

        return Eff(value)


class Par(DataOption):
    """
    Represents INP par data card par options.

    ``Par`` implements ``DataOption``.

    Attributes:
        kind: Source particle type.
    """

    def __init__(self, kind: str):
        """
        Initializes ``Sdef``.

        Parameters:
            kind: Source particle type.

        Raises:
            McnpError: INVALID_DATUM_VALUE.
        """

        if kind is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS)

        self.keyword: Final[SdefKeyword] = SdefKeyword.PAR
        self.value: Final[str] = kind
        self.kind: Final[str] = kind

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Par`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for ``Par``.

        Returns:
            ``Par`` object.

        Raises:
            McnpError: EXPECTED_TOKEN, UNEXPECTED_TOKEN.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        if tokens.popl() != 'par':
            raise errors.McnpError(errors.McnpCode.EXPECTED_TOKEN)

        value = tokens.popl()

        return Par(value)


class Sdef(Data):
    """
    Represents INP sdef data cards.

    ``Sdef`` implements ``Data``.

    Attributes:
        pairs: Dictionary of options.
    """

    def __init__(self, pairs: dict[DataOption]):
        """
        Initializes ``Sdef``.

        Parameters:
            pairs: Dictionary of options.

        Raises:
            McnpError: INVALID_DATUM_PARAMETERS.
        """

        if pairs is None:
            raise errors.McnpError(errors.McnpCode.INVALID_DATUM_PARAMETERS, str(pairs))

        self.mnemonic: Final[DataMnemonic] = DataMnemonic.SDEF
        self.parameters: Final[tuple[any]] = tuple([pairs])
        self.pairs: Final[dict[DataOption]] = pairs
        self.ident: Final[str] = 'sdef'

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Sdef`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for sdef data cards.

        Returns:
            ``Sdef`` object.

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
        if mnemonic != 'sdef':
            raise errors.McnpError(errors.McnpCode.KEYWORD_DATUM_MNEMONIC)

        tokens.popl()

        pairs = {}
        keywords = re.findall(
            r'cel|sur|erg|tme|dir|vec|nrm|pos|rad|ext|axs|x|y|z|ccc|ara|wgt|eff|par',
            ' '.join(tokens.deque),
        )
        values = re.split(
            r'cel|sur|erg|tme|dir|vec|nrm|pos|rad|ext|axs|x|y|z|ccc|ara|wgt|eff|par',
            ' '.join(tokens.deque),
        )[1:]
        for keyword, value in zip(keywords, values):
            match keyword:
                case 'cel':
                    pairs['cel'] = Cel.from_mcnp(f'{keyword}={value}')
                case 'sur':
                    pairs['sur'] = Sur.from_mcnp(f'{keyword}={value}')
                case 'erg':
                    pairs['erg'] = Erg.from_mcnp(f'{keyword}={value}')
                case 'tme':
                    pairs['tme'] = Tme.from_mcnp(f'{keyword}={value}')
                case 'dir':
                    pairs['dir'] = Dir.from_mcnp(f'{keyword}={value}')
                case 'vec':
                    pairs['vec'] = Vec.from_mcnp(f'{keyword}={value}')
                case 'nrm':
                    pairs['nrm'] = Nrm.from_mcnp(f'{keyword}={value}')
                case 'pos':
                    pairs['pos'] = Pos.from_mcnp(f'{keyword}={value}')
                case 'rad':
                    pairs['rad'] = Rad.from_mcnp(f'{keyword}={value}')
                case 'ext':
                    pairs['ext'] = Ext.from_mcnp(f'{keyword}={value}')
                case 'axs':
                    pairs['axs'] = Axs.from_mcnp(f'{keyword}={value}')
                case 'x':
                    pairs['x'] = X.from_mcnp(f'{keyword}={value}')
                case 'y':
                    pairs['y'] = Y.from_mcnp(f'{keyword}={value}')
                case 'z':
                    pairs['z'] = Z.from_mcnp(f'{keyword}={value}')
                case 'ccc':
                    pairs['ccc'] = Ccc.from_mcnp(f'{keyword}={value}')
                case 'ara':
                    pairs['ara'] = Ara.from_mcnp(f'{keyword}={value}')
                case 'wgt':
                    pairs['wgt'] = Wgt.from_mcnp(f'{keyword}={value}')
                case 'eff':
                    pairs['eff'] = Eff.from_mcnp(f'{keyword}={value}')
                case 'par':
                    pairs['par'] = Par.from_mcnp(f'{keyword}={value}')

        data = Sdef(pairs)
        data.comment = comments

        return data

    def to_mcnp(self) -> str:
        """
        Generates INP from ``Sdef`` objects.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``Sdef``.
        """

        return _parser.Postprocessor.add_continuation_lines(
            f"{self.mnemonic.to_mcnp()} {" ".join(entry.to_mcnp() for entry in self.pairs.values())}"
        )
