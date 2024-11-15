from enum import Enum

from .datum import Datum, DatumMnemonic
from .. import _card
from ...utils import types
from ...utils import errors
from ...utils import _parser


class WeightWindowKeyword(str, Enum):
    """
    ``WeightWindowKeyword`` represents INP deterministic
    weight window data card keywords.

    ``WeightWindowKeyword`` implements INP deterministic
    weight window data card keywords as a Python inner class. It
    enumerates MCNP keywords and provides methods for casting strings
    to ``WeightWindowKeyword`` instances. It represents
    the INP deterministic weight window data card keyword syntax
    element, so ``WeightWindow`` and
    ``WeightWindowOption`` depend on
    ``WeightWindowKeyword`` as an enum.
    """

    POINTS = 'points'
    BLOCK = 'block'
    NGROUP = 'ngroup'
    ISN = 'isn'
    NISO = 'niso'
    MT = 'mt'
    IQUAD = 'iquad'
    FMMIX = 'fmmix'
    NOSOLV = 'nosolv'
    NOEDIT = 'noedit'
    NOGEOD = 'nogeod'
    NOMIX = 'nomix'
    NOASG = 'noasg'
    NOMACR = 'nomacr'
    NOSLNP = 'noslnp'
    NOEDTT = 'noedtt'
    NOADJM = 'noadjm'
    LIB = 'lib'
    LIBNAME = 'libname'
    FISSNEUT = 'fissneut'
    LNG = 'lng'
    BALXS = 'balxs'
    NTICHI = 'ntichi'
    IEVT = 'ievt'
    SCT = 'sct'
    ITH = 'ith'
    TRCOR = 'trcor'
    IBL = 'ibl'
    IBR = 'ibr'
    IBT = 'ibt'
    IBB = 'ibb'
    IBFRNT = 'ibfrnt'
    BIBACK = 'biback'
    EPSI = 'epsi'
    OITM = 'oitm'
    NOSIGF = 'nosigf'
    SRCACC = 'srcacc'
    DIFFSOL = 'diffsol'
    TSASN = 'tsasn'
    TSAEPSI = 'tsaepsi'
    TSAITS = 'tsaits'
    TSABETA = 'tsabeta'
    PTCONV = 'ptconv'
    NORM = 'norm'
    XESCTP = 'xesctp'
    FISSRP = 'fissrp'
    SOURCP = 'sourcp'
    ANGP = 'angp'
    BALP = 'balp'
    RAFLUX = 'raflux'
    RMFLUX = 'rmflux'
    AVATAR = 'avatar'
    ASLEFT = 'asleft'
    ASRITE = 'asrite'
    ASBOTT = 'asbott'
    ASTOP = 'astop'
    ASFRNT = 'asfrnt'
    ASBACK = 'asback'
    MASSED = 'massed'
    PTED = 'pted'
    ZNED = 'zned'
    RZFLUX = 'rzflux'
    RXMFLUX = 'rxmflux'
    EDOUTF = 'edoutf'
    BYVLOP = 'byvlop'
    AJED = 'ajed'
    FLUXONE = 'fluxone'

    @staticmethod
    def from_mcnp(source: str):
        """
        ``from_mcnp`` generates ``WeightWindowKeyword``
        objects from INP.

        ``from_mcnp`` constructs instances of
        ``WeightWindowKeyword`` from INP source strings,
        so it operates as a class constructor method and INP parser
        helper function.

        Parameters:
            source: INP for deterministic weight window keyword.

        Returns:
            ``WeightWindowKeyword`` object.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_KEYWORD.
        """

        source = _parser.Preprocessor.process_inp(source)

        # Processing Keyword
        if source not in [enum.value for enum in WeightWindowKeyword]:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_KEYWORD)

        return WeightWindowKeyword(source)


