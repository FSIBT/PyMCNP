from enum import Enum
import re
from typing import Final

from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors
from ...utils import _parser


class SourceDefinitionKeyword(str, Enum):
    """
    ``SourceDefinitionKeyword`` represents INP source definition data
    card keywords.

    ``SourceDefinitionKeyword`` implements INP source definition data
    card keywords as a Python inner class. It enumerates MCNP keywords
    and provides methods for casting strings to
    ``SourceDefinitionKeyword`` instances. It represents the INP
    source definition data card keyword syntax element, so
    ``SourceDefinition`` and ``SourceDefinitionOption`` depend on
    ``SourceDefinitionKeyword`` as an enum.
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
    TR = 'tr'
    EFF = 'eff'
    PAR = 'par'
    DAT = 'dat'
    LOC = 'loc'
    BEM = 'bem'
    BAP = 'bap'

    def to_mcnp(self) -> str:
        return str(self.value)

    @staticmethod
    def from_mcnp(source: str):
        """
        ``from_mcnp`` generates ``SourceDefinitionKeyword`` objects
        from INP.

        ``from_mcnp`` constructs instances of
        ``SourceDefinitionKeyword`` from INP source strings, so it
        operates as a class constructor method and INP parser helper
        function.

        Parameters:
            source: INP for source definition option keyword.

        Returns:
            ``SourceDefinitionKeyword`` object.

        Raises:
            MCNPSemanticError: INVALID_DATUM_SOURCE_KEYWORD.
        """

        source = _parser.Preprocessor.process_inp(source)

        # Processing Keyword
        if source not in [enum.value for enum in SourceDefinitionKeyword]:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_KEYWORD)

        return SourceDefinitionKeyword(source)


class SourceDefinitionOption:
    """
    ``SourceDefinitionOption`` represents INP source definition data card
    options.

    ``SourceDefinitionOption`` implements INP source definition data card
    options. Its attributes store keywords and values, and its methods
    provide entry and endpoints for working with INP source definition
    data card options. It represents the generic INP source definition
    data card option syntax element, so ``SourceDefinition`` depends on
    ``SourceDefinitionOption`` as a generic data structure and superclass.

    Attributes:
        keyword: Source definition data card option keyword.
        value: Source definition data card option value.
    """

    def __init__(self, keyword: SourceDefinitionKeyword, value: any):
        """
        ``__init__`` initializes ``SourceDefinitionOption``.

        Parameters:
            keyword: Source definition data card option keyword.
            value: Source definition data card option value.

        Raises:
            MCNPSemanticError: INVALID_DATUM_SOURCE_KEYWORD.
        """

        if keyword is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_KEYWORD)

        match keyword:
            case SourceDefinitionKeyword.CEL:
                obj = Cel(value)
            case SourceDefinitionKeyword.SUR:
                obj = Sur(value)
            case SourceDefinitionKeyword.ERG:
                obj = Erg(value)
            case SourceDefinitionKeyword.TME:
                obj = Tme(value)
            case SourceDefinitionKeyword.DIR:
                obj = Dir(value)
            case SourceDefinitionKeyword.VEC:
                obj = Vec(value)
            case SourceDefinitionKeyword.NRM:
                obj = Nrm(value)
            case SourceDefinitionKeyword.POS:
                obj = Pos(value)
            case SourceDefinitionKeyword.RAD:
                obj = Rad(value)
            case SourceDefinitionKeyword.EXT:
                obj = Ext(value)
            case SourceDefinitionKeyword.AXS:
                obj = Axs(value)
            case SourceDefinitionKeyword.X:
                obj = X(value)
            case SourceDefinitionKeyword.Y:
                obj = Y(value)
            case SourceDefinitionKeyword.Z:
                obj = Z(value)
            case SourceDefinitionKeyword.CCC:
                obj = Ccc(value)
            case SourceDefinitionKeyword.ARA:
                obj = Ara(value)
            case SourceDefinitionKeyword.WGT:
                obj = Wgt(value)
            case SourceDefinitionKeyword.TR:
                obj = Tr(value)
            case SourceDefinitionKeyword.EFF:
                obj = Eff(value)
            case SourceDefinitionKeyword.PAR:
                obj = Par(value)
            case SourceDefinitionKeyword.DAT:
                obj = Dat(value)
            case SourceDefinitionKeyword.LOC:
                obj = Loc(value)
            case SourceDefinitionKeyword.BEM:
                obj = Bem(value)
            case SourceDefinitionKeyword.BAP:
                obj = Bap(value)

        self.__dict__ = obj.__dict__
        self.__class__ = obj.__class__

        self.value = value

    @staticmethod
    def from_mcnp(source: str):
        """
        ``from_mcnp`` generates ``SourceDefinitionOption`` objects from
        INP.

        ``from_mcnp`` constructs instances of ``SourceDefinitionOption``
        from INP source strings, so it operates as a class constructor
        method and INP parser helper function. Although defined on the
        superclass, it returns ``SourceDefinitionOption`` subclasses.

        Parameters:
            source: INP for source definition option.

        Returns:
            ``SourceDefinitionOption`` object.

        Raises:
            MCNPSyntaxError: TOOFEW_DATUM_SOURCE.
            MCNPSyntaxError: TOOLONG_DATUM_SOURCE.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            re.split(r'=| ', source),
            errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_SOURCE),
        )

        # Processing Keyword
        keyword = SourceDefinitionKeyword.from_mcnp(tokens.popl())

        # Processing Values
        match keyword:
            case SourceDefinitionKeyword.CEL:
                value = types.McnpInteger.from_mcnp(tokens.popl())
            case SourceDefinitionKeyword.SUR:
                value = types.McnpInteger.from_mcnp(tokens.popl())
            case SourceDefinitionKeyword.ERG:
                if tokens.peekl()[0] == 'd':
                    value = types.DistributionNumber.from_mcnp(tokens.popl())
                else:
                    value = types.McnpReal.from_mcnp(tokens.popl())
            case SourceDefinitionKeyword.TME:
                value = types.McnpReal.from_mcnp(tokens.popl())
            case SourceDefinitionKeyword.DIR:
                if tokens.peekl()[0] == 'd':
                    value = types.DistributionNumber.from_mcnp(tokens.popl())
                else:
                    value = types.McnpReal.from_mcnp(tokens.popl())
            case SourceDefinitionKeyword.VEC:
                value = (
                    types.McnpReal.from_mcnp(tokens.popl()),
                    types.McnpReal.from_mcnp(tokens.popl()),
                    types.McnpReal.from_mcnp(tokens.popl()),
                )
            case SourceDefinitionKeyword.NRM:
                value = types.McnpInteger.from_mcnp(tokens.popl())
            case SourceDefinitionKeyword.POS:
                value = (
                    types.McnpReal.from_mcnp(tokens.popl()),
                    types.McnpReal.from_mcnp(tokens.popl()),
                    types.McnpReal.from_mcnp(tokens.popl()),
                )
            case SourceDefinitionKeyword.RAD:
                if tokens.peekl()[0] == 'd':
                    value = types.DistributionNumber.from_mcnp(tokens.popl())
                else:
                    value = types.McnpReal.from_mcnp(tokens.popl())
            case SourceDefinitionKeyword.EXT:
                value = types.McnpReal.from_mcnp(tokens.popl())
            case SourceDefinitionKeyword.AXS:
                value = (
                    types.McnpReal.from_mcnp(tokens.popl()),
                    types.McnpReal.from_mcnp(tokens.popl()),
                    types.McnpReal.from_mcnp(tokens.popl()),
                )
            case SourceDefinitionKeyword.X:
                value = types.McnpReal.from_mcnp(tokens.popl())
            case SourceDefinitionKeyword.Y:
                value = types.McnpReal.from_mcnp(tokens.popl())
            case SourceDefinitionKeyword.Z:
                value = types.McnpReal.from_mcnp(tokens.popl())
            case SourceDefinitionKeyword.CCC:
                value = types.McnpInteger.from_mcnp(tokens.popl())
            case SourceDefinitionKeyword.ARA:
                value = types.McnpReal.from_mcnp(tokens.popl())
            case SourceDefinitionKeyword.WGT:
                value = types.McnpReal.from_mcnp(tokens.popl())
            case SourceDefinitionKeyword.TR:
                value = types.McnpInteger.from_mcnp(tokens.popl())
            case SourceDefinitionKeyword.EFF:
                value = types.McnpReal.from_mcnp(tokens.popl())
            case SourceDefinitionKeyword.PAR:
                value = tokens.popl()
            case SourceDefinitionKeyword.DAT:
                value = (
                    types.McnpInteger.from_mcnp(tokens.popl()),
                    types.McnpInteger.from_mcnp(tokens.popl()),
                    types.McnpInteger.from_mcnp(tokens.popl()),
                )
            case SourceDefinitionKeyword.LOC:
                value = (
                    types.McnpReal.from_mcnp(tokens.popl()),
                    types.McnpReal.from_mcnp(tokens.popl()),
                    types.McnpReal.from_mcnp(tokens.popl()),
                )
            case SourceDefinitionKeyword.BEM:
                value = (
                    types.McnpReal.from_mcnp(tokens.popl()),
                    types.McnpReal.from_mcnp(tokens.popl()),
                    types.McnpReal.from_mcnp(tokens.popl()),
                )
            case SourceDefinitionKeyword.BAP:
                value = (
                    types.McnpReal.from_mcnp(tokens.popl()),
                    types.McnpReal.from_mcnp(tokens.popl()),
                    types.McnpReal.from_mcnp(tokens.popl()),
                )

        if tokens:
            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_SOURCE)

        return SourceDefinitionOption(keyword, value)

    def to_mcnp(self):
        """
        ``to_mcnp`` generates INP from ``SourceDefinitionOption`` objects.

        ``to_mcnp`` creates INP source string from ``SourceDefinitionOption``
        objects, so it provides an MCNP endpoint.

        Returns:
            INP string for ``SourceDefinitionOption`` object.
        """

        if isinstance(self.value, str):
            return f'{self.keyword.to_mcnp()}={self.value}'

        if isinstance(self.value, tuple):
            value = ' '.join(k.to_mcnp() for k in self.value)
            return f'{self.keyword.to_mcnp()}={value}'

        return f'{self.keyword.to_mcnp()}={self.value.to_mcnp()}'


