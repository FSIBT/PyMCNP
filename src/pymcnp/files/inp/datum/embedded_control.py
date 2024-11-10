from enum import Enum

from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors
from ...utils import _parser

from .embedded_geometry import EmbeddedGeometryKeyword


class EmbeddedControlKeyword(str, Enum):
    """
    ``EmbeddedControlKeyword`` represents INP embedded elemental
    edits control data card option keywords.

    ``EmbeddedControlKeyword`` implements INP embedded elemental
    edits control data card option keywords as a Python inner class. It
    enumerates MCNP keywords and provides methods for casting strings
    to ``EmbeddedControlKeyword`` instances. It represents the
    INP embedded elemental edits control data card option keyword
    syntax element, so ``EmbeddedControl`` and
    ``EmbeddedControlOption`` depend on ``EmbeddedControlKeyword`` as
    an enum.
    """

    EMBED = 'embed'
    ENERGY = 'energy'
    TIME = 'time'
    ATOM = 'atom'
    FACTOR = 'factor'
    LIST = 'list'
    MAT = 'mat'
    MTYPE = 'mtype'

    @staticmethod
    def from_mcnp(source: str):
        """
        ``from_mcnp`` generates ``EmbeddedControlKeyword``
        objects from INP.

        ``from_mcnp`` constructs instances of ``EmbeddedControlKeyword``
        from INP source strings, so it operates as a class constructor
        method and INP parser helper function.

        Parameters:
            source: INP for embedded edits control option keyword.

        Returns:
            ``EmbeddedControlKeyword`` object.

        Raises:
            MCNPSemanticError: INVALID_DATUM_EMBEE_KEYWORD.
        """

        source = _parser.Preprocessor.process_inp(source)

        # Processing Keyword
        if source not in [enum.value for enum in EmbeddedControlKeyword]:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_KEYWORD)

        return EmbeddedControlKeyword(source)