class WeightWindowOption:
    """
    ``WeightWindowOption`` represents INP deterministic weight
    window data card options.

    ``WeightWindowOption`` implements INP deterministic weight
    window data card options. Its attributes store keywords and values, and
    its methods provide entry and endpoints for working with INP
    deterministic weight window data card options. It represents the
    generic INP deterministic weight window data card option syntax
    element, so ``WeightWindow`` depends on
    ``WeightWindowOption`` as a generic data structure and
    superclass.

    Attributes:
        keyword:  weight window data card option keyword.
        value:  weight window data card option value.
    """

    def __init__(self):
        """Needs to be implmemented by the subclass."""
        raise NotImplementedError

    @staticmethod
    def from_mcnp(source: str):
        """
        ``from_mcnp`` generates ``WeightWindowOption`` objects
        from INP.

        ``from_mcnp`` constructs instances of
        ``WeightWindowOption`` from INP source strings, so it
        operates as a class constructor method and INP parser helper
        function. Although defined on the superclass, it returns
        ``WeightWindowOption`` subclasses.

        Parameters:
            source: INP for deterministic weight window data card option.

        Returns:
            ``WeightWindowOption`` object.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_KEYWORD.
            MCNPSyntaxError: TOOFEW_DATUM_DAWWG, TOOLONG_DATUM_DAWWG.
        """

        source = _parser.Preprocessor.process_inp(source)
        tokens = _parser.Parser(
            source.split('='),
            errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOFEW_DATUM_DAWWG),
        )

        # Processing Keyword
        keyword = WeightWindowKeyword.cast_keyword(tokens.peekl())

        # Processing Values
        match keyword:
            case (
                WeightWindowKeyword.POINTS
                | WeightWindowKeyword.BLOCK
                | WeightWindowKeyword.NGROUP
                | WeightWindowKeyword.ISN
                | WeightWindowKeyword.NISO
                | WeightWindowKeyword.MT
                | WeightWindowKeyword.IQUAD
                | WeightWindowKeyword.FMMIX
                | WeightWindowKeyword.NOSOLV
                | WeightWindowKeyword.NOEDIT
                | WeightWindowKeyword.NOGEOD
                | WeightWindowKeyword.NOMIX
                | WeightWindowKeyword.NOASG
                | WeightWindowKeyword.NOMACR
                | WeightWindowKeyword.NOSLNP
                | WeightWindowKeyword.NOEDTT
                | WeightWindowKeyword.NOADJM
                | WeightWindowKeyword.FISSNEUT
                | WeightWindowKeyword.LNG
                | WeightWindowKeyword.BALXS
                | WeightWindowKeyword.NTICHI
                | WeightWindowKeyword.IEVT
                | WeightWindowKeyword.SCT
                | WeightWindowKeyword.ITH
                | WeightWindowKeyword.TRCOR
                | WeightWindowKeyword.IBL
                | WeightWindowKeyword.IBR
                | WeightWindowKeyword.IBT
                | WeightWindowKeyword.IBB
                | WeightWindowKeyword.IBFRNT
                | WeightWindowKeyword.BIBACK
                | WeightWindowKeyword.OITM
                | WeightWindowKeyword.NOSIGF
                | WeightWindowKeyword.TSASN
                | WeightWindowKeyword.TSAEPSI
                | WeightWindowKeyword.PTCONV
                | WeightWindowKeyword.XESCTP
                | WeightWindowKeyword.FISSRP
                | WeightWindowKeyword.SOURCP
                | WeightWindowKeyword.ANGP
                | WeightWindowKeyword.BALP
                | WeightWindowKeyword.RAFLUX
                | WeightWindowKeyword.RMFLUX
                | WeightWindowKeyword.AVATAR
                | WeightWindowKeyword.ASLEFT
                | WeightWindowKeyword.ASRITE
                | WeightWindowKeyword.ASBOTT
                | WeightWindowKeyword.ASTOP
                | WeightWindowKeyword.ASFRNT
                | WeightWindowKeyword.ASBACK
                | WeightWindowKeyword.MASSED
                | WeightWindowKeyword.PTED
                | WeightWindowKeyword.ZNED
                | WeightWindowKeyword.RZFLUX
                | WeightWindowKeyword.RXMFLUX
                | WeightWindowKeyword.EDOUTF
                | WeightWindowKeyword.BYVLOP
                | WeightWindowKeyword.AJED
                | WeightWindowKeyword.FLUXONE
            ):
                value = types.McnpInteger.from_mcnp(tokens.popl())
            case (
                WeightWindowKeyword.LIB
                | WeightWindowKeyword.LIBNAME
                | WeightWindowKeyword.TRCOR
                | WeightWindowKeyword.SRCACC
                | WeightWindowKeyword.DIFFSOL
            ):
                value = types.McnpReal.from_mcnp(tokens.popl())
            case (
                WeightWindowKeyword.EPSI
                | WeightWindowKeyword.TSAEPSI
                | WeightWindowKeyword.TSAITS
                | WeightWindowKeyword.TSABETA
            ):
                value = tokens.popl()
            case _:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_KEYWORD)

        if tokens:
            raise errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOOLONG_DATUM_DAWWG)

        # create correct subclass
        if keyword is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_KEYWORD)

        match keyword:
            case WeightWindowKeyword.POINTS:
                obj = Points(keyword, value)  # noqa: F821
            case WeightWindowKeyword.XSEC:
                obj = Xsec(keyword, value)  # noqa: F821
            case WeightWindowKeyword.TALLY:
                obj = Tally(keyword, value)  # noqa: F821
            case WeightWindowKeyword.BLOCK:
                obj = Block(keyword, value)  # noqa: F821
            case WeightWindowKeyword.NGROUP:
                obj = Ngroup(keyword, value)  # noqa: F821
            case WeightWindowKeyword.ISN:
                obj = Isn(keyword, value)  # noqa: F821
            case WeightWindowKeyword.NISO:
                obj = Niso(keyword, value)  # noqa: F821
            case WeightWindowKeyword.MT:
                obj = Mt(keyword, value)  # noqa: F821
            case WeightWindowKeyword.IQUAD:
                obj = Iquad(keyword, value)  # noqa: F821
            case WeightWindowKeyword.FMMIX:
                obj = Fmmix(keyword, value)  # noqa: F821
            case WeightWindowKeyword.NOSOLV:
                obj = Nosolv(keyword, value)  # noqa: F821
            case WeightWindowKeyword.NOEDIT:
                obj = Noedit(keyword, value)  # noqa: F821
            case WeightWindowKeyword.NOGEOD:
                obj = Nogeod(keyword, value)  # noqa: F821
            case WeightWindowKeyword.NOMIX:
                obj = Nomix(keyword, value)  # noqa: F821
            case WeightWindowKeyword.NOASG:
                obj = Noasg(keyword, value)  # noqa: F821
            case WeightWindowKeyword.NOMACR:
                obj = Nomacr(keyword, value)  # noqa: F821
            case WeightWindowKeyword.NOSLNP:
                obj = Noslnp(keyword, value)  # noqa: F821
            case WeightWindowKeyword.NOEDTT:
                obj = Noedtt(keyword, value)  # noqa: F821
            case WeightWindowKeyword.NOADJM:
                obj = Noadjm(keyword, value)  # noqa: F821
            case WeightWindowKeyword.LIB:
                obj = Lib(keyword, value)  # noqa: F821
            case WeightWindowKeyword.LIBNAME:
                obj = Libname(keyword, value)  # noqa: F821
            case WeightWindowKeyword.FISSNEUT:
                obj = Fissneut(keyword, value)  # noqa: F821
            case WeightWindowKeyword.LNG:
                obj = Lng(keyword, value)  # noqa: F821
            case WeightWindowKeyword.BALXS:
                obj = Balxs(keyword, value)  # noqa: F821
            case WeightWindowKeyword.NTICHI:
                obj = Ntichi(keyword, value)  # noqa: F821
            case WeightWindowKeyword.IEVT:
                obj = Ievt(keyword, value)  # noqa: F821
            case WeightWindowKeyword.SCT:
                obj = Isct(keyword, value)  # noqa: F821
            case WeightWindowKeyword.ITH:
                obj = Ith(keyword, value)  # noqa: F821
            case WeightWindowKeyword.TRCOR:
                obj = Trcor(keyword, value)  # noqa: F821
            case WeightWindowKeyword.IBL:
                obj = Ibl(keyword, value)  # noqa: F821
            case WeightWindowKeyword.IBR:
                obj = Ibr(keyword, value)  # noqa: F821
            case WeightWindowKeyword.IBT:
                obj = Ibt(keyword, value)  # noqa: F821
            case WeightWindowKeyword.IBB:
                obj = Ibb(keyword, value)  # noqa: F821
            case WeightWindowKeyword.IBFRNT:
                obj = Ibfrnt(keyword, value)  # noqa: F821
            case WeightWindowKeyword.BIBACK:
                obj = Ibback(keyword, value)  # noqa: F821
            case WeightWindowKeyword.EPSI:
                obj = Epsi(keyword, value)  # noqa: F821
            case WeightWindowKeyword.OITM:
                obj = Oitm(keyword, value)  # noqa: F821
            case WeightWindowKeyword.NOSIGF:
                obj = Nosigf(keyword, value)  # noqa: F821
            case WeightWindowKeyword.SRCACC:
                obj = Srcacc(keyword, value)  # noqa: F821
            case WeightWindowKeyword.DIFFSOL:
                obj = Diffsol(keyword, value)  # noqa: F821
            case WeightWindowKeyword.TSASN:
                obj = Tsasn(keyword, value)  # noqa: F821
            case WeightWindowKeyword.TSAEPSI:
                obj = Tsaepsi(keyword, value)  # noqa: F821
            case WeightWindowKeyword.TSAITS:
                obj = Tsaits(keyword, value)  # noqa: F821
            case WeightWindowKeyword.TSABETA:
                obj = Tsabeta(keyword, value)  # noqa: F821
            case WeightWindowKeyword.PTCONV:
                obj = Ptconv(keyword, value)  # noqa: F821
            case WeightWindowKeyword.NORM:
                obj = Norm(keyword, value)  # noqa: F821
            case WeightWindowKeyword.XESCTP:
                obj = Xesctp(keyword, value)  # noqa: F821
            case WeightWindowKeyword.FISSRP:
                obj = Fissrp(keyword, value)  # noqa: F821
            case WeightWindowKeyword.SOURCP:
                obj = Sourcp(keyword, value)  # noqa: F821
            case WeightWindowKeyword.ANGP:
                obj = Angp(keyword, value)  # noqa: F821
            case WeightWindowKeyword.BALP:
                obj = Balp(keyword, value)  # noqa: F821
            case WeightWindowKeyword.RAFLUX:
                obj = Raflux(keyword, value)  # noqa: F821
            case WeightWindowKeyword.RMFLUX:
                obj = Rmflux(keyword, value)  # noqa: F821
            case WeightWindowKeyword.AVATAR:
                obj = Avatar(keyword, value)  # noqa: F821
            case WeightWindowKeyword.ASLEFT:
                obj = Asleft(keyword, value)  # noqa: F821
            case WeightWindowKeyword.ASRITE:
                obj = Asrite(keyword, value)  # noqa: F821
            case WeightWindowKeyword.ASBOTT:
                obj = Asbott(keyword, value)  # noqa: F821
            case WeightWindowKeyword.ASTOP:
                obj = Astop(keyword, value)  # noqa: F821
            case WeightWindowKeyword.ASFRNT:
                obj = Asfrnt(keyword, value)  # noqa: F821
            case WeightWindowKeyword.ASBACK:
                obj = Asback(keyword, value)  # noqa: F821
            case WeightWindowKeyword.MASSED:
                obj = Massed(keyword, value)  # noqa: F821
            case WeightWindowKeyword.PTED:
                obj = Pted(keyword, value)  # noqa: F821
            case WeightWindowKeyword.ZNED:
                obj = Zned(keyword, value)  # noqa: F821
            case WeightWindowKeyword.RZFLUX:
                obj = Rzflux(keyword, value)  # noqa: F821
            case WeightWindowKeyword.RXMFLUX:
                obj = Rzmflux(keyword, value)  # noqa: F821
            case WeightWindowKeyword.EDOUTF:
                obj = Edoutf(keyword, value)  # noqa: F821
            case WeightWindowKeyword.BYVLOP:
                obj = Byvlop(keyword, value)  # noqa: F821
            case WeightWindowKeyword.AJED:
                obj = Ajed(keyword, value)  # noqa: F821
            case WeightWindowKeyword.FLUXONE:
                obj = Fluxone(keyword, value)  # noqa: F821

        return obj