class Cel(SourceDefinitionOption):
    """
    ``Cel`` represents INP Cel source definition data card
    options.

    ``Cel`` inherits attributes from ``SourceDefinitionOption``. It
    represents the INP Cel source definition data card option syntax element.

    Attributes:
        number: Cell number.
    """

    def __init__(self, number: types.McnpInteger):
        """
        ``__init__`` initializes ``Cel``.

        Parameters:
            number: Cell number.

        Raises:
            MCNPSemanticError: INVALID_DATUM_SOURCE_VALUE.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        self.keyword = SourceDefinitionKeyword.CEL
        self.value = number
        self.number = number


class Sur(SourceDefinitionOption):
    """
    ``Sur`` represents INP Sur source definition data card
    options.

    ``Sur`` inherits attributes from ``SourceDefinitionOption``. It
    represents the INP Sur source definition data card option syntax element.

    Attributes:
        number: Surface number.
    """

    def __init__(self, number: types.McnpInteger):
        """
        ``__init__`` initializes ``Sur``.

        Parameters:
            number: Surface number.

        Raises:
            MCNPSemanticError: INVALID_DATUM_SOURCE_VALUE.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        self.keyword = SourceDefinitionKeyword.SUR
        self.value = number
        self.number = number


class Erg(SourceDefinitionOption):
    """
    ``Erg`` represents INP Erg source definition data card
    options.

    ``Erg`` inherits attributes from ``SourceDefinitionOption``. It
    represents the INP Erg source definition data card option syntax element.

    Attributes:
        energy: Kinetic energy.
    """

    def __init__(self, energy: types.McnpReal | types.DistributionNumber):
        """
        ``__init__`` initializes ``Erg``.

        Parameters:
            energy: Kinetic energy.

        Raises:
            MCNPSemanticError: INVALID_DATUM_SOURCE_VALUE.
        """

        if isinstance(energy, types.McnpReal):
            if energy is None or not (energy >= 0):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)
        else:
            if energy is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        self.keyword = SourceDefinitionKeyword.ERG
        self.value = energy
        self.energy = energy