class EmbeddedControlOption:
    """
    ``EmbeddedControlOption`` represents INP embedded elemental
    edits control data card options.

    ``EmbeddedControlOption`` implements INP embedded elemental
    edits control data card options. Its attributes store keywords and
    values, and its methods provide entry and endpoints for working wit
    INP embedded elemental edits control data card options. It represents
    the generic INP embedded elemental edits control data card option
    syntax element, so ``EmbeddedControl`` depends on
    ``EmbeddedControlOption`` as a genric data structre and superclass.

    Attributes:
        keyword: INP embedded elemental control  option keyword.
        value: INP embedded elemental control option value.
    """

    def __init__(self, keyword: EmbeddedControlKeyword, value: any):
        """
        ``__init__`` initializes ``EmbeddedControlOption``.

        Parameters:
            keyword: Embedded edits control data card option keyword.

        Raises:
            MCNPSemanticError: INVALID_DATUM_EMBEE_KEYWORD.
        """

        if keyword is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_KEYWORD)

        match keyword:
            case EmbeddedControlKeyword.EMBED:
                obj = Embed(keyword, value)  # noqa: F821
            case EmbeddedControlKeyword.ENERGY:
                obj = Energy(keyword, value)  # noqa: F821
            case EmbeddedControlKeyword.TIME:
                obj = Time(keyword, value)  # noqa: F821
            case EmbeddedControlKeyword.ATOM:
                obj = Atom(keyword, value)  # noqa: F821
            case EmbeddedControlKeyword.FACTOR:
                obj = Factor(keyword, value)  # noqa: F821
            case EmbeddedControlKeyword.LIST:
                assert False, 'Unimplemented'
            case EmbeddedControlKeyword.MAT:
                obj = Mat(keyword, value)  # noqa: F821
            case EmbeddedControlKeyword.MTYPE:
                obj = Mtype(keyword, value)  # noqa: F821

        self.__dict__ = obj.__dict__
        self.__class__ = obj.__class__

    @staticmethod
    def from_mcnp(source: str):
        """
        ``from_mcnp`` generates ``EmbeddedControlOption`` objects from INP.

        ``from_mcnp`` constructs instances of ``EmbeddedControlOption``
        from INP source strings, so it operates as a class constructor
        method and INP parser helper function. Although defined on the
        superclass, it returns ``EmbeddedControlOption`` subclasses.

        Parameters:
            source: INP for embedded elemental edits control option.

        Returns:
            ``EmbeddedControlOption`` object.

        Raises:
            MCNPSemanticError: INVALID_DATUM_EMBEE_KEYWORD.
            MCNPSyntaxError: TOOFEW_DATUM_EMBEE, TOOLONG_DATUM_EMBEE.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            source.split('='),
            errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_EMBEE),
        )

        # Processing Keyword
        keyword = EmbeddedGeometryKeyword.from_mcnp(tokens.peekl())

        # Processing Values
        match keyword:
            case EmbeddedGeometryKeyword.EMBED:
                value = types.McnpInteger.from_mcnp(tokens.popl())
            case (
                EmbeddedGeometryKeyword.ENERGY
                | EmbeddedGeometryKeyword.TIME
                | EmbeddedGeometryKeyword.FRACTOR
            ):
                value = types.McnpReal.from_mcnp(tokens.popl())
            case EmbeddedGeometryKeyword.ATOM | EmbeddedGeometryKeyword.MTYPE:
                value = tokens.popl()
            case _:
                errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_KEYWORD)

        if tokens:
            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_EMBEE)

        return EmbeddedControl.EmbeddedControlOption(keyword, value)


class Embed(EmbeddedControlOption):
    """
    ``Embed`` represents INP Embed embedded elemental edits control data
    card options.

    ``Embed`` inherits attributes from ``EmbeddedControlOption``. It
    represents the INP Embed embedded elemental edits control data card
    option syntax element.

    Attributes:
        number: Embedded mesh universe number.
    """

    def __init__(self, number: types.McnpInteger):
        """
        ``__init__`` initializes ``Embed``.

        Parameters:
            number: Embedded mesh universe number.

        Raises:
            MCNPSemanticError: INVALID_DATUM_EMBEE_VALUE.
        """

        if number is None or not (1 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_VALUE)

        self.keyword = EmbeddedControlKeyword.EMBED
        self.value = number
        self.number = number


class Energy(EmbeddedControlOption):
    """
    ``Energy`` represents INP Energy embedded elemental edits control data
    card options.

    ``Energy`` inherits attributes from ``EmbeddedControlOption``. It
    represents the INP Energy embedded elemental edits control data card
    option syntax element.

    Attributes:
        factor: Conversion factor for all energy outputs.
    """

    def __init__(self, factor: types.McnpReal):
        """
        ``__init__`` initializes ``Energy``.

        Parameters:
            factor: Conversion factor for all energy outputs.

        Raises:
            MCNPSemanticError: INVALID_DATUM_EMBEE_VALUE.
        """

        if factor is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_VALUE)

        self.keyword = EmbeddedControlKeyword.ENERGY
        self.value = factor
        self.factor = factor


class Time(EmbeddedControlOption):
    """
    ``Time`` represents INP Time embedded elemental edits control data card
    options.

    ``Time`` inherits attributes from ``EmbeddedControlOption``. It
    represents the INP Time embedded elemental edits control data card
    option syntax element.

    Attributes:
        factor: Conversion factor for all time-related outputs.
    """

    def __init__(self, factor: types.McnpReal):
        """
        ``__init__`` initializes ``Time``.

        Parameters:
            factor: Conversion factor for all time-related outputs.

        Raises:
            MCNPSemanticError: INVALID_DATUM_EMBEE_VALUE.
        """

        if factor is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_VALUE)

        self.keyword = EmbeddedControlKeyword.TIME
        self.value = factor
        self.factor = factor


class Atom(EmbeddedControlOption):
    """
    ``Atom`` represents INP Atom embedded elemental edits control data card
    options.

    ``Atom`` inherits attributes from ``EmbeddedControlOption``. It
    represents the INP Atom embedded elemental edits control data card
    option syntax element.

    Attributes:
        yes_no: Flag to multiply by atom density.
    """

    def __init__(self, yes_no: str):
        """
        ``__init__`` initializes ``Atom``.

        Parameters:
            yes_no: Flag to multiply by atom density.

        Raises:
            MCNPSemanticError: INVALID_DATUM_EMBEE_VALUE.
        """

        if yes_no is None or yes_no not in {'yes', 'no'}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_VALUE)

        self.keyword = EmbeddedControlKeyword.ATOM
        self.value = yes_no
        self.yes_no = yes_no


class Factor(EmbeddedControlOption):
    """
    ``Factor`` represents INP Factor embedded elemental edits control data
    card options.

    ``Factor`` inherits attributes from ``EmbeddedControlOption``. It
    represents the INP Factor embedded elemental edits control data card
    option syntax element.

    Attributes:
        factor: Multiplicative constant.
    """

    def __init__(self, factor: types.McnpReal):
        """
        ``__init__`` initializes ``Factor``.

        Parameters:
            factor: Multiplicative constant.

        Raises:
            MCNPSemanticError: INVALID_DATUM_EMBEE_VALUE.
        """

        if factor is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_VALUE)

        self.keyword = EmbeddedControlKeyword.FACTOR
        self.value = factor
        self.factor = factor


class Mat(EmbeddedControlOption):
    """
    ``Mat`` represents INP Mat embedded elemental edits control data card
    options.

    ``Mat`` inherits attributes from ``EmbeddedControlOption``. It
    represents the INP Mat embedded elemental edits control data card option
    syntax element.

    Attributes:
        number: Material number.
    """

    def __init__(self, number: types.McnpInteger):
        """
        ``__init__`` initializes ``Mat``.

        Parameters:
            number: Material number.

        Raises:
            MCNPSemanticError: INVALID_DATUM_EMBEE_VALUE.
        """

        if number is None or not (0 <= number <= 99_999_999):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_VALUE)

        self.keyword = EmbeddedControlKeyword.MAT
        self.value = number
        self.number = number


class Mtype(EmbeddedControlOption):
    """
    ``Mtype`` represents INP Mtype embedded elemental edits control data
    card options.

    ``Mtype`` inherits attributes from ``EmbeddedControlOption``. It
    represents the INP Mtype embedded elemental edits control data card
    option syntax element.

    Attributes:
        mtype: Multiplier type.
    """

    def __init__(self, mtype: str):
        """
        ``__init__`` initializes ``Mtype``.

        Parameters:
            mtype: Multiplier type.

        Raises:
            MCNPSemanticError: INVALID_DATUM_EMBEE_VALUE.
        """

        if mtype is None or mtype not in {
            'flux',
            'isotopic',
            'population',
            'reaction',
            'source',
            'tracks',
        }:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBEE_VALUE)

        self.keyword = EmbeddedControlKeyword.MTYPE
        self.value = mtype
        self.mtype = mtype


class EmbeddedControl(Datum):
    """
    ``EmbeddedControl`` represents INP embedded elemental edits control
    data cards.

    ``EmbeddedGeometry`` inherits attributes from ``Datum``. It represents the
    INP embedded elemental edits control data card syntax element.

    Attributes:
        pairs: Tuple of key-value pairs.
        suffix: Data card suffix.
        designator: Data card designator.
    """

    def __init__(
        self,
        pairs: tuple[EmbeddedControlOption],
        suffix: types.McnpInteger,
        designator: tuple[types.Designator],
    ):
        """
        ``__init__`` initializes ``EmbeddedControl``.

        Parameters:
            pairs: Tuple of key-value pairs.
            suffix: Data card suffix.
            designator: Data card designator.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
            MCNPSemanticError: INVALID_DATUM_SUFFIX.
            MCNPSemanticError: INVALID_DATUM_DESIGNATOR
        """

        for parameter in pairs:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        for particle in designator:
            if particle is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DESIGNATOR)

        _card.Card.__init__(self, f'embee{suffix}:{designator.to_mcnp()}')
        self.mnemonic = DatumMnemonic.EMBEDDED_CONTROL
        self.parameters = pairs
        self.suffix = suffix
        self.designator = designator

        self.pairs = pairs