class Points(WeightWindowOption):
    """
    ``Points`` represents INP points deterministic weight window data card
    options.

    ``Points`` inherits attributes from
    ``WeightWindowOption``. It represents the INP points
    deterministic weight window data card option syntax element.

    Attributes:
        point:  weight window data card sample point count.
    """

    def __init__(self, point: types.McnpInteger):
        """
        ``__init__`` initializes ``Points``.

        Parameters:
            point:  weight window data card sample point count.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if point is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.POINTS
        self.value = point
        self.point = point


class Block(WeightWindowOption):
    """
    ``Block`` represents INP block deterministic weight window data card
    options.

    ``Block`` inherits attributes from ``WeightWindowOption``.
    It represents the INP block deterministic weight window data card
    option syntax element.

    Attributes:
        state: PARTISN input file passed value setting.
    """

    def __init__(self, state: types.McnpInteger):
        """
        ``__init__`` initializes ``Block``.

        Parameters:
            state: PARTISN input file passed value setting.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if state is None or state not in {1, 3, 5, 6}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.BLOCK
        self.value = state
        self.state = state


class Ngroup(WeightWindowOption):
    """
    ``Ngroup`` represents INP ngroup deterministic weight window data card
    options.

    ``Ngroup`` inherits attributes from
    ``WeightWindowOption``. It represents the INP ngroup
    deterministic weight window data card option syntax element.

    Attributes:
        energy_group_number: DAWWG energy group count.
    """

    def __init__(self, energy_group_number: types.McnpInteger):
        """
        ``__init__`` initializes ``Ngroup``.

        Parameters:
            energy_group_number: DAWWG energy group count.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if energy_group_number is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.NGROUP
        self.value = energy_group_number
        self.energy_group_number = energy_group_number


class Isn(WeightWindowOption):
    """
    ``Isn`` represents INP isn deterministic weight window data card
    options.

    ``Isn`` inherits attributes from ``WeightWindowOption``.
    It represents the INP isn deterministic weight window data option
    syntax element.

    Attributes:
        sn_order: DAWWG Sn order.
    """

    def __init__(self, sn_order: types.McnpInteger):
        """
        ``__init__`` initializes ``Isn``.

        Parameters:
            sn_order: DAWWG Sn order.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if sn_order is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.ISN
        self.value = sn_order
        self.sn_order = sn_order


class Niso(WeightWindowOption):
    """
    ``Niso`` represents INP niso deterministic weight window data card
    options.

    ``Niso`` inherits attributes from ``WeightWindowOption``.
    It represents the INP niso deterministic weight window data card option
    syntax element.

    Attributes:
        isotopes_number: DAWWG isotopes number.
    """

    def __init__(self, isotopes_number: types.McnpInteger):
        """
        ``__init__`` initializes ``Niso``.

        Parameters:
            isotopes_number: DAWWG isotopes number.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if isotopes_number is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.NISO
        self.value = isotopes_number
        self.isotopes_number = isotopes_number


class Mt(WeightWindowOption):
    """
    ``Mt`` represents INP mt deterministic weight window data card options.

    ``Mt`` inherits attributes from ``WeightWindowOption``.
    It represents the INP mt deterministic weight window data card option
    syntax element.

    Attributes:
        materials_number: DAWWG materials number.
    """

    def __init__(self, materials_number: types.McnpInteger):
        """
        ``__init__`` initializes ``Mt``.

        Parameters:
            materials_number: DAWWG materials number.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if materials_number is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.MT
        self.value = materials_number
        self.materials_number = materials_number


class Iquad(WeightWindowOption):
    """
    ``Iquad`` represents INP iquad deterministic weight window data card
    options.

    ``Iquad`` inherits attributes from ``WeightWindowOption``.
    It represents the INP iquad deterministic weight window data card
    option syntax element.

    Attributes:
        quadrature: DAWWG quadrature.
    """

    def __init__(self, quadrature: types.McnpInteger):
        """
        ``__init__`` initializes ``Iquad``.

        Parameters:
            quadrature: DAWWG quadrature.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if quadrature is None or quadrature not in {1, 3, 4, 5, 6, 7, 8, 9}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.IQUAD
        self.value = quadrature
        self.quadrature = quadrature


class Fmmix(WeightWindowOption):
    """
    ``Fmmix`` represents INP fmmix deterministic weight window data card
    options.

    ``Fmmix`` inherits attributes from ``WeightWindowOption``.
    It represents the INP fmmix deterministic weight window data card
    option sytnax element.

    Attributes:
        state: DAWWG LNK3DNT reading comprehension toggle.
    """

    def __init__(self, state: types.McnpInteger):
        """
        ``__init__`` initializes ``Fmmix``.

        Parameters:
            state: DAWWG LNK3DNT reading comprehension toggle.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if state is None or state not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.FMMIX
        self.value = state
        self.state = state


class Nosolv(WeightWindowOption):
    """
    ``Nosolv`` represents INP nosolv deterministic weight window data card
    options.

    ``Nosolv`` inherits attributes from
    ``WeightWindowOption``. It represents the INP nosolv
    deterministic weight window data card option syntax element

    Attributes:
        state: Suppress solver module setting.
    """

    def __init__(self, state: types.McnpInteger):
        """
        ``__init__`` initializes ``Nosolv``.

        Parameters:
            state: Suppress solver module setting.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if state is None or state not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.NOSOLV
        self.value = state
        self.state = state


class Noedit(WeightWindowOption):
    """
    ``Noedit`` represents INP noedit deterministic weight window data card
    options.

    ``Noedit`` inherits attributes from
    ``WeightWindowOption``. It represents the INP noedit
    deterministic weight window data card option syntax element.

    Attributes:
        state: Suppress edit module setting.
    """

    def __init__(self, state: types.McnpInteger):
        """
        ``__init__`` initializes ``Noedit``.

        Parameters:
            state: Suppress edit module setting.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if state is None or state not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.NOEDIT
        self.value = state
        self.state = state