class Tme(SourceDefinitionOption):
    """
    ``Tme`` represents INP Tme source definition data card
    options.

    ``Tme`` inherits attributes from ``SourceDefinitionOption``. It
    represents the INP Tme source definition data card option syntax element.

    Attributes:
        time: Time.
    """

    def __init__(self, time: types.McnpReal):
        """
        ``__init__`` initializes ``Tme``.

        Parameters:
            _

        Raises:
            MCNPSemanticError: INVALID_DATUM_SOURCE_VALUE.
        """

        if time is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        self.keyword = SourceDefinitionKeyword.TME
        self.value = time
        self.time = time


class Dir(SourceDefinitionOption):
    """
    ``Dir`` represents INP Dir source definition data card
    options.

    ``Dir`` inherits attributes from ``SourceDefinitionOption``. It
    represents the INP Dir source definition data card option syntax element.

    Attributes:
        cosine: Cosine of the angle between VEC and particle's direction.
    """

    def __init__(self, cosine: types.McnpReal | types.DistributionNumber):
        """
        ``__init__`` initializes ``Dir``.

        Parameters:
            cosine: Cosine of the angle between VEC and particle's direction.

        Raises:
            MCNPSemanticError: INVALID_DATUM_SOURCE_VALUE.
        """

        if isinstance(cosine, types.McnpReal):
            if cosine is None or not (-1 <= cosine <= 1):
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)
        else:
            if cosine is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        self.keyword = SourceDefinitionKeyword.DIR
        self.value = cosine
        self.cosine = cosine


