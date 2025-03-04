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
        'emax': types.Real,
        'ides': types.Integer,
        'iphot': types.Integer,
        'ibad': types.Integer,
        'istrg': types.Integer,
        'bnum': types.Real,
        'xnum': types.Real,
        'rnok': types.Integer,
        'enum': types.Integer,
        'numb': types.Integer,
        'i_mcs_model': types.Integer,
        'efac': types.Real,
        'electron_method_boundary': types.Real,
        'ckvnum': types.Real,
    }

    _REGEX = re.compile(
        r'phys:e( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)'
    )

    def __init__(
        self,
        emax: types.Real,
        ides: types.Integer,
        iphot: types.Integer,
        ibad: types.Integer,
        istrg: types.Integer,
        bnum: types.Real,
        xnum: types.Real,
        rnok: types.Integer,
        enum: types.Integer,
        numb: types.Integer,
        i_mcs_model: types.Integer,
        efac: types.Real,
        electron_method_boundary: types.Real,
        ckvnum: types.Real,
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

        self.emax: typing.Final[types.Real] = emax
        self.ides: typing.Final[types.Integer] = ides
        self.iphot: typing.Final[types.Integer] = iphot
        self.ibad: typing.Final[types.Integer] = ibad
        self.istrg: typing.Final[types.Integer] = istrg
        self.bnum: typing.Final[types.Real] = bnum
        self.xnum: typing.Final[types.Real] = xnum
        self.rnok: typing.Final[types.Integer] = rnok
        self.enum: typing.Final[types.Integer] = enum
        self.numb: typing.Final[types.Integer] = numb
        self.i_mcs_model: typing.Final[types.Integer] = i_mcs_model
        self.efac: typing.Final[types.Real] = efac
        self.electron_method_boundary: typing.Final[types.Real] = electron_method_boundary
        self.ckvnum: typing.Final[types.Real] = ckvnum