class Nogeod(WeightWindowOption):
    """
    ``Nogeod`` represents INP nogeod deterministic weight window data card
    options.

    ``Nogeod`` inherits attributes from
    ``WeightWindowOption``. It represents the INP nogeod
    deterministic weight window data card option syntax element.

    Attributes:
        state: Supress writing GEODST file setting.
    """

    def __init__(self, state: types.McnpInteger):
        """
        ``__init__`` initializes ``Nogeod``.

        Parameters:
            state: Supress writing GEODST file setting.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if state is None or state not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.NOGEOD
        self.value = state
        self.state = state


class Nomix(WeightWindowOption):
    """
    ``Nomix`` represents INP nomix deterministic weight window data card
    options.

    ``Nomix`` inherits attributes from ``WeightWindowOption``.
    It represents the INP nomix deterministic weight window data card
    option syntax element.

    Attributes:
        state: Suppress writing mixing file setting.
    """

    def __init__(self, state: types.McnpInteger):
        """
        ``__init__`` initializes ``Nomix``.

        Parameters:
            state: Suppress writing mixing file setting.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if state is None or state not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.NOMIX
        self.value = state
        self.state = state


class Noasg(WeightWindowOption):
    """
    ``Noasg`` represents INP noasg deterministic weight window data card
    options.

    ``Noasg`` inherits attributes from ``WeightWindowOption``.
    It represents the INP noasg deterministic weight window data card
    option syntax element.

    Attributes:
        state: Suppress wirting ASGMAT file seting.
    """

    def __init__(self, state: types.McnpInteger):
        """
        ``__init__`` initializes ``Noasg``.

        Parameters:
            state: Suppress wirting ASGMAT file seting.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if state is None or state not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.NOASG
        self.value = state
        self.state = state


class Nomacr(WeightWindowOption):
    """
    ``Nomacr`` represents INP nomacr deterministic weight window data card
    options.

    ``Nomacr`` inherits attributes from
    ``WeightWindowOption``. It represents the INP nomacr
    deterministic weight window data card option syntax element.

    Attributes:
        state: Suppress writing MACRXS file.
    """

    def __init__(self, state: types.McnpInteger):
        """
        ``__init__`` initializes ``Nomacr``.

        Parameters:
            state: Suppress writing MACRXS file.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if state is None or state not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.NOMACR
        self.value = state
        self.state = state


class Noslnp(WeightWindowOption):
    """
    ``Noslnp`` represents INP noslnp deterministic weight window data card
    options.

    ``Noslnp`` inherits attributes from
    ``WeightWindowOption``. It represents the INP noslnp
    deterministic weight window data card option syntax element.

    Attributes:
        state: Suppress writing SOLINP file setting.
    """

    def __init__(self, state: types.McnpInteger):
        """
        ``__init__`` initializes ``Noslnp``.

        Parameters:
            state: Suppress writing SOLINP file setting.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if state is None or state not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.NOSLNP
        self.value = state
        self.state = state


class Noedtt(WeightWindowOption):
    """
    ``Noedtt`` represents INP noedtt deterministic weight window data card
    options.

    ``Noedtt`` inherits attributes from
    ``WeightWindowOption``. It represents the INP noedtt
    deterministic weight window data card option syntax element.

    Attributes:
        state: Supress writing EDITIT file setting.
    """

    def __init__(self, state: types.McnpInteger):
        """
        ``__init__`` initializes ``Noedtt``.

        Parameters:
            state: Supress writing EDITIT file setting.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if state is None or state not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.NOEDTT
        self.value = state
        self.state = state


class Noadjm(WeightWindowOption):
    """
    ``Noadjm`` represents INP noadjm deterministic weight window data card
    options.

    ``Noadjm`` inherits attributes from
    ``WeightWindowOption``. It represents the INP noadjm
    deterministic weight window data card option syntax element.

    Attributes:
        state: Suppress writing ADJMAC file setting.
    """

    def __init__(self, state: types.McnpInteger):
        """
        ``__init__`` initializes ``Noadjm``.

        Parameters:
            state: Suppress writing ADJMAC file setting.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if state is None or state not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.NOADJM
        self.value = state
        self.state = state


class Lib(WeightWindowOption):
    """
    ``Lib`` represents lib deterministic weight window datacell coptions.

    ``Lib`` inherits attributes from ``WeightWindowOption``.
    It represents the Libents deterministic weight window data cell option
    syntax element.

    Attributes:
        name: Name/Form of corss-seciotn data file.
    """

    def __init__(self, name: str):
        """
        ``__init__`` initializes ``Lib``.

        Parameters:
            name: Name/Form of corss-seciotn data file.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if name is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.LIB
        self.value = name
        self.name = name


class Libname(WeightWindowOption):
    """
    ``Libname`` represents INP libname deterministic weight window data
    card options.

    ``Libname`` inherits attributes from
    ``WeightWindowOption``. It represents the INP libname
    deterministic weight window data card option syntax element.

    Attributes:
        filename: Cross-section file name.
    """

    def __init__(self, filename: str):
        """
        ``__init__`` initializes ``Libname``.

        Parameters:
            filename: Cross-section file name.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if filename is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.LIBNAME
        self.value = filename
        self.filename = filename


class Fissneut(WeightWindowOption):
    """
    ``Fissneut`` represents INP fissneut deterministic weight window data
    card options.

    ``Fissneut`` inherits attributes from
    ``WeightWindowOption``. It represents the INP fissneut
    deterministic weight window data card option syntax element.

    Attributes:
        fission_neutron_flag: Fission neutron flag.
    """

    def __init__(self, fission_neutron_flag: types.McnpInteger):
        """
        ``__init__`` initializes ``Fissneut``.

        Parameters:
            fission_neutron_flag: Fission neutron flag.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if fission_neutron_flag is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.FISSNEUT
        self.value = fission_neutron_flag
        self.fission_neutron_flag = fission_neutron_flag


class Lng(WeightWindowOption):
    """
    ``Lng`` represents lng deterministic weight window datacell coptions.

    ``Lng`` inherits attributes from ``WeightWindowOption``.
    It represents the Lngents deterministic weight window datacell coption
    syntax element.

    Attributes:
        last_neutron_group_number: Number of the last neutron group.
    """

    def __init__(self, last_neutron_group_number: types.McnpInteger):
        """
        ``__init__`` initializes ``Lng``.

        Parameters:
            last_neutron_group_number: Number of the last neutron group.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if last_neutron_group_number is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.LNG
        self.value = last_neutron_group_number
        self.last_neutron_group_number = last_neutron_group_number


class Balxs(WeightWindowOption):
    """
    ``Balxs`` represents INP balxs deterministic weight window data card
    options.

    ``Balxs`` inherits attributes from ``WeightWindowOption``.
    It represents the INP balxs deterministic weight window data card
    option syntax element.

    Attributes:
        cross_section_balance_control: Cross-section balance control.
    """

    def __init__(self, cross_section_balance_control: types.McnpInteger):
        """
        ``__init__`` initializes ``Balxs``.

        Parameters:
            cross_section_balance_control: Cross-section balance control.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if cross_section_balance_control is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.BALXS
        self.value = cross_section_balance_control
        self.cross_section_balance_control = cross_section_balance_control