class Vec(SourceDefinitionOption):
    """
    ``Vec`` represents INP Vec source definition data card
    options.

    ``Vec`` inherits attributes from ``SourceDefinitionOption``. It
    represents the INP Vec source definition data card option syntax element.

    Attributes:
        vector: Reference vector for DIR in vector notation.
    """

    def __init__(self, vector: tuple[types.McnpReal]):
        """
        ``__init__`` initializes ``Vec``.

        Parameters:
            vector: Reference vector for DIR in vector notation.

        Raises:
            MCNPSemanticError: INVALID_DATUM_SOURCE_VALUE.
        """

        if vector is None or not (len(vector) == 3):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        x, y, z = vector

        if x is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        if y is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        if z is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        self.keyword = SourceDefinitionKeyword.VEC
        self.value = vector
        self.vector = vector


class Nrm(SourceDefinitionOption):
    """
    ``Nrm`` represents INP Nrm source definition data card
    options.

    ``Nrm`` inherits attributes from ``SourceDefinitionOption``. It
    represents the INP Nrm source definition data card option syntax element.

    Attributes:
        sign: Sign of the surface normal.
    """

    def __init__(self, sign: types.McnpInteger):
        """
        ``__init__`` initializes ``Nrm``.

        Parameters:
            sign: Sign of the surface normal.

        Raises:
            MCNPSemanticError: INVALID_DATUM_SOURCE_VALUE.
        """

        if sign is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        self.keyword = SourceDefinitionKeyword.NRM
        self.value = sign
        self.sign = sign


class Pos(SourceDefinitionOption):
    """
    ``Pos`` represents INP Pos source definition data card
    options.

    ``Pos`` inherits attributes from ``SourceDefinitionOption``. It
    represents the INP Pos source definition data card option syntax element.

    Attributes:
        position: Reference point for sampling in vector notation.
    """

    def __init__(self, position: tuple[types.McnpInteger]):
        """
        ``__init__`` initializes ``Pos``.

        Parameters:
            position: Reference point for sampling in vector notation.

        Raises:
            MCNPSemanticError: INVALID_DATUM_SOURCE_VALUE.
        """

        if position is None or not (len(position) == 3):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        x, y, z = position

        if x is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        if y is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        if z is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        self.keyword = SourceDefinitionKeyword.POS
        self.value = position
        self.position = position


