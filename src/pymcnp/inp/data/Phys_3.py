import re
import copy
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

    _KEYWORD = 'phys:h'

    _ATTRS = {
        'emax': types.Real,
        'ean': types.Real,
        'tabl': types.Real,
        'istrg': types.Integer,
        'recl': types.Real,
        'i_mcs_model': types.Integer,
        'i_int_model': types.Integer,
        'i_els_model': types.Integer,
        'efac': types.Real,
        'ckvnum': types.Real,
        'drp': types.Real,
    }

    _REGEX = re.compile(
        rf'\Aphys:h( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z'
    )

    def __init__(
        self,
        emax: types.Real = None,
        ean: types.Real = None,
        tabl: types.Real = None,
        istrg: types.Integer = None,
        recl: types.Real = None,
        i_mcs_model: types.Integer = None,
        i_int_model: types.Integer = None,
        i_els_model: types.Integer = None,
        efac: types.Real = None,
        ckvnum: types.Real = None,
        drp: types.Real = None,
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

        if tabl is not None and not (
            isinstance(tabl.value, types.Jump) or tabl.value == -1 or tabl.value >= 0
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, tabl)
        if istrg is not None and not (isinstance(istrg.value, types.Jump) or istrg.value in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, istrg)
        if recl is not None and not (isinstance(recl.value, types.Jump) or 0 <= recl.value <= 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, recl)
        if i_mcs_model is not None and not (
            isinstance(i_mcs_model.value, types.Jump) or i_mcs_model.value in {-1, 0, 1, 2}
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, i_mcs_model)
        if i_int_model is not None and not (
            isinstance(i_int_model.value, types.Jump) or i_int_model.value in {-1, 0, 1, 2}
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, i_int_model)
        if i_els_model is not None and not (
            isinstance(i_els_model.value, types.Jump) or i_els_model.value in {-1, 0}
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, i_els_model)
        if efac is not None and not (
            isinstance(efac.value, types.Jump) or 0.8 <= efac.value <= 0.99
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, efac)
        if ckvnum is not None and not (
            isinstance(ckvnum.value, types.Jump) or 0 <= ckvnum.value < 1
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ckvnum)
        if drp is not None and not (
            isinstance(drp.value, types.Jump) or drp.value >= 0 or drp.value == -1
        ):
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

        self.emax: typing.Final[types.Real] = emax
        self.ean: typing.Final[types.Real] = ean
        self.tabl: typing.Final[types.Real] = tabl
        self.istrg: typing.Final[types.Integer] = istrg
        self.recl: typing.Final[types.Real] = recl
        self.i_mcs_model: typing.Final[types.Integer] = i_mcs_model
        self.i_int_model: typing.Final[types.Integer] = i_int_model
        self.i_els_model: typing.Final[types.Integer] = i_els_model
        self.efac: typing.Final[types.Real] = efac
        self.ckvnum: typing.Final[types.Real] = ckvnum
        self.drp: typing.Final[types.Real] = drp


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

    emax: str | float | types.Real = None
    ean: str | float | types.Real = None
    tabl: str | float | types.Real = None
    istrg: str | int | types.Integer = None
    recl: str | float | types.Real = None
    i_mcs_model: str | int | types.Integer = None
    i_int_model: str | int | types.Integer = None
    i_els_model: str | int | types.Integer = None
    efac: str | float | types.Real = None
    ckvnum: str | float | types.Real = None
    drp: str | float | types.Real = None

    def build(self):
        """
        Builds ``PhysBuilder_3`` into ``Phys_3``.

        Returns:
            ``Phys_3`` for ``PhysBuilder_3``.
        """

        emax = self.emax
        if isinstance(self.emax, types.Real):
            emax = self.emax
        elif isinstance(self.emax, float) or isinstance(self.emax, int):
            emax = types.Real(self.emax)
        elif isinstance(self.emax, str):
            emax = types.Real.from_mcnp(self.emax)

        ean = self.ean
        if isinstance(self.ean, types.Real):
            ean = self.ean
        elif isinstance(self.ean, float) or isinstance(self.ean, int):
            ean = types.Real(self.ean)
        elif isinstance(self.ean, str):
            ean = types.Real.from_mcnp(self.ean)

        tabl = self.tabl
        if isinstance(self.tabl, types.Real):
            tabl = self.tabl
        elif isinstance(self.tabl, float) or isinstance(self.tabl, int):
            tabl = types.Real(self.tabl)
        elif isinstance(self.tabl, str):
            tabl = types.Real.from_mcnp(self.tabl)

        istrg = self.istrg
        if isinstance(self.istrg, types.Integer):
            istrg = self.istrg
        elif isinstance(self.istrg, int):
            istrg = types.Integer(self.istrg)
        elif isinstance(self.istrg, str):
            istrg = types.Integer.from_mcnp(self.istrg)

        recl = self.recl
        if isinstance(self.recl, types.Real):
            recl = self.recl
        elif isinstance(self.recl, float) or isinstance(self.recl, int):
            recl = types.Real(self.recl)
        elif isinstance(self.recl, str):
            recl = types.Real.from_mcnp(self.recl)

        i_mcs_model = self.i_mcs_model
        if isinstance(self.i_mcs_model, types.Integer):
            i_mcs_model = self.i_mcs_model
        elif isinstance(self.i_mcs_model, int):
            i_mcs_model = types.Integer(self.i_mcs_model)
        elif isinstance(self.i_mcs_model, str):
            i_mcs_model = types.Integer.from_mcnp(self.i_mcs_model)

        i_int_model = self.i_int_model
        if isinstance(self.i_int_model, types.Integer):
            i_int_model = self.i_int_model
        elif isinstance(self.i_int_model, int):
            i_int_model = types.Integer(self.i_int_model)
        elif isinstance(self.i_int_model, str):
            i_int_model = types.Integer.from_mcnp(self.i_int_model)

        i_els_model = self.i_els_model
        if isinstance(self.i_els_model, types.Integer):
            i_els_model = self.i_els_model
        elif isinstance(self.i_els_model, int):
            i_els_model = types.Integer(self.i_els_model)
        elif isinstance(self.i_els_model, str):
            i_els_model = types.Integer.from_mcnp(self.i_els_model)

        efac = self.efac
        if isinstance(self.efac, types.Real):
            efac = self.efac
        elif isinstance(self.efac, float) or isinstance(self.efac, int):
            efac = types.Real(self.efac)
        elif isinstance(self.efac, str):
            efac = types.Real.from_mcnp(self.efac)

        ckvnum = self.ckvnum
        if isinstance(self.ckvnum, types.Real):
            ckvnum = self.ckvnum
        elif isinstance(self.ckvnum, float) or isinstance(self.ckvnum, int):
            ckvnum = types.Real(self.ckvnum)
        elif isinstance(self.ckvnum, str):
            ckvnum = types.Real.from_mcnp(self.ckvnum)

        drp = self.drp
        if isinstance(self.drp, types.Real):
            drp = self.drp
        elif isinstance(self.drp, float) or isinstance(self.drp, int):
            drp = types.Real(self.drp)
        elif isinstance(self.drp, str):
            drp = types.Real.from_mcnp(self.drp)

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

    @staticmethod
    def unbuild(ast: Phys_3):
        """
        Unbuilds ``Phys_3`` into ``PhysBuilder_3``

        Returns:
            ``PhysBuilder_3`` for ``Phys_3``.
        """

        return Phys_3(
            emax=copy.deepcopy(ast.emax),
            ean=copy.deepcopy(ast.ean),
            tabl=copy.deepcopy(ast.tabl),
            istrg=copy.deepcopy(ast.istrg),
            recl=copy.deepcopy(ast.recl),
            i_mcs_model=copy.deepcopy(ast.i_mcs_model),
            i_int_model=copy.deepcopy(ast.i_int_model),
            i_els_model=copy.deepcopy(ast.i_els_model),
            efac=copy.deepcopy(ast.efac),
            ckvnum=copy.deepcopy(ast.ckvnum),
            drp=copy.deepcopy(ast.drp),
        )