class Ntichi(WeightWindowOption):
    """
    ``Ntichi`` represents INP ntichi deterministic weight window data card
    options.

    ``Ntichi`` inherits attributes from
    ``WeightWindowOption``. It represents the INP ntichi
    deterministic weight window data card option syntax element.

    Attributes:
        mendf_fission_fraction: MENDF fission fraction to use.
    """

    def __init__(self, mendf_fission_fraction: types.McnpInteger):
        """
        ``__init__`` initializes ``Ntichi``.

        Parameters:
            mendf_fission_fraction: MENDF fission fraction to use.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if mendf_fission_fraction is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.NTICHI
        self.value = mendf_fission_fraction
        self.mendf_fission_fraction = mendf_fission_fraction


class Ievt(WeightWindowOption):
    """
    ``Ievt`` represents INP ievt deterministic weight window data card
    options.

    ``Ievt`` inherits attributes from ``WeightWindowOption``.
    It represents the INP ievt deterministic weight window data card option
    syntax element.

    Attributes:
        calculation_type: Calculation type.
    """

    def __init__(self, calculation_type: types.McnpInteger):
        """
        ``__init__`` initializes ``Ievt``.

        Parameters:
            calculation_type: Calculation type.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if calculation_type is None or calculation_type not in {0, 1, 2, 3, 4}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.IEVT
        self.value = calculation_type
        self.calculation_type = calculation_type


class Isct(WeightWindowOption):
    """
    ``Isct`` represents INP isct deterministic weight window data card
    options.

    ``Isct`` inherits attributes from ``WeightWindowOption``.
    It represents the INP isct deterministic weight window data card option
    syntax element.

    Attributes:
        legendre_order: Legendre order.
    """

    def __init__(self, legendre_order: types.McnpInteger):
        """
        ``__init__`` initializes ``Isct``.

        Parameters:
            legendre_order: Legendre order.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if legendre_order is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.SCT
        self.value = legendre_order
        self.legendre_order = legendre_order


class Ith(WeightWindowOption):
    """
    ``Ith`` represents ith deterministic weight window datacell coptions.

    ``Ith`` inherits attributes from ``WeightWindowOption``.
    It represents the Ithents deterministic weight window datacell coption
    syntax element.

    Attributes:
        calculation_state: Direct or adjoint calculation.
    """

    def __init__(self, calculation_state: types.McnpInteger):
        """
        ``__init__`` initializes ``Ith``.

        Parameters:
            calculation_state: Direct or adjoint calculation.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if calculation_state is None or calculation_state not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.ITH
        self.value = calculation_state
        self.calculation_state = calculation_state


class Trcor(WeightWindowOption):
    """
    ``Trcor`` represents INP trcor deterministic weight window data card
    options.

    ``Trcor`` inherits attributes from ``WeightWindowOption``.
    It represents the INP trcor deterministic weight window data card
    option syntax element.

    Attributes:
        trcor: trcor.
    """

    def __init__(self, trcor: str):
        """
        ``__init__`` initializes ``Trcor``.

        Parameters:
            trcor: trcor.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if trcor is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.TRCOR
        self.value = trcor
        self.trcor = trcor


class Ibl(WeightWindowOption):
    """
    ``Ibl`` represents ibl deterministic weight window datacell coptions.

    ``Ibl`` inherits attributes from ``WeightWindowOption``.
    It represents the Iblents deterministic weight window datacell coption
    syntax element.

    Attributes:
        left_boundary: Left boundary condition.
    """

    def __init__(self, left_boundary: types.McnpInteger):
        """
        ``__init__`` initializes ``Ibl``.

        Parameters:
            left_boundary: Left boundary condition.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if left_boundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.IBL
        self.value = left_boundary
        self.left_boundary = left_boundary


class Ibr(WeightWindowOption):
    """
    ``Ibr`` represents ibr deterministic weight window datacell coptions.

    ``Ibr`` inherits attributes from ``WeightWindowOption``.
    It represents the Ibrents deterministic weight window datacell coption
    syntax element.

    Attributes:
        right_boundary: Right boundary condition.
    """

    def __init__(self, right_boundary: types.McnpInteger):
        """
        ``__init__`` initializes ``Ibr``.

        Parameters:
            right_boundary: Right boundary condition.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if right_boundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.IBR
        self.value = right_boundary
        self.right_boundary = right_boundary


class Ibt(WeightWindowOption):
    """
    ``Ibt`` represents ibt deterministic weight window datacell coptions.

    ``Ibt`` inherits attributes from ``WeightWindowOption``.
    It represents the Ibtents deterministic weight window datacell coption
    syntax element.

    Attributes:
        top_boundary: Top boundary condition.
    """

    def __init__(self, top_boundary: types.McnpInteger):
        """
        ``__init__`` initializes ``Ibt``.

        Parameters:
            top_boundary: Top boundary condition.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if top_boundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.IBT
        self.value = top_boundary
        self.top_boundary = top_boundary


class Ibb(WeightWindowOption):
    """
    ``Ibb`` represents ibb deterministic weight window datacell coptions.

    ``Ibb`` inherits attributes from ``WeightWindowOption``.
    It represents the Ibbents deterministic weight window datacell coption
    syntax element.

    Attributes:
        bottom_boundary: Bottom boundary condition.
    """

    def __init__(self, bottom_boundary: types.McnpInteger):
        """
        ``__init__`` initializes ``Ibb``.

        Parameters:
            bottom_boundary: Bottom boundary condition.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if bottom_boundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.IBB
        self.value = bottom_boundary
        self.bottom_boundary = bottom_boundary


class Ibfrnt(WeightWindowOption):
    """
    ``Ibfrnt`` represents INP ibfrnt deterministic weight window data card
    options.

    ``Ibfrnt`` inherits attributes from
    ``WeightWindowOption``. It represents the INP ibfrnt
    deterministic weight window data card option syntax element.

    Attributes:
        front_boundary: Front boundary condition.
    """

    def __init__(self, front_boundary: types.McnpInteger):
        """
        ``__init__`` initializes ``Ibfrnt``.

        Parameters:
            front_boundary: Front boundary condition.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if front_boundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.IBFRNT
        self.value = front_boundary
        self.front_boundary = front_boundary


class Ibback(WeightWindowOption):
    """
    ``Ibback`` represents INP ibback deterministic weight window data card
    options.

    ``Ibback`` inherits attributes from
    ``WeightWindowOption``. It represents the INP ibback
    deterministic weight window data card option syntax element.

    Attributes:
        back_boundary: Back boundary condition.
    """

    def __init__(self, back_boundary: types.McnpInteger):
        """
        ``__init__`` initializes ``Ibback``.

        Parameters:
            back_boundary: Back boundary condition.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if back_boundary is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.BIBACK
        self.value = back_boundary
        self.back_boundary = back_boundary


class Epsi(WeightWindowOption):
    """
    ``Epsi`` represents INP epsi deterministic weight window data card
    options.

    ``Epsi`` inherits attributes from ``WeightWindowOption``.
    It represents the INP epsi deterministic weight window data card option
    syntax element.

    Attributes:
        Convergence percision: Convergence percision.
    """

    def __init__(self, convergence_percision: types.McnpReal):
        """
        ``__init__`` initializes ``Epsi``.

        Parameters:
            convergence_percision: Convergence percision.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if convergence_percision is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.EPSI
        self.value = convergence_percision
        self.convergence_percision = convergence_percision