class Rad(SourceDefinitionOption):
    """
    ``Rad`` represents INP Rad source definition data card
    options.

    ``Rad`` inherits attributes from ``SourceDefinitionOption``. It
    represents the INP Rad source definition data card option syntax element.

    Attributes:
        distance: Radial distance of the position.
    """

    def __init__(self, distance: types.McnpReal | types.DistributionNumber):
        """
        ``__init__`` initializes ``Rad``.

        Parameters:
            distance: Radial distance of the position.

        Raises:
            MCNPSemanticError: INVALID_DATUM_SOURCE_VALUE.
        """

        if distance is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        self.keyword = SourceDefinitionKeyword.RAD
        self.value = distance
        self.distance = distance


class Ext(SourceDefinitionOption):
    """
    ``Ext`` represents INP Ext source definition data card
    options.

    ``Ext`` inherits attributes from ``SourceDefinitionOption``. It
    represents the INP Ext source definition data card option syntax element.

    Attributes:
         ext: Distance from POS along AXS or cosine of angle from AXS.
    """

    def __init__(self, ext: types.McnpReal):
        """
        ``__init__`` initializes ``Ext``.

        Parameters:
            ext: Distance from POS along AXS or cosine of angle from AXS.

        Raises:
            MCNPSemanticError: INVALID_DATUM_SOURCE_VALUE.
        """

        if ext is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        self.keyword = SourceDefinitionKeyword.EXT
        self.value = ext
        self.ext = ext


class Axs(SourceDefinitionOption):
    """
    ``Axs`` represents INP Axs source definition data card
    options.

    ``Axs`` inherits attributes from ``SourceDefinitionOption``. It
    represents the INP Axs source definition data card option syntax element.

    Attributes:
        vector: Reference vector for EXT and READ.
    """

    def __init__(self, vector: tuple[types.McnpReal]):
        """
        ``__init__`` initializes ``Axs``.

        Parameters:
            vector: Reference vector for EXT and READ.

        Raises:
            MCNPSemanticError: INVALID_DATUM_SOURCE_VALUE.
        """

        if vector is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        self.keyword = SourceDefinitionKeyword.AXS
        self.value = vector
        self.vector = vector


class X(SourceDefinitionOption):
    """
    ``X`` represents INP X source definition data card
    options.

    ``X`` inherits attributes from ``SourceDefinitionOption``. It
    represents the INP X source definition data card option syntax element.

    Attributes:
        x: X-coordinate of position.
    """

    def __init__(self, x: types.McnpReal):
        """
        ``__init__`` initializes ``X``.

        Parameters:
            x: X-coordinate of position.

        Raises:
            MCNPSemanticError: INVALID_DATUM_SOURCE_VALUE.
        """

        if x is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        self.keyword = SourceDefinitionKeyword.X
        self.value = x
        self.x = x


class Y(SourceDefinitionOption):
    """
    ``Y`` represents INP Y source definition data card
    options.

    ``Y`` inherits attributes from ``SourceDefinitionOption``. It
    represents the INP Y source definition data card option syntax element.

    Attributes:
        y: Y-coordinate of position.
    """

    def __init__(self, y: types.McnpReal):
        """
        ``__init__`` initializes ``Y``.

        Parameters:
            y: Y-coordinate of position.

        Raises:
            MCNPSemanticError: INVALID_DATUM_SOURCE_VALUE.
        """

        if y is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        self.keyword = SourceDefinitionKeyword.Y
        self.value = y
        self.y = y


class Z(SourceDefinitionOption):
    """
    ``Z`` represents INP Z source definition data card
    options.

    ``Z`` inherits attributes from ``SourceDefinitionOption``. It
    represents the INP Z source definition data card option syntax element.

    Attributes:
        z: Z-coordinate of position.
    """

    def __init__(self, z: types.McnpReal):
        """
        ``__init__`` initializes ``Z``.

        Parameters:
            y: Y-coordinate of position.

        Raises:
            MCNPSemanticError: INVALID_DATUM_SOURCE_VALUE.
        """

        if z is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        self.keyword = SourceDefinitionKeyword.Z
        self.value = z
        self.z = z


