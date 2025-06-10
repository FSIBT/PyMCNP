import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Phys_4(_option.DataOption):
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

    _KEYWORD = 'phys'

    _ATTRS = {
        'designator': types.Designator,
        'emax': types.Real,
        'istrg': types.Integer,
        'xmunum': types.Integer,
        'xmugam': types.Real,
        'i_mcs_model': types.Integer,
        'i_int_model': types.Integer,
        'i_els_model': types.Integer,
        'efac': types.Real,
        'ckvnum': types.Real,
        'drp': types.Real,
    }

    _REGEX = re.compile(
        rf'\Aphys:(\S+)( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z'
    )

    def __init__(
        self,
        designator: types.Designator,
        emax: types.Real = None,
        istrg: types.Integer = None,
        xmunum: types.Integer = None,
        xmugam: types.Real = None,
        i_mcs_model: types.Integer = None,
        i_int_model: types.Integer = None,
        i_els_model: types.Integer = None,
        efac: types.Real = None,
        ckvnum: types.Real = None,
        drp: types.Real = None,
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
        if istrg is not None and not (isinstance(istrg.value, types.Jump) or istrg.value in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, istrg)
        if xmunum is not None and not (isinstance(xmunum.value, types.Jump) or xmunum.value in {-1, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, xmunum)
        if i_mcs_model is not None and not (isinstance(i_mcs_model.value, types.Jump) or i_mcs_model.value in {-1, 0, 1, 2}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, i_mcs_model)
        if i_int_model is not None and not (isinstance(i_int_model.value, types.Jump) or i_int_model.value in {-1, 0, 1, 2}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, i_int_model)
        if i_els_model is not None and not (isinstance(i_els_model.value, types.Jump) or i_els_model.value in {-1, 0}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, i_els_model)
        if efac is not None and not (isinstance(efac.value, types.Jump) or 0.8 <= efac.value <= 0.99):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, efac)
        if ckvnum is not None and not (isinstance(ckvnum.value, types.Jump) or 0 <= ckvnum.value < 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ckvnum)
        if drp is not None and not (isinstance(drp.value, types.Jump) or drp.value >= 0 or drp.value == -1):
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
        self.emax: typing.Final[types.Real] = emax
        self.istrg: typing.Final[types.Integer] = istrg
        self.xmunum: typing.Final[types.Integer] = xmunum
        self.xmugam: typing.Final[types.Real] = xmugam
        self.i_mcs_model: typing.Final[types.Integer] = i_mcs_model
        self.i_int_model: typing.Final[types.Integer] = i_int_model
        self.i_els_model: typing.Final[types.Integer] = i_els_model
        self.efac: typing.Final[types.Real] = efac
        self.ckvnum: typing.Final[types.Real] = ckvnum
        self.drp: typing.Final[types.Real] = drp


@dataclasses.dataclass
class PhysBuilder_4(_option.DataOptionBuilder):
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
    emax: str | float | types.Real = None
    istrg: str | int | types.Integer = None
    xmunum: str | int | types.Integer = None
    xmugam: str | float | types.Real = None
    i_mcs_model: str | int | types.Integer = None
    i_int_model: str | int | types.Integer = None
    i_els_model: str | int | types.Integer = None
    efac: str | float | types.Real = None
    ckvnum: str | float | types.Real = None
    drp: str | float | types.Real = None

    def build(self):
        """
        Builds ``PhysBuilder_4`` into ``Phys_4``.

        Returns:
            ``Phys_4`` for ``PhysBuilder_4``.
        """

        designator = self.designator
        if isinstance(self.designator, types.Designator):
            designator = self.designator
        elif isinstance(self.designator, str):
            designator = types.Designator.from_mcnp(self.designator)

        emax = self.emax
        if isinstance(self.emax, types.Real):
            emax = self.emax
        elif isinstance(self.emax, float) or isinstance(self.emax, int):
            emax = types.Real(self.emax)
        elif isinstance(self.emax, str):
            emax = types.Real.from_mcnp(self.emax)

        istrg = self.istrg
        if isinstance(self.istrg, types.Integer):
            istrg = self.istrg
        elif isinstance(self.istrg, int):
            istrg = types.Integer(self.istrg)
        elif isinstance(self.istrg, str):
            istrg = types.Integer.from_mcnp(self.istrg)

        xmunum = self.xmunum
        if isinstance(self.xmunum, types.Integer):
            xmunum = self.xmunum
        elif isinstance(self.xmunum, int):
            xmunum = types.Integer(self.xmunum)
        elif isinstance(self.xmunum, str):
            xmunum = types.Integer.from_mcnp(self.xmunum)

        xmugam = self.xmugam
        if isinstance(self.xmugam, types.Real):
            xmugam = self.xmugam
        elif isinstance(self.xmugam, float) or isinstance(self.xmugam, int):
            xmugam = types.Real(self.xmugam)
        elif isinstance(self.xmugam, str):
            xmugam = types.Real.from_mcnp(self.xmugam)

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

    @staticmethod
    def unbuild(ast: Phys_4):
        """
        Unbuilds ``Phys_4`` into ``PhysBuilder_4``

        Returns:
            ``PhysBuilder_4`` for ``Phys_4``.
        """

        return PhysBuilder_4(
            designator=copy.deepcopy(ast.designator),
            emax=copy.deepcopy(ast.emax),
            istrg=copy.deepcopy(ast.istrg),
            xmunum=copy.deepcopy(ast.xmunum),
            xmugam=copy.deepcopy(ast.xmugam),
            i_mcs_model=copy.deepcopy(ast.i_mcs_model),
            i_int_model=copy.deepcopy(ast.i_int_model),
            i_els_model=copy.deepcopy(ast.i_els_model),
            efac=copy.deepcopy(ast.efac),
            ckvnum=copy.deepcopy(ast.ckvnum),
            drp=copy.deepcopy(ast.drp),
        )