class Oitm(WeightWindowOption):
    """
    ``Oitm`` represents INP oitm deterministic weight window data card
    options.

    ``Oitm`` inherits attributes from ``WeightWindowOption``.
    It represents the INP oitm deterministic weight window data card option
    syntax element.

    Attributes:
        maximnum_outer_iteration: Maximum outer iteration count.
    """

    def __init__(self, maximum_outer_iteration: types.McnpInteger):
        """
        ``__init__`` initializes ``Oitm``.

        Parameters:
            maximnum_outer_iteration: Maximum outer iteration count.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if maximum_outer_iteration is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.OITM
        self.value = maximum_outer_iteration
        self.maximum_outer_iteration = maximum_outer_iteration


class Nosigf(WeightWindowOption):
    """
    ``Nosigf`` represents INP nosigf deterministic weight window data card
    options.

    ``Nosigf`` inherits attributes from
    ``WeightWindowOption``. It represents the INP nosigf
    deterministic weight window data card option syntax element.

    Attributes:
        state: Inhibit fission multiplication setting.
    """

    def __init__(self, state: types.McnpInteger):
        """
        ``__init__`` initializes ``Nosigf``.

        Parameters:
            state: Inhibit fission multiplication setting.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if state is None or state not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.NOSIGF
        self.value = state
        self.state = state


class Srcacc(WeightWindowOption):
    """
    ``Srcacc`` represents INP srcacc deterministic weight window data card
    options.

    ``Srcacc`` inherits attributes from
    ``WeightWindowOption``. It represents the INP srcacc
    deterministic weight window data card option syntax element.

    Attributes:
        transport_accelerations: Transport accelerations.
    """

    def __init__(self, transport_accelerations: str):
        """
        ``__init__`` initializes ``Srcacc``.

        Parameters:
            transport_accelerations: Transport accelerations.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if transport_accelerations is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.SRCACC
        self.value = transport_accelerations
        self.transport_accelerations = transport_accelerations


class Diffsol(WeightWindowOption):
    """
    ``Diffsol`` represents INP diffsol deterministic weight window data
    card options.

    ``Diffsol`` inherits attributes from
    ``WeightWindowOption``. It represents the INP diffsol
    deterministic weight window data card option syntax element.

    Attributes:
        diffusion_operator_solver: Diffusion operator solver.
    """

    def __init__(self, diffusion_operator_solver: str):
        """
        ``__init__`` initializes ``Diffsol``.

        Parameters:
            diffusion_operator_solver: Diffusion operator solver.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if diffusion_operator_solver is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.DIFFSOL
        self.value = diffusion_operator_solver
        self.diffusion_operator_solver = diffusion_operator_solver


class Tsasn(WeightWindowOption):
    """
    ``Tsasn`` represents INP tsasn deterministic weight window data card
    options.

    ``Tsasn`` inherits attributes from ``WeightWindowOption``.
    It represents the INP tsasn deterministic weight window data card
    option syntax element.

    Attributes:
        sn_order: Sn order for low order TSA sweeps.
    """

    def __init__(self, sn_order: types.McnpInteger):
        """
        ``__init__`` initializes ``Tsasn``.

        Parameters:
            sn_order: Sn order for low order TSA sweeps.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if sn_order is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.TSASN
        self.value = sn_order
        self.sn_order = sn_order


class Tsaepsi(WeightWindowOption):
    """
    ``Tsaepsi`` represents INP tsaepsi deterministic weight window data
    card options.

    ``Tsaepsi`` inherits attributes from
    ``WeightWindowOption``. It represents the INP tsaepsi
    deterministic weight window data card option syntax element.

    Attributes:
        convergence_criteria: Convergence criteria for TSA sweeps.
    """

    def __init__(self, convergence_criteria: types.McnpReal):
        """
        ``__init__`` initializes ``Tsaepsi``.

        Parameters:
            convergence_criteria: Convergence criteria for TSA sweeps.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if convergence_criteria is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.TSAEPSI
        self.value = convergence_criteria
        self.convergence_criteria = convergence_criteria


class Tsaits(WeightWindowOption):
    """
    ``Tsaits`` represents INP tsaits deterministic weight window data card
    options.

    ``Tsaits`` inherits attributes from
    ``WeightWindowOption``. It represents the INP tsaits
    deterministic weight window data card option syntax element.

    Attributes:
        maximum_tsa_iteration: Maximmum TSA iteration count.
    """

    def __init__(self, maximum_tsa_iteration: types.McnpInteger):
        """
        ``__init__`` initializes ``Tsaits``.

        Parameters:
            maximum_tsa_iteration: Maximmum TSA iteration count.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if maximum_tsa_iteration is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.TSAITS
        self.value = maximum_tsa_iteration
        self.maximum_tsa_iteration = maximum_tsa_iteration


class Tsabeta(WeightWindowOption):
    """
    ``Tsabeta`` represents INP tsabeta deterministic weight window data
    card options.

    ``Tsabeta`` inherits attributes from
    ``WeightWindowOption``. It represents the INP tsabeta
    deterministic weight window data card option syntax element.

    Attributes:
        tsa_scattering_corss_section: Scatting cross-section reduction.
    """

    def __init__(self, tsa_scattering_cross_section: types.McnpReal):
        """
        ``__init__`` initializes ``Tsabeta``.

        Parameters:
            tsa_scattering_cross_section: Scatting cross-section reduction.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if tsa_scattering_cross_section is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.TSABETA
        self.value = tsa_scattering_cross_section
        self.tsa_scattering_cross_section = tsa_scattering_cross_section


class Ptconv(WeightWindowOption):
    """
    ``Ptconv`` represents INP ptconv deterministic weight window data card
    options.

    ``Ptconv`` inherits attributes from
    ``WeightWindowOption``. It represents the INP ptconv
    deterministic weight window data card option syntax element.

    Attributes:
        state: Special criticality convergence scheme.
    """

    def __init__(self, state: types.McnpInteger):
        """
        ``__init__`` initializes ``Ptconv``.

        Parameters:
            state: Special criticality convergence scheme.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if state is None or state not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.PTCONV
        self.value = state
        self.state = state


class Norm(WeightWindowOption):
    """
    ``Norm`` represents INP norm deterministic weight window data card
    options.

    ``Norm`` inherits attributes from ``WeightWindowOption``.
    It represents the INP norm deterministic weight window data card option
    syntax element.

    Attributes:
        norm: Norm.
    """

    def __init__(self, norm: types.McnpReal):
        """
        ``__init__`` initializes ``Norm``.

        Parameters:
            norm: Norm.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if norm is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.NORM
        self.value = norm
        self.norm = norm