class Ccc(SourceDefinitionOption):
    """
    ``Ccc`` represents INP Ccc source definition data card
    options.

    ``Ccc`` inherits attributes from ``SourceDefinitionOption``. It
    represents the INP Ccc source definition data card option syntax element.

    Attributes:
        number: Cookie-cutter cell number.
    """

    def __init__(self, number: types.McnpInteger):
        """
        ``__init__`` initializes ``Ccc``.

        Parameters:
            number Cookie-cutter cell number.

        Raises:
            MCNPSemanticError: INVALID_DATUM_SOURCE_VALUE.
        """

        if number is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        self.keyword = SourceDefinitionKeyword.CCC
        self.value = number
        self.number = number


class Ara(SourceDefinitionOption):
    """
    ``Ara`` represents INP Ara source definition data card
    options.

    ``Ara`` inherits attributes from ``SourceDefinitionOption``. It
    represents the INP Ara source definition data card option syntax element.

    Attributes:
        area: Area of surface.
    """

    def __init__(self, area: types.McnpReal):
        """
        ``__init__`` initializes ``Ara``.

        Parameters:
            area: Area of surface.

        Raises:
            MCNPSemanticError: INVALID_DATUM_SOURCE_VALUE.
        """

        if area is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        self.keyword = SourceDefinitionKeyword.ARA
        self.value = area
        self.area = area


class Wgt(SourceDefinitionOption):
    """
    ``Wgt`` represents INP Wgt source definition data card
    options.

    ``Wgt`` inherits attributes from ``SourceDefinitionOption``. It
    represents the INP Wgt source definition data card option syntax element.

    Attributes:
        weight: Particle weight.
    """

    def __init__(self, weight: types.McnpReal):
        """
        ``__init__`` initializes ``Wgt``.

        Parameters:
            weight: Particle weight.

        Raises:
            MCNPSemanticError: INVALID_DATUM_SOURCE_VALUE.
        """

        if weight is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        self.keyword = SourceDefinitionKeyword.WGT
        self.value = weight
        self.weight = weight


class Tr(SourceDefinitionOption):
    """
    ``Tr`` represents INP Tr source definition data card
    options.

    ``Tr`` inherits attributes from ``SourceDefinitionOption``. It
    represents the INP Tr source definition data card option syntax element.

    Attributes:
        transformation: Source particle transformation number.
    """

    def __init__(self, transformation: types.McnpInteger):
        """
        ``__init__`` initializes ``Tr``.

        Parameters:
            transformation: Source particle transformation number.

        Raises:
            MCNPSemanticError: INVALID_DATUM_SOURCE_VALUE.
        """

        if transformation is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        self.keyword = SourceDefinitionKeyword.TR
        self.value = transformation
        self.transformation = transformation


class Eff(SourceDefinitionOption):
    """
    ``Eff`` represents INP Eff source definition data card
    options.

    ``Eff`` inherits attributes from ``SourceDefinitionOption``. It
    represents the INP Eff source definition data card option syntax element.

    Attributes:
        criterion: Rejection efficiency criterion for poition sampling.
    """

    def __init__(self, criterion: types.McnpReal):
        """
        ``__init__`` initializes ``Eff``.

        Parameters:
            criterion: Rejection efficiency criterion for poition sampling.

        Raises:
            MCNPSemanticError: INVALID_DATUM_SOURCE_VALUE.
        """

        if criterion is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        self.keyword = SourceDefinitionKeyword.EFF
        self.value = criterion
        self.criterion = criterion


class Par(SourceDefinitionOption):
    """
    ``Par`` represents INP Par source definition data card
    options.

    ``Par`` inherits attributes from ``SourceDefinitionOption``. It
    represents the INP Par source definition data card option syntax element.

    Attributes:
        symbol: Source particle type by symbol or number.
    """

    def __init__(self, symbol: str):
        """
        ``__init__`` initializes ``Par``.

        Parameters:
            symbol: Source particle type by symbol or number.

        Raises:
            MCNPSemanticError: INVALID_DATUM_SOURCE_VALUE.
        """

        if symbol is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        self.keyword = SourceDefinitionKeyword.PAR
        self.value = symbol
        self.symbol = symbol


