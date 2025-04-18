import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Phys_3(DataOption_, keyword='phys:h'):
    """
    Represents INP phys_3 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'emax': types.RealOrJump,
        'ean': types.RealOrJump,
        'tabl': types.RealOrJump,
        'istrg': types.IntegerOrJump,
        'recl': types.RealOrJump,
        'i_mcs_model': types.IntegerOrJump,
        'i_int_model': types.IntegerOrJump,
        'i_els_model': types.IntegerOrJump,
        'efac': types.RealOrJump,
        'ckvnum': types.RealOrJump,
        'drp': types.RealOrJump,
    }

    _REGEX = re.compile(
        rf'\Aphys:h( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        emax: types.RealOrJump,
        ean: types.RealOrJump,
        tabl: types.RealOrJump,
        istrg: types.IntegerOrJump,
        recl: types.RealOrJump,
        i_mcs_model: types.IntegerOrJump,
        i_int_model: types.IntegerOrJump,
        i_els_model: types.IntegerOrJump,
        efac: types.RealOrJump,
        ckvnum: types.RealOrJump,
        drp: types.RealOrJump,
    ):
        """
        Initializes ``Phys_3``.

        Parameters:
            emax: Upper proton energy limit.
            ean: Analog energy limit.
            tabl: Table-based physics cutoff.
            istrg: Charged-particle straggling controls.
            recl: Light ion recoil control.
            i_mcs_model: Choice of Coulomb scattering model controls.
            i_int_model: Treatment of nuclear interactions controls.
            i_els_model: Treatment of nuclear elastic scattering controls.
            efac: Stopping power energy spacing.
            ckvnum: Crenkov photon emission scalar.
            drp: Lower energy delta-ray cutoff.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if emax is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, emax)
        if ean is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ean)
        if tabl is None or not (tabl == -1 or tabl >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, tabl)
        if istrg is None or istrg not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, istrg)
        if recl is None or not (0 <= recl <= 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, recl)
        if i_mcs_model is None or i_mcs_model not in {-1, 0, 1, 2}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, i_mcs_model)
        if i_int_model is None or i_int_model not in {-1, 0, 1, 2}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, i_int_model)
        if i_els_model is None or i_els_model not in {-1, 0}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, i_els_model)
        if efac is None or not (0.8 <= efac <= 0.99):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, efac)
        if ckvnum is None or not (0 <= ckvnum < 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ckvnum)
        if drp is None or not (drp >= 0 or drp == -1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, drp)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                emax,
                ean,
                tabl,
                istrg,
                recl,
                i_mcs_model,
                i_int_model,
                i_els_model,
                efac,
                ckvnum,
                drp,
            ]
        )

        self.emax: typing.Final[types.RealOrJump] = emax
        self.ean: typing.Final[types.RealOrJump] = ean
        self.tabl: typing.Final[types.RealOrJump] = tabl
        self.istrg: typing.Final[types.IntegerOrJump] = istrg
        self.recl: typing.Final[types.RealOrJump] = recl
        self.i_mcs_model: typing.Final[types.IntegerOrJump] = i_mcs_model
        self.i_int_model: typing.Final[types.IntegerOrJump] = i_int_model
        self.i_els_model: typing.Final[types.IntegerOrJump] = i_els_model
        self.efac: typing.Final[types.RealOrJump] = efac
        self.ckvnum: typing.Final[types.RealOrJump] = ckvnum
        self.drp: typing.Final[types.RealOrJump] = drp