class Xesctp(WeightWindowOption):
    """
    ``Xesctp`` represents INP xesctp deterministic weight window data card
    options.

    ``Xesctp`` inherits attributes from
    ``WeightWindowOption``. It represents the INP xesctp
    deterministic weight window data card option syntax element.

    Attributes:
        cross_section_print_flag: Corss-section print flag.
    """

    def __init__(self, cross_section_print_flag: types.McnpInteger):
        """
        ``__init__`` initializes ``Xesctp``.

        Parameters:
            cross_section_print_flag: Corss-section print flag.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if cross_section_print_flag is None or cross_section_print_flag not in {
            0,
            1,
            2,
        }:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.XESCTP
        self.value = cross_section_print_flag
        self.cross_section_print_flag = cross_section_print_flag


class Fissrp(WeightWindowOption):
    """
    ``Fissrp`` represents INP fissrp deterministic weight window data card
    options.

    ``Fissrp`` inherits attributes from
    ``WeightWindowOption``. It represents the INP fissrp
    deterministic weight window data card option syntax element.

    Attributes:
        state: Print fission source rate.
    """

    def __init__(self, state: types.McnpInteger):
        """
        ``__init__`` initializes ``Fissrp``.

        Parameters:
            state: Print fission source rate.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if state is None or state not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.FISSRP
        self.value = state
        self.state = state


class Sourcp(WeightWindowOption):
    """
    ``Sourcp`` represents INP sourcp deterministic weight window data card
    options.

    ``Sourcp`` inherits attributes from
    ``WeightWindowOption``. It represents the INP sourcp
    deterministic weight window data card option syntax element.

    Attributes:
       source_print_flag: Source print flag.
    """

    def __init__(self, source_print_flag: types.McnpInteger):
        """
        ``__init__`` initializes ``Sourcp``.

        Parameters:
            source_print_flag: Source print flag.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if source_print_flag is None or source_print_flag not in {0, 1, 2, 3}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.SOURCP
        self.value = source_print_flag
        self.source_print_flag = source_print_flag


class Angp(WeightWindowOption):
    """
    ``Angp`` represents INP angp deterministic weight window data card
    options.

    ``Angp`` inherits attributes from ``WeightWindowOption``.
    It represents the INP angp deterministic weight window data card option
    syntax element.

    Attributes:
        state: Print angular flux setting.
    """

    def __init__(self, state: types.McnpInteger):
        """
        ``__init__`` initializes ``Angp``.

        Parameters:
            state: Print angular flux setting.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if state is None or state not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.ANGP
        self.value = state
        self.state = state


class Balp(WeightWindowOption):
    """
    ``Balp`` represents INP balp deterministic weight window data card
    options.

    ``Balp`` inherits attributes from ``WeightWindowOption``.
    It represents the INP balp deterministic weight window data card option
    syntax element.

    Attributes:
        state: Print coarse-mesh balance tables setting.
    """

    def __init__(self, state: types.McnpInteger):
        """
        ``__init__`` initializes ``Balp``.

        Parameters:
            state: Print coarse-mesh balance tables setting.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if state is None or state not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.BALP
        self.value = state
        self.state = state


class Raflux(WeightWindowOption):
    """
    ``Raflux`` represents INP raflux deterministic weight window data card
    options.

    ``Raflux`` inherits attributes from
    ``WeightWindowOption``. It represents the INP raflux
    deterministic weight window data card option syntax element.

    Attributes:
        state: Prepare angular flux file setting.
    """

    def __init__(self, state: types.McnpInteger):
        """
        ``__init__`` initializes ``Raflux``.

        Parameters:
            state: Prepare angular flux file setting.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if state is None or state not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.RAFLUX
        self.value = state
        self.state = state


class Rmflux(WeightWindowOption):
    """
    ``Rmflux`` represents INP rmflux deterministic weight window data card
    options.

    ``Rmflux`` inherits attributes from
    ``WeightWindowOption``. It represents the INP rmflux
    deterministic weight window data card option syntax element.

    Attributes:
        state: Prepare flux moments file setting.
    """

    def __init__(self, state: types.McnpInteger):
        """
        ``__init__`` initializes ``Rmflux``.

        Parameters:
            state: Prepare flux moments file setting.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if state is None or state not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.RMFLUX
        self.value = state
        self.state = state


class Avatar(WeightWindowOption):
    """
    ``Avatar`` represents INP avatar deterministic weight window data card
    options.

    ``Avatar`` inherits attributes from
    ``WeightWindowOption``. It represents the INP avatar
    deterministic weight window data card option syntax element.

    Attributes:
        state: Prepare special XMFLUXA file setting.
    """

    def __init__(self, state: types.McnpInteger):
        """
        ``__init__`` initializes ``Avatar``.

        Parameters:
            state: Prepare special XMFLUXA file setting.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if state is None or state not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.AVATAR
        self.value = state
        self.state = state


class Asleft(WeightWindowOption):
    """
    ``Asleft`` represents INP asleft deterministic weight window data card
    options.

    ``Asleft`` inherits attributes from
    ``WeightWindowOption``. It represents the INP asleft
    deterministic weight window data card option syntax element.

    Attributes:
        right_going_flux: Right-going flux at plane i.
    """

    def __init__(self, right_going_flux: types.McnpInteger):
        """
        ``__init__`` initializes ``Asleft``.

        Parameters:
            right_going_flux: Right-going flux at plane i.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if right_going_flux is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.ASLEFT
        self.value = right_going_flux
        self.right_going_flux = right_going_flux


class Asrite(WeightWindowOption):
    """
    ``Asrite`` represents INP asrite deterministic weight window data card
    options.

    ``Asrite`` inherits attributes from
    ``WeightWindowOption``. It represents the INP asrite
    deterministic weight window data card option syntax element.

    Attributes:
        left_going_flux: Left-going flux at plane i.
    """

    def __init__(self, left_going_flux: types.McnpInteger):
        """
        ``__init__`` initializes ``Asrite``.

        Parameters:
            left_going_flux: Left-going flux at plane i.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if left_going_flux is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.ASRITE
        self.value = left_going_flux
        self.left_going_flux = left_going_flux


class Asbott(WeightWindowOption):
    """
    ``Asbott`` represents INP asbott deterministic weight window data card
    options.

    ``Asbott`` inherits attributes from
    ``WeightWindowOption``. It represents the INP asbott
    deterministic weight window data card option syntax element.

    Attributes:
        top_going_flux: Top-going flux at plane j.
    """

    def __init__(self, top_going_flux: types.McnpInteger):
        """
        ``__init__`` initializes ``Asbott``.

        Parameters:
            top_going_flux: Top-going flux at plane j.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if top_going_flux is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.ASBOTT
        self.value = top_going_flux
        self.top_going_flux = top_going_flux


class Astop(WeightWindowOption):
    """
    ``Astop`` represents INP astop deterministic weight window data card
    options.

    ``Astop`` inherits attributes from ``WeightWindowOption``.
    It represents the INP astop deterministic weight window data card
    option syntax element.

    Attributes:
        bottom_going_flux: Bottom-going flux at plane j.
    """

    def __init__(self, bottom_going_flux: types.McnpInteger):
        """
        ``__init__`` initializes ``Astop``.

        Parameters:
            bottom_going_flux: Bottom-going flux at plane j.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if bottom_going_flux is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.ASTOP
        self.value = bottom_going_flux
        self.bottom_going_flux = bottom_going_flux


