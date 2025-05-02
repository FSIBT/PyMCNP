import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Phys_4(DataOption):
    """
    Represents INP phys variation #4 elements.

    Attributes:
        designator: Data card particle designator.
        emax: Upper energy limit.
        istrg: Charged-particle straggling controls.
        xmunum: Selection of muonic x-ray controls.
        xmugam: Probability for emitting k-shell photon.
        i_mcs_model: Choice of Coulomb scattering model controls.
        i_int_model: Treatment of nuclear interactions controls.
        i_els_model: Treatment of nuclear elastic scattering controls.
        efac: Stopping power energy spacing.
        ckvnum: Crenkov photon emission scalar.
        drp: Lower energy delta-ray cutoff.
    """

    _ATTRS = {
        'designator': types.Designator,
        'emax': types.RealOrJump,
        'istrg': types.IntegerOrJump,
        'xmunum': types.IntegerOrJump,
        'xmugam': types.RealOrJump,
        'i_mcs_model': types.IntegerOrJump,
        'i_int_model': types.IntegerOrJump,
        'i_els_model': types.IntegerOrJump,
        'efac': types.RealOrJump,
        'ckvnum': types.RealOrJump,
        'drp': types.RealOrJump,
    }

    _REGEX = re.compile(
        rf'\Aphys:(\S+)( {types.RealOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.IntegerOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?( {types.RealOrJump._REGEX.pattern})?\Z'
    )

    def __init__(
        self,
        designator: types.Designator,
        emax: types.RealOrJump = None,
        istrg: types.IntegerOrJump = None,
        xmunum: types.IntegerOrJump = None,
        xmugam: types.RealOrJump = None,
        i_mcs_model: types.IntegerOrJump = None,
        i_int_model: types.IntegerOrJump = None,
        i_els_model: types.IntegerOrJump = None,
        efac: types.RealOrJump = None,
        ckvnum: types.RealOrJump = None,
        drp: types.RealOrJump = None,
    ):
        """
        Initializes ``Phys_4``.

        Parameters:
            designator: Data card particle designator.
            emax: Upper energy limit.
            istrg: Charged-particle straggling controls.
            xmunum: Selection of muonic x-ray controls.
            xmugam: Probability for emitting k-shell photon.
            i_mcs_model: Choice of Coulomb scattering model controls.
            i_int_model: Treatment of nuclear interactions controls.
            i_els_model: Treatment of nuclear elastic scattering controls.
            efac: Stopping power energy spacing.
            ckvnum: Crenkov photon emission scalar.
            drp: Lower energy delta-ray cutoff.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, designator)
        if istrg is not None and not (isinstance(istrg, types.Jump) or istrg in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, istrg)
        if xmunum is not None and not (isinstance(xmunum, types.Jump) or xmunum in {-1, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, xmunum)
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
                istrg,
                xmunum,
                xmugam,
                i_mcs_model,
                i_int_model,
                i_els_model,
                efac,
                ckvnum,
                drp,
            ]
        )

        self.designator: typing.Final[types.Designator] = designator
        self.emax: typing.Final[types.RealOrJump] = emax
        self.istrg: typing.Final[types.IntegerOrJump] = istrg
        self.xmunum: typing.Final[types.IntegerOrJump] = xmunum
        self.xmugam: typing.Final[types.RealOrJump] = xmugam
        self.i_mcs_model: typing.Final[types.IntegerOrJump] = i_mcs_model
        self.i_int_model: typing.Final[types.IntegerOrJump] = i_int_model
        self.i_els_model: typing.Final[types.IntegerOrJump] = i_els_model
        self.efac: typing.Final[types.RealOrJump] = efac
        self.ckvnum: typing.Final[types.RealOrJump] = ckvnum
        self.drp: typing.Final[types.RealOrJump] = drp


@dataclasses.dataclass
class PhysBuilder_4:
    """
    Builds ``Phys_4``.

    Attributes:
        designator: Data card particle designator.
        emax: Upper energy limit.
        istrg: Charged-particle straggling controls.
        xmunum: Selection of muonic x-ray controls.
        xmugam: Probability for emitting k-shell photon.
        i_mcs_model: Choice of Coulomb scattering model controls.
        i_int_model: Treatment of nuclear interactions controls.
        i_els_model: Treatment of nuclear elastic scattering controls.
        efac: Stopping power energy spacing.
        ckvnum: Crenkov photon emission scalar.
        drp: Lower energy delta-ray cutoff.
    """

    designator: str | types.Designator
    emax: str | float | types.RealOrJump = None
    istrg: str | int | types.IntegerOrJump = None
    xmunum: str | int | types.IntegerOrJump = None
    xmugam: str | float | types.RealOrJump = None
    i_mcs_model: str | int | types.IntegerOrJump = None
    i_int_model: str | int | types.IntegerOrJump = None
    i_els_model: str | int | types.IntegerOrJump = None
    efac: str | float | types.RealOrJump = None
    ckvnum: str | float | types.RealOrJump = None
    drp: str | float | types.RealOrJump = None

    def build(self):
        """
        Builds ``PhysBuilder_4`` into ``Phys_4``.

        Returns:
            ``Phys_4`` for ``PhysBuilder_4``.
        """

        if isinstance(self.designator, types.Designator):
            designator = self.designator
        elif isinstance(self.designator, str):
            designator = types.Designator.from_mcnp(self.designator)

        emax = None
        if isinstance(self.emax, types.Real):
            emax = self.emax
        elif isinstance(self.emax, float) or isinstance(self.emax, int):
            emax = types.RealOrJump(self.emax)
        elif isinstance(self.emax, str):
            emax = types.RealOrJump.from_mcnp(self.emax)

        istrg = None
        if isinstance(self.istrg, types.Integer):
            istrg = self.istrg
        elif isinstance(self.istrg, int):
            istrg = types.IntegerOrJump(self.istrg)
        elif isinstance(self.istrg, str):
            istrg = types.IntegerOrJump.from_mcnp(self.istrg)

        xmunum = None
        if isinstance(self.xmunum, types.Integer):
            xmunum = self.xmunum
        elif isinstance(self.xmunum, int):
            xmunum = types.IntegerOrJump(self.xmunum)
        elif isinstance(self.xmunum, str):
            xmunum = types.IntegerOrJump.from_mcnp(self.xmunum)

        xmugam = None
        if isinstance(self.xmugam, types.Real):
            xmugam = self.xmugam
        elif isinstance(self.xmugam, float) or isinstance(self.xmugam, int):
            xmugam = types.RealOrJump(self.xmugam)
        elif isinstance(self.xmugam, str):
            xmugam = types.RealOrJump.from_mcnp(self.xmugam)

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

        return Phys_4(
            designator=designator,
            emax=emax,
            istrg=istrg,
            xmunum=xmunum,
            xmugam=xmugam,
            i_mcs_model=i_mcs_model,
            i_int_model=i_int_model,
            i_els_model=i_els_model,
            efac=efac,
            ckvnum=ckvnum,
            drp=drp,
        )