class Dat(SourceDefinitionOption):
    """
    ``Dat`` represents INP Dat source definition data card
    options.

    ``Dat`` inherits attributes from ``SourceDefinitionOption``. It
    represents the INP Dat source definition data card option syntax element.

    Attributes:
        date: Date to use for cosmic-ray and background sources.
    """

    def __init__(self, date: tuple[types.McnpInteger]):
        """
        ``__init__`` initializes ``Dat``.

        Parameters:
            date: Date to use for cosmic-ray and background sources.

        Raises:
            MCNPSemanticError: INVALID_DATUM_SOURCE_VALUE.
        """

        if date is None or not (len(date) == 3):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        m, d, y = date

        if m is None or not (1 <= m <= 12):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        if d is None or not (1 <= d <= 31):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        if y is None or not (0 <= y <= 9999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        self.keyword = SourceDefinitionKeyword.DAT
        self.value = date
        self.date = date


class Loc(SourceDefinitionOption):
    """
    ``Loc`` represents INP Loc source definition data card
    options.

    ``Loc`` inherits attributes from ``SourceDefinitionOption``. It
    represents the INP Loc source definition data card option syntax element.

    Attributes:
        location: Location of cosmic particle source.
    """

    def __init__(self, location: tuple[types.McnpReal]):
        """
        ``__init__`` initializes ``Loc``.

        Parameters:
            location: Location of cosmic particle source.

        Raises:
            MCNPSemanticError: INVALID_DATUM_SOURCE_VALUE.
        """

        if location is None or not (len(location) == 3):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        lat, lng, alt = location

        if lat is None or not (-90 <= lat <= 90):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        if lng is None or not (-180 <= lng <= 180):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        if alt is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        self.keyword = SourceDefinitionKeyword.LOC
        self.value = location
        self.location = location


class Bem(SourceDefinitionOption):
    """
    ``Bem`` represents INP Bem source definition data card
    options.

    ``Bem`` inherits attributes from ``SourceDefinitionOption``. It
    represents the INP Bem source definition data card option syntax element.

    Attributes:
        parameters: Beam emittance parameters.
    """

    def __init__(self, parameters: tuple[types.McnpReal]):
        """
        ``__init__`` initializes ``Bem``.

        Parameters:
            parameters: Beam emittance parameters.

        Raises:
            MCNPSemanticError: INVALID_DATUM_SOURCE_VALUE.
        """

        if parameters is None or not (len(parameters) == 3):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        exn, eyn, bm1 = parameters

        if exn is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        if eyn is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        if bm1 is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        self.keyword = SourceDefinitionKeyword.BEM
        self.value = parameters
        self.parameters = parameters


class Bap(SourceDefinitionOption):
    """
    ``Bap`` represents INP Bap source definition data card
    options.

    ``Bap`` inherits attributes from ``SourceDefinitionOption``. It
    represents the INP Bap source definition data card option syntax element.

    Attributes:
        parameters: Beam aperture parameters.
    """

    def __init__(self, parameters: tuple[types.McnpReal]):
        """
        ``__init__`` initializes ``Bap``.

        Parameters:
            parameters: Beam aperture parameters.

        Raises:
            MCNPSemanticError: INVALID_DATUM_SOURCE_VALUE.
        """

        if parameters is None or not (len(parameters) == 3):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        ba1, ba2, u = parameters

        if ba1 is None or not (ba1 > 0):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        if ba2 is None or not (ba2 > 0):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        if u is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SOURCE_VALUE)

        self.keyword = SourceDefinitionKeyword.BAP
        self.value = parameters
        self.parameters = parameters


class SourceDefinition(Datum):
    """
    ``SourceDefinition`` represents INP source definition data cards.

    ``SourceDefinition`` inherits attributes from ``Datum``. It represents the
    INP model physics source definition data card syntax element.

    Attributes:
        pairs: Tuple of key-value pairs.
    """

    def __init__(self, pairs: tuple[SourceDefinitionOption]):
        """
        ``__init__`` initializes ``SourceDefinition``.

        Parameters:
            pairs: Tuple of key-value pairs.
        """

        if pairs is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        for pair in pairs:
            if pair is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, 'sdef')
        self.mnemonic: Final[DatumMnemonic] = DatumMnemonic.GENERAL_SOURCE_DEFINITION
        self.parameters: Final[tuple] = pairs

        self.pairs: Final[SourceDefinitionOption] = pairs
