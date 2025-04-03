import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Phys_2(DataOption_, keyword='phys:e'):
    """
    Represents INP phys_2 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'emax': types.RealOrJump,
        'ides': types.IntegerOrJump,
        'iphot': types.IntegerOrJump,
        'ibad': types.IntegerOrJump,
        'istrg': types.IntegerOrJump,
        'bnum': types.RealOrJump,
        'xnum': types.RealOrJump,
        'rnok': types.IntegerOrJump,
        'enum': types.IntegerOrJump,
        'numb': types.IntegerOrJump,
        'i_mcs_model': types.IntegerOrJump,
        'efac': types.RealOrJump,
        'electron_method_boundary': types.RealOrJump,
        'ckvnum': types.RealOrJump,
    }

    _REGEX = re.compile(
        rf'\Aphys:e( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        emax: types.RealOrJump,
        ides: types.IntegerOrJump,
        iphot: types.IntegerOrJump,
        ibad: types.IntegerOrJump,
        istrg: types.IntegerOrJump,
        bnum: types.RealOrJump,
        xnum: types.RealOrJump,
        rnok: types.IntegerOrJump,
        enum: types.IntegerOrJump,
        numb: types.IntegerOrJump,
        i_mcs_model: types.IntegerOrJump,
        efac: types.RealOrJump,
        electron_method_boundary: types.RealOrJump,
        ckvnum: types.RealOrJump,
    ):
        """
        Initializes ``Phys_2``.

        Parameters:
            emax: Upper limit for electron energy.
            ides: Photon electron production controls.
            iphot: Electron photon production controls.
            ibad: Bremsstrahlung angular distribution method controls.
            istrg: Electron continuous-energy straggling controls.
            bnum: Bremsstrahlung photon production controls.
            xnum: Sampling of electron-induced x-rays controls.
            rnok: Knock-on electron creation controls.
            enum: Photon-induced secondary electron creation controls.
            numb: Bremsstrahlung electron creation controls.
            i_mcs_model: Choice of Coulomb scattering model controls.
            efac: Stopping power energy spacing controls.
            electron_method_boundary: Single-event transport start sontrols.
            ckvnum: Crenkov photon emission scalar.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if emax is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, emax)
        if ides is None or ides not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ides)
        if iphot is None or iphot not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, iphot)
        if ibad is None or ibad not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ibad)
        if istrg is None or istrg not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, istrg)
        if bnum is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bnum)
        if xnum is None or not (xnum >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, xnum)
        if rnok is None or not (rnok >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, rnok)
        if enum is None or not (enum >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, enum)
        if numb is None or not (i_mcs_model >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, numb)
        if i_mcs_model is None or i_mcs_model not in {-1, 0}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, i_mcs_model)
        if efac is None or not (0.8 <= efac <= 0.99):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, efac)
        if electron_method_boundary is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, electron_method_boundary)
        if ckvnum is None or not (0 <= ckvnum < 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ckvnum)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                emax,
                ides,
                iphot,
                ibad,
                istrg,
                bnum,
                xnum,
                rnok,
                enum,
                numb,
                i_mcs_model,
                efac,
                electron_method_boundary,
                ckvnum,
            ]
        )

        self.emax: typing.Final[types.RealOrJump] = emax
        self.ides: typing.Final[types.IntegerOrJump] = ides
        self.iphot: typing.Final[types.IntegerOrJump] = iphot
        self.ibad: typing.Final[types.IntegerOrJump] = ibad
        self.istrg: typing.Final[types.IntegerOrJump] = istrg
        self.bnum: typing.Final[types.RealOrJump] = bnum
        self.xnum: typing.Final[types.RealOrJump] = xnum
        self.rnok: typing.Final[types.IntegerOrJump] = rnok
        self.enum: typing.Final[types.IntegerOrJump] = enum
        self.numb: typing.Final[types.IntegerOrJump] = numb
        self.i_mcs_model: typing.Final[types.IntegerOrJump] = i_mcs_model
        self.efac: typing.Final[types.RealOrJump] = efac
        self.electron_method_boundary: typing.Final[types.RealOrJump] = electron_method_boundary
        self.ckvnum: typing.Final[types.RealOrJump] = ckvnum
