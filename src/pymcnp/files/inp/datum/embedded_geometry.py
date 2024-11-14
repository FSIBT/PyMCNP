from enum import Enum
from typing import Final

from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors
from ...utils import _parser


class EmbeddedGeometryKeyword(str, Enum):
    """
    ``EmbeddedGeometryKeyword`` represents INP embedded geometry
    specification data card option keywords.

    ``EmbeddedGeometryKeyword`` implements INP embedded geometry
    specification data card option keywords as a Python inner class. It
    enumerates MCNP keywords and provides methods for casting strings
    to ``EmbeddedGeometryKeyword`` instances. It represents the INP
    embedded geometry specification data card option keyword syntax
    element, so ``EmbeddedGeometry`` and ``EmbeddedGeometryOption``
    depend on ``EmbeddedGeometryKeyword`` as an enum.
    """

    MATCELL = 'matcell'
    MESHOGEO = 'meshgeo'
    MGEOIN = 'mgeoin'
    MEEOUT = 'meeout'
    MEEIN = 'meein'
    CALC_VOLS = 'calc_vols'
    DEBUG = 'debug'
    FILETYPE = 'filetype'
    GMVFILE = 'gmvfile'
    LENGTH = 'length'
    MCNPUMFILE = 'mcnpumfile'
    OVERLAP = 'overlap'

    @staticmethod
    def from_mcnp(source: str):
        """
        ``from_mcnp`` generates ``EmbeddedGeometryKeyword``
        objects from INP.

        ``from_mcnp`` constructs instances of
        ``EmbeddedGeometryKeyword`` from INP source strings,
        so it operates as a class constructor method and INP parser
        helper function.

        Parameters:
            source: INP for embedded geometry option keyword.

        Returns:
            ``EmbeddedGeometryKeyword`` object.

        Raises:
            MCNPSemanticError: INVALID_DATUM_EMBED_KEYWORD.
        """

        source = _parser.Preprocessor.process_inp(source)

        # Processing Keyword
        if source not in [enum.value for enum in EmbeddedGeometryKeyword]:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_KEYWORD)

        return EmbeddedGeometryKeyword(source)