class Asfrnt(WeightWindowOption):
    """
    ``Asfrnt`` represents INP asfrnt deterministic weight window data card
    options.

    ``Asfrnt`` inherits attributes from
    ``WeightWindowOption``. It represents the INP asfrnt
    deterministic weight window data card option syntax element.

    Attributes:
        back_going_flux: Back-going flux at plane k.
    """

    def __init__(self, back_going_flux: types.McnpInteger):
        """
        ``__init__`` initializes ``Asfrnt``.

        Parameters:
            back_going_flux: Back-going flux at plane k.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if back_going_flux is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.ASFRNT
        self.value = back_going_flux
        self.back_going_flux = back_going_flux


class Asback(WeightWindowOption):
    """
    ``Asback`` represents INP asback deterministic weight window data card
    options.

    ``Asback`` inherits attributes from
    ``WeightWindowOption``. It represents the INP asback
    deterministic weight window data card option syntax element.

    Attributes:
        front_going_flux: Front-going flux at plane k.
    """

    def __init__(self, front_going_flux: types.McnpInteger):
        """
        ``__init__`` initializes ``Asback``.

        Parameters:
            front_going_flux: Front-going flux at plane k.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if front_going_flux is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.ASBACK
        self.value = front_going_flux
        self.front_going_flux = front_going_flux


class Massed(WeightWindowOption):
    """
    ``Massed`` represents INP massed deterministic weight window data card
    options.

    ``Massed`` inherits attributes from
    ``WeightWindowOption``. It represents the INP massed
    deterministic weight window data card option syntax element.

    Attributes:
        state: Mass edits setting.
    """

    def __init__(self, state: types.McnpInteger):
        """
        ``__init__`` initializes ``Massed``.

        Parameters:
            state: Mass edits setting.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if state is None or state not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.MASSED
        self.value = state
        self.state = state


class Pted(WeightWindowOption):
    """
    ``Pted`` represents INP pted deterministic weight window data card
    options.

    ``Pted`` inherits attributes from ``WeightWindowOption``.
    It represents the INP pted deterministic weight window data card option
    syntax element.

    Attributes:
        state: Edits by fine mesh setting.
    """

    def __init__(self, state: types.McnpInteger):
        """
        ``__init__`` initializes ``Pted``.

        Parameters:
            state: Edits by fine mesh setting.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if state is None or state not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.PTED
        self.value = state
        self.state = state


class Zned(WeightWindowOption):
    """
    ``Zned`` represents INP zned deterministic weight window data card
    options.

    ``Zned`` inherits attributes from ``WeightWindowOption``.
    It represents the INP zned deterministic weight window data card option
    syntax element.

    Attributes:
        state: Edits by zone setting.
    """

    def __init__(self, state: types.McnpInteger):
        """
        ``__init__`` initializes ``Zned``.

        Parameters:
            state: Edits by zone setting.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if state is None or state not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.ZNED
        self.value = state
        self.state = state


class Rzflux(WeightWindowOption):
    """
    ``Rzflux`` represents INP rzflux deterministic weight window data card
    options.

    ``Rzflux`` inherits attributes from
    ``WeightWindowOption``. It represents the INP rzflux
    deterministic weight window data card option syntax element.

    Attributes:
        state: Write a-flux file setting.
    """

    def __init__(self, state: types.McnpInteger):
        """
        ``__init__`` initializes ``Rzflux``.

        Parameters:
            state: Write a-flux file setting.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if state is None or state not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.RZFLUX
        self.value = state
        self.state = state


class Rzmflux(WeightWindowOption):
    """
    ``Rzmflux`` represents INP rzmflux deterministic weight window data
    card options.

    ``Rzmflux`` inherits attributes from
    ``WeightWindowOption``. It represents the INP rzmflux
    deterministic weight window data card option syntax element.

    Attributes:
        state: Write b-flux file setting.
    """

    def __init__(self, state: types.McnpInteger):
        """
        ``__init__`` initializes ``Rzmflux``.

        Parameters:
            state: Write b-flux file setting.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if state is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.RXMFLUX
        self.value = state
        self.state = state


class Edoutf(WeightWindowOption):
    """
    ``Edoutf`` represents INP edoutf deterministic weight window data card
    options.

    ``Edoutf`` inherits attributes from
    ``WeightWindowOption``. It represents the INP edoutf
    deterministic weight window data card option syntax element.

    Attributes:
        ascii_output_control: ASCII output file control.
    """

    def __init__(self, ascii_output_control: types.McnpInteger):
        """
        ``__init__`` initializes ``Edoutf``.

        Parameters:
            ascii_output_control: ASCII output file control.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if ascii_output_control is None or not (-3 <= ascii_output_control <= 3):
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.EDOUTF
        self.value = ascii_output_control
        self.ascii_output_control = ascii_output_control


class Byvlop(WeightWindowOption):
    """
    ``Byvlop`` represents INP byvlop deterministic weight window data card
    options.

    ``Byvlop`` inherits attributes from
    ``WeightWindowOption``. It represents the INP byvlop
    deterministic weight window data card option syntax element.

    Attributes:
        state: Printed point reaction rates scaled by mesh volume setting.
    """

    def __init__(self, state: types.McnpInteger):
        """
        ``__init__`` initializes ``Byvlop``.

        Parameters:
            state: Printed point reaction rates scaled by mesh volume setting.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if state is None or state not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.BYVLOP
        self.value = state
        self.state = state


class Ajed(WeightWindowOption):
    """
    ``Ajed`` represents INP ajed deterministic weight window data card
    options.

    ``Ajed`` inherits attributes from ``WeightWindowOption``.
    It represents the INP ajed deterministic weight window data card option
    syntax element.

    Attributes:
        state: Regular and adjoint edit setting.
    """

    def __init__(self, state: types.McnpInteger):
        """
        ``__init__`` initializes ``Ajed``.

        Parameters:
            state: Regular and adjoint edit setting.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if state is None or state not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.AJED
        self.value = state
        self.state = state


class Fluxone(WeightWindowOption):
    """
    ``Fluxone`` represents INP fluxone deterministic weight window data
    card options.

    ``Fluxone`` inherits attributes from
    ``WeightWindowOption``. It represents the INP fluxone
    deterministic weight window data card option syntax element.

    Attributes:
        state: Flux override setting.
    """

    def __init__(self, state: types.McnpInteger):
        """
        ``__init__`` initializes ``Fluxone``.

        Parameters:
            state: Flux override setting.

        Raises:
            MCNPSemanticError: INVALID_DATUM_DAWWG_VALUE.
        """

        if state is None or state not in {0, 1}:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_DAWWG_VALUE)

        self.keyword = WeightWindowKeyword.FLUXONE
        self.value = state
        self.state = state


class WeightWindow(Datum):
    """
    ``WeightWindow`` represents INP deterministic weight window
    data cards.

    ``WeightWindow`` inherits attributes from ``Datum``. It
    represents the INP deterministic weight window data card syntax element.

    Attributes:
        pairs: Tuple of key-value pairs.
    """

    def __init__(self, pairs: tuple[WeightWindowOption]):
        """
        ``__init__`` initializes ``WeightWindow``.

        Parameters:
            pairs: Tuple of key-value pairs.

        Raises:
            MCNPSemanticError: INVALID_DATUM_PARAMETERS.
        """

        for parameter in pairs:
            if parameter is None:
                raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_DATUM_PARAMETERS)

        _card.Card.__init__(self, 'dawwg')
        self.mnemonic = DatumMnemonic.DETERMINISTIC_WEIGHT_WINDOW
        self.parameters = pairs

        self.pairs = pairs
