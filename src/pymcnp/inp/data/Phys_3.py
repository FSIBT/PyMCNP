import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Phys_3(DataOption):
    """
    Represents INP phys variation #3 elements.

    Attributes:
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
        rf'\Aphys:h( {types.RealOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?\Z'
    )

    def __init__(
        self,
        emax: types.RealOrJump = None,
        ean: types.RealOrJump = None,
        tabl: types.RealOrJump = None,
        istrg: types.IntegerOrJump = None,
        recl: types.RealOrJump = None,
        i_mcs_model: types.IntegerOrJump = None,
        i_int_model: types.IntegerOrJump = None,
        i_els_model: types.IntegerOrJump = None,
        efac: types.RealOrJump = None,
        ckvnum: types.RealOrJump = None,
        drp: types.RealOrJump = None,
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
            InpError: SEMANTICS_OPTION.
        """

        if tabl is not None and not (isinstance(tabl, types.Jump) or tabl == -1 or tabl >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, tabl)
        if istrg is not None and not (isinstance(istrg, types.Jump) or istrg in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, istrg)
        if recl is not None and not (isinstance(recl, types.Jump) or 0 <= recl <= 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, recl)
        if i_mcs_model is not None and not (
            isinstance(i_mcs_model, types.Jump) or i_mcs_model in {-1, 0, 1, 2}
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, i_mcs_model)
        if i_int_model is not None and not (
            isinstance(i_int_model, types.Jump) or i_int_model in {-1, 0, 1, 2}
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, i_int_model)
        if i_els_model is not None and not (
            isinstance(i_els_model, types.Jump) or i_els_model in {-1, 0}
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, i_els_model)
        if efac is not None and not (isinstance(efac, types.Jump) or 0.8 <= efac <= 0.99):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, efac)
        if ckvnum is not None and not (isinstance(ckvnum, types.Jump) or 0 <= ckvnum < 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ckvnum)
        if drp is not None and not (isinstance(drp, types.Jump) or drp >= 0 or drp == -1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, drp)

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


@dataclasses.dataclass
class PhysBuilder_3:
    """
    Builds ``Phys_3``.

    Attributes:
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
    """

    emax: str | float | types.RealOrJump = None
    ean: str | float | types.RealOrJump = None
    tabl: str | float | types.RealOrJump = None
    istrg: str | int | types.IntegerOrJump = None
    recl: str | float | types.RealOrJump = None
    i_mcs_model: str | int | types.IntegerOrJump = None
    i_int_model: str | int | types.IntegerOrJump = None
    i_els_model: str | int | types.IntegerOrJump = None
    efac: str | float | types.RealOrJump = None
    ckvnum: str | float | types.RealOrJump = None
    drp: str | float | types.RealOrJump = None

    def build(self):
        """
        Builds ``PhysBuilder_3`` into ``Phys_3``.

        Returns:
            ``Phys_3`` for ``PhysBuilder_3``.
        """

        emax = None
        if isinstance(self.emax, types.Real):
            emax = self.emax
        elif isinstance(self.emax, float) or isinstance(self.emax, int):
            emax = types.RealOrJump(self.emax)
        elif isinstance(self.emax, str):
            emax = types.RealOrJump.from_mcnp(self.emax)

        ean = None
        if isinstance(self.ean, types.Real):
            ean = self.ean
        elif isinstance(self.ean, float) or isinstance(self.ean, int):
            ean = types.RealOrJump(self.ean)
        elif isinstance(self.ean, str):
            ean = types.RealOrJump.from_mcnp(self.ean)

        tabl = None
        if isinstance(self.tabl, types.Real):
            tabl = self.tabl
        elif isinstance(self.tabl, float) or isinstance(self.tabl, int):
            tabl = types.RealOrJump(self.tabl)
        elif isinstance(self.tabl, str):
            tabl = types.RealOrJump.from_mcnp(self.tabl)

        istrg = None
        if isinstance(self.istrg, types.Integer):
            istrg = self.istrg
        elif isinstance(self.istrg, int):
            istrg = types.IntegerOrJump(self.istrg)
        elif isinstance(self.istrg, str):
            istrg = types.IntegerOrJump.from_mcnp(self.istrg)

        recl = None
        if isinstance(self.recl, types.Real):
            recl = self.recl
        elif isinstance(self.recl, float) or isinstance(self.recl, int):
            recl = types.RealOrJump(self.recl)
        elif isinstance(self.recl, str):
            recl = types.RealOrJump.from_mcnp(self.recl)

        i_mcs_model = None
        if isinstance(self.i_mcs_model, types.Integer):
            i_mcs_model = self.i_mcs_model
        elif isinstance(self.i_mcs_model, int):
            i_mcs_model = types.IntegerOrJump(self.i_mcs_model)
        elif isinstance(self.i_mcs_model, str):
            i_mcs_model = types.IntegerOrJump.from_mcnp(self.i_mcs_model)

        i_int_model = None
        if isinstance(self.i_int_model, types.Integer):
            i_int_model = self.i_int_model
        elif isinstance(self.i_int_model, int):
            i_int_model = types.IntegerOrJump(self.i_int_model)
        elif isinstance(self.i_int_model, str):
            i_int_model = types.IntegerOrJump.from_mcnp(self.i_int_model)

        i_els_model = None
        if isinstance(self.i_els_model, types.Integer):
            i_els_model = self.i_els_model
        elif isinstance(self.i_els_model, int):
            i_els_model = types.IntegerOrJump(self.i_els_model)
        elif isinstance(self.i_els_model, str):
            i_els_model = types.IntegerOrJump.from_mcnp(self.i_els_model)

        efac = None
        if isinstance(self.efac, types.Real):
            efac = self.efac
        elif isinstance(self.efac, float) or isinstance(self.efac, int):
            efac = types.RealOrJump(self.efac)
        elif isinstance(self.efac, str):
            efac = types.RealOrJump.from_mcnp(self.efac)

        ckvnum = None
        if isinstance(self.ckvnum, types.Real):
            ckvnum = self.ckvnum
        elif isinstance(self.ckvnum, float) or isinstance(self.ckvnum, int):
            ckvnum = types.RealOrJump(self.ckvnum)
        elif isinstance(self.ckvnum, str):
            ckvnum = types.RealOrJump.from_mcnp(self.ckvnum)

        drp = None
        if isinstance(self.drp, types.Real):
            drp = self.drp
        elif isinstance(self.drp, float) or isinstance(self.drp, int):
            drp = types.RealOrJump(self.drp)
        elif isinstance(self.drp, str):
            drp = types.RealOrJump.from_mcnp(self.drp)

        return Phys_3(
            emax=emax,
            ean=ean,
            tabl=tabl,
            istrg=istrg,
            recl=recl,
            i_mcs_model=i_mcs_model,
            i_int_model=i_int_model,
            i_els_model=i_els_model,
            efac=efac,
            ckvnum=ckvnum,
            drp=drp,
        )