class EmbeddedGeometryOption:
    """
    ``EmbeddedGeometryOption`` represents INP embedded geometry specification
    data card options.

    ``EmbeddedGeometryOption`` implements INP embedded geometry specification
    data card options. Its attributes store keywords and values, and its
    methods provide entry and endpoints for working with INP embedded
    geometry specification data card options. It represents the generic INP
    embedded geometry specification data card option syntax element, so
    ``EmbeddedGeometry`` depends on ``EmbeddedGeometryOption`` as a genric
    data structre and superclass.

    Attributes:
        keyword: INP embedded geometry specification option keyword.
        value: INP embedded geometry specification option value.
    """

    def __init__(self):
        """Needs to be implemented in subclass."""
        raise NotImplementedError

    @staticmethod
    def from_mcnp(source: str):
        """
        ``from_mcnp`` generates ``EmbeddedGeometryOption`` objects from INP.

        ``from_mcnp`` constructs instances of ``EmbeddedGeometryOption``
        from INP source strings, so it operates as a class constructor
        method and INP parser helper function. Although defined on the
        superclass, it returns ``EmbeddedGeometryOption`` subclasses.

        Parameters:
            source: INP for embedded geometry specification option.

        Returns:
            ``EmbeddedGeometryOption`` object.

        Raises:
            MCNPSemanticError: INVALID_DATUM_EMBED_KEYWORD.
            MCNPSyntaxError: TOOFEW_DATUM_EMBED, TOOLONG_DATUM_EMBED.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            source.split('='),
            errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_EMBED),
        )

        keyword = EmbeddedGeometryKeyword.from_mcnp(tokens.popl())

        match keyword:
            case EmbeddedGeometryKeyword.MATCELL:
                assert False, 'Unimplemented'
            case (
                EmbeddedGeometryKeyword.MESHOGEO
                | EmbeddedGeometryKeyword.MGEOIN
                | EmbeddedGeometryKeyword.MEEOUT
                | EmbeddedGeometryKeyword.MEEIN
                | EmbeddedGeometryKeyword.CALC_VOLS
                | EmbeddedGeometryKeyword.DEBUG
                | EmbeddedGeometryKeyword.FILETYPE
                | EmbeddedGeometryKeyword.GMVFILE
                | EmbeddedGeometryKeyword.MCNPUMFILE
            ):
                value = tokens.popl()
            case EmbeddedGeometryKeyword.LENGTH:
                value = types.McnpReal.from_mcnp(tokens.popl())
            case EmbeddedGeometryKeyword.OVERLAP:
                assert False, 'Unimplemented'
            case _:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_KEYWORD)

        if tokens:
            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_EMBED)

        # select correct subclass
        if keyword is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_KEYWORD)

        match keyword:
            case EmbeddedGeometryKeyword.MATCELL:
                obj = Matcell(keyword, value)  # noqa: F821
            case EmbeddedGeometryKeyword.MESHOGEO:
                obj = Meshgeo(keyword, value)  # noqa: F821
            case EmbeddedGeometryKeyword.MGEOIN:
                obj = Mgeoin(keyword, value)  # noqa: F821
            case EmbeddedGeometryKeyword.MEEOUT:
                obj = Meeout(keyword, value)  # noqa: F821
            case EmbeddedGeometryKeyword.MEEIN:
                obj = Meein(keyword, value)  # noqa: F821
            case EmbeddedGeometryKeyword.CALC_VOLS:
                obj = CalcVols(keyword, value)  # noqa: F821
            case EmbeddedGeometryKeyword.DEBUG:
                obj = Debug(keyword, value)  # noqa: F821
            case EmbeddedGeometryKeyword.FILETYPE:
                obj = Filetype(keyword, value)  # noqa: F821
            case EmbeddedGeometryKeyword.GMVFILE:
                obj = Gmvfile(keyword, value)  # noqa: F821
            case EmbeddedGeometryKeyword.LENGTH:
                obj = Length(keyword, value)  # noqa: F821
            case EmbeddedGeometryKeyword.MCNPUMFILE:
                obj = Mcnpumfile(keyword, value)  # noqa: F821
            case EmbeddedGeometryKeyword.OVERLAP:
                obj = Overlap(keyword, value)  # noqa: F821

        return obj


class Meshgeo(EmbeddedGeometryOption):
    """
    ``Meshgeo`` represents INP meshgeo embedded geometry specification
    options.

    ``Meshgeo`` inherits attributes from ``EmbeddedGeometryOption``. It
    represents the INP meshgeo embedded geometry data card option sytnax
    element.

    Attributes:
        form: Format specification of the embedded mesh input file.
    """

    def __init__(self, form: str):
        """
        ``__init__`` initializes ``Meshgeo``.

        Parameters:
            form: Format specification of the embedded mesh input file.

        Raises:
            MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
        """

        if form is None or form not in {'lnk3dnt', 'abaqus', 'mcnpum'}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

        self.keyword = EmbeddedGeometryKeyword.MESHOGEO
        self.value = form
        self.form = form


class Mgeoin(EmbeddedGeometryOption):
    """
    ``Mgeoin`` represents INP mgeoin embedded geometry specification
    options.

    ``Mgeoin`` inherits attributes from ``EmbeddedGeometryOption``. It
    represents the INP mgeoin embedded geometry data card option sytnax
    element.

    Attributes:
        filename: Name of the input file with mesh description.
    """

    def __init__(self, filename: str):
        """
        ``__init__`` initializes ``Mgeoin``.

        Parameters:
            filename: Name of the input file with mesh description.

        Raises:
            MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
        """

        if filename is None or not filename:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

        self.keyword = EmbeddedGeometryKeyword.MGEOIN
        self.value = filename
        self.filename = filename


class Meeout(EmbeddedGeometryOption):
    """
    ``Meeout`` represents INP meeout embedded geometry specification
    options.

    ``Meeout`` inherits attributes from ``EmbeddedGeometryOption``. It
    represents the INP meeout embedded geometry data card option sytnax
    element.

    Attributes:
        filename: Name assigned to EEOUT, the elemental edit output file.
    """

    def __init__(self, filename: str):
        """
        ``__init__`` initializes ``Meeout``.

        Parameters:
            filename: Name assigned to EEOUT, the elemental edit output file.

        Raises:
            MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
        """

        if filename is None or not filename:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

        self.keyword = EmbeddedGeometryKeyword.MEEOUT
        self.value = filename
        self.filename = filename


class Meein(EmbeddedGeometryOption):
    """
    ``Meein`` represents INP meein embedded geometry specification options.

    ``Meein`` inherits attributes from ``EmbeddedGeometryOption``. It
    represents the INP meein embedded geometry data card option sytnax
    element.

    Attributes:
        filename: Name of the EEOUT results file to read.
    """

    def __init__(self, filename: str):
        """
        ``__init__`` initializes ``Meein``.

        Parameters:
            filename: Name of the EEOUT results file to read.

        Raises:
            MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
        """

        if filename is None or not filename:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

        self.keyword = EmbeddedGeometryKeyword.MEEIN
        self.value = filename
        self.filename = filename


class CalcVols(EmbeddedGeometryOption):
    """
    ``CalcVols`` represents INP calc_vols embedded geometry specification
    options.

    ``CalcVols`` inherits attributes from ``EmbeddedGeometryOption``. It
    represents the INP calc_vols embedded geometry data card option sytnax
    element.

    Attributes:
        yes_no: Inferred geometry volume and masses calculation setting.
    """

    def __init__(self, yes_no: str):
        """
        ``__init__`` initializes ``CalcVols``.

        Parameters:
            yes_no: Inferred geometry volume and masses calculation setting.

        Raises:
            MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
        """

        if yes_no is None or yes_no not in {'yes', 'no'}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

        self.keyword = EmbeddedGeometryKeyword.CALC_VOLS
        self.value = yes_no
        self.yes_no = yes_no


class Debug(EmbeddedGeometryOption):
    """
    ``Debug`` represents INP debug embedded geometry specification options.

    ``Debug`` inherits attributes from ``EmbeddedGeometryOption``. It
    represents the INP debug embedded geometry data card option sytnax
    element.

    Attributes:
        form: Write the embedded geometry parameters to the OUTP file.
    """

    def __init__(self, form: str):
        """
        ``__init__`` initializes ``Debug``.

        Parameters:
            form: Write the embedded geometry parameters to the OUTP file.

        Raises:
            MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
        """

        if form is None or form not in {'echomesh'}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

        self.keyword = EmbeddedGeometryKeyword.DEBUG
        self.value = form
        self.form = form


class Filetype(EmbeddedGeometryOption):
    """
    ``Filetype`` represents INP filetype embedded geometry specification
    options.

    ``Filetype`` inherits attributes from ``EmbeddedGeometryOption``. It
    represents the INP filetype embedded geometry data card option sytnax
    element.

    Attributes:
        filetype: File type for the elemental edit output file.
    """

    def __init__(self, filetype: str):
        """
        ``__init__`` initializes ``Filetype``.

        Parameters:
            filetype: File type for the elemental edit output file.

        Raises:
            MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
        """

        if filetype is None or filetype not in {'ascii', 'binary'}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

        self.keyword = EmbeddedGeometryKeyword.FILETYPE
        self.value = filetype
        self.filetype = filetype


class Gmvfile(EmbeddedGeometryOption):
    """
    ``Gmvfile`` represents INP gmvfile embedded geometry specification
    options.

    ``Gmvfile`` inherits attributes from ``EmbeddedGeometryOption``. It
    represents the INP gmvfile embedded geometry data card option sytnax
    element.

    Attributes:
        filename: Name of the GMV output file.
    """

    def __init__(self, filename: str):
        """
        ``__init__`` initializes ``Gmvfile``.

        Parameters:
            filename: Name of the GMV output file.

        Raises:
            MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
        """

        if filename is None or not filename:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

        self.keyword = EmbeddedGeometryKeyword.GMVFILE
        self.value = filename
        self.filename = filename


class Length(EmbeddedGeometryOption):
    """
    ``Length`` represents INP length embedded geometry specification
    options.

    ``Length`` inherits attributes from ``EmbeddedGeometryOption``. It
    represents the INP length embedded geometry data card option sytnax
    element.

    Attributes:
        factor: Multiplicative conversion factor to centimeters from mesh.
    """

    def __init__(self, factor: types.McnpReal):
        """
        ``__init__`` initializes ``Length``.

        Parameters:
            factor: Multiplicative conversion factor to centimeters from mesh.

        Raises:
            MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
        """

        if factor is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

        self.keyword = EmbeddedGeometryKeyword.LENGTH
        self.value = factor
        self.factor = factor


class Mcnpumfile(EmbeddedGeometryOption):
    """
    ``Mcnpumfile `` represents INP mcnpumfile embedded geometry
    specification options.

    ``Mcnpumfile`` inherits attributes from ``EmbeddedGeometryOption``. It
    represents the INP mcnpumfile embedded geometry data card option sytnax
    element.

    Attributes:
        filename: Name of the MCNPUM output file.
    """

    def __init__(self, filename: str):
        """
        ``__init__`` initializes ``Mcnpumfile``.

        Parameters:
            filename: Name of the MCNPUM output file.

        Raises:
            MCNPSemanticError: INVALID_DATUM_EMBED_VALUE.
        """

        if filename is None or not filename:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_EMBED_VALUE)

        self.keyword = EmbeddedGeometryKeyword.MCNPUMFILE
        self.value = filename
        self.filename = filename


class EmbeddedGeometry(Datum):
    """
    ``EmbeddedGeometry`` represents INP deterministic embedded geometry data
    cards.

    ``EmbeddedGeometry`` inherits attributes from ``Datum``. It represents the
    INP embedded geometry data card syntax element.

    Attributes:
        pairs: Tuple of key-value pairs.
        suffix: Data card suffix.
    """

    def __init__(self, pairs: tuple[EmbeddedGeometryOption], suffix: types.McnpInteger):
        """
        ``__init__`` initializes ``EmbeddedGeometry``.

        Parameters:
            pairs: Tuple of key-value pairs.
            suffix: Data card suffix.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
            MCNPSemanticError: INVALID_DATUM_SUFFIX.
        """

        for parameter in pairs:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        if suffix is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_SUFFIX)

        _card.Card.__init__(self, f'embed{suffix}')
        self.mnemonic = DatumMnemonic.EMBEDDED_GEOMETRY
        self.parameters = pairs
        self.suffix: Final[int] = suffix

        self.pairs = pairs
