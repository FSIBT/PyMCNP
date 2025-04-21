import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Phys_0(DataOption, keyword='phys:n'):
    """
    Represents INP phys variation #0 elements.

    Attributes:
        emax: Upper limit for neutron energy.
        emcnf: Analog energy limit.
        iunr: Unresolved resonanace controls.
        coilf: Light-ion and heavy-ion recoil and NCIA control.
        cutn: Table-based physics cutoff controls.
        ngam: Secondary photon production controls.
        i_int_model: Treataement of nuclear interactions controls.
        i_els_model: Treatment of nuclear elastic scattering controls.
    """

    _ATTRS = {
        'emax': types.RealOrJump,
        'emcnf': types.RealOrJump,
        'iunr': types.RealOrJump,
        'coilf': types.RealOrJump,
        'cutn': types.IntegerOrJump,
        'ngam': types.IntegerOrJump,
        'i_int_model': types.IntegerOrJump,
        'i_els_model': types.IntegerOrJump,
    }

    _REGEX = re.compile(
        rf'\Aphys:n( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        emax: types.RealOrJump,
        emcnf: types.RealOrJump,
        iunr: types.RealOrJump,
        coilf: types.RealOrJump,
        cutn: types.IntegerOrJump,
        ngam: types.IntegerOrJump,
        i_int_model: types.IntegerOrJump,
        i_els_model: types.IntegerOrJump,
    ):
        """
        Initializes ``Phys_0``.

        Parameters:
            emax: Upper limit for neutron energy.
            emcnf: Analog energy limit.
            iunr: Unresolved resonanace controls.
            coilf: Light-ion and heavy-ion recoil and NCIA control.
            cutn: Table-based physics cutoff controls.
            ngam: Secondary photon production controls.
            i_int_model: Treataement of nuclear interactions controls.
            i_els_model: Treatment of nuclear elastic scattering controls.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if emax is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, emax)
        if emcnf is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, emcnf)
        if iunr is None or iunr not in {0, 1}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, iunr)
        if coilf is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, coilf)
        if cutn is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, cutn)
        if ngam is None or ngam not in {0, 1, 2}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ngam)
        if i_int_model is None or i_int_model not in {-1, 0, 1, 2}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, i_int_model)
        if i_els_model is None or i_els_model not in {-1, 0}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, i_els_model)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                emax,
                emcnf,
                iunr,
                coilf,
                cutn,
                ngam,
                i_int_model,
                i_els_model,
            ]
        )

        self.emax: typing.Final[types.RealOrJump] = emax
        self.emcnf: typing.Final[types.RealOrJump] = emcnf
        self.iunr: typing.Final[types.RealOrJump] = iunr
        self.coilf: typing.Final[types.RealOrJump] = coilf
        self.cutn: typing.Final[types.IntegerOrJump] = cutn
        self.ngam: typing.Final[types.IntegerOrJump] = ngam
        self.i_int_model: typing.Final[types.IntegerOrJump] = i_int_model
        self.i_els_model: typing.Final[types.IntegerOrJump] = i_els_model


@dataclasses.dataclass
class PhysBuilder_0:
    """
    Builds ``Phys_0``.

    Attributes:
        emax: Upper limit for neutron energy.
        emcnf: Analog energy limit.
        iunr: Unresolved resonanace controls.
        coilf: Light-ion and heavy-ion recoil and NCIA control.
        cutn: Table-based physics cutoff controls.
        ngam: Secondary photon production controls.
        i_int_model: Treataement of nuclear interactions controls.
        i_els_model: Treatment of nuclear elastic scattering controls.
    """

    emax: str | float | types.RealOrJump
    emcnf: str | float | types.RealOrJump
    iunr: str | float | types.RealOrJump
    coilf: str | float | types.RealOrJump
    cutn: str | int | types.IntegerOrJump
    ngam: str | int | types.IntegerOrJump
    i_int_model: str | int | types.IntegerOrJump
    i_els_model: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``PhysBuilder_0`` into ``Phys_0``.

        Returns:
            ``Phys_0`` for ``PhysBuilder_0``.
        """

        if isinstance(self.emax, types.Real):
            emax = self.emax
        elif isinstance(self.emax, float) or isinstance(self.emax, int):
            emax = types.RealOrJump(self.emax)
        elif isinstance(self.emax, str):
            emax = types.RealOrJump.from_mcnp(self.emax)

        if isinstance(self.emcnf, types.Real):
            emcnf = self.emcnf
        elif isinstance(self.emcnf, float) or isinstance(self.emcnf, int):
            emcnf = types.RealOrJump(self.emcnf)
        elif isinstance(self.emcnf, str):
            emcnf = types.RealOrJump.from_mcnp(self.emcnf)

        if isinstance(self.iunr, types.Real):
            iunr = self.iunr
        elif isinstance(self.iunr, float) or isinstance(self.iunr, int):
            iunr = types.RealOrJump(self.iunr)
        elif isinstance(self.iunr, str):
            iunr = types.RealOrJump.from_mcnp(self.iunr)

        if isinstance(self.coilf, types.Real):
            coilf = self.coilf
        elif isinstance(self.coilf, float) or isinstance(self.coilf, int):
            coilf = types.RealOrJump(self.coilf)
        elif isinstance(self.coilf, str):
            coilf = types.RealOrJump.from_mcnp(self.coilf)

        if isinstance(self.cutn, types.Integer):
            cutn = self.cutn
        elif isinstance(self.cutn, int):
            cutn = types.IntegerOrJump(self.cutn)
        elif isinstance(self.cutn, str):
            cutn = types.IntegerOrJump.from_mcnp(self.cutn)

        if isinstance(self.ngam, types.Integer):
            ngam = self.ngam
        elif isinstance(self.ngam, int):
            ngam = types.IntegerOrJump(self.ngam)
        elif isinstance(self.ngam, str):
            ngam = types.IntegerOrJump.from_mcnp(self.ngam)

        if isinstance(self.i_int_model, types.Integer):
            i_int_model = self.i_int_model
        elif isinstance(self.i_int_model, int):
            i_int_model = types.IntegerOrJump(self.i_int_model)
        elif isinstance(self.i_int_model, str):
            i_int_model = types.IntegerOrJump.from_mcnp(self.i_int_model)

        if isinstance(self.i_els_model, types.Integer):
            i_els_model = self.i_els_model
        elif isinstance(self.i_els_model, int):
            i_els_model = types.IntegerOrJump(self.i_els_model)
        elif isinstance(self.i_els_model, str):
            i_els_model = types.IntegerOrJump.from_mcnp(self.i_els_model)

        return Phys_0(
            emax=emax,
            emcnf=emcnf,
            iunr=iunr,
            coilf=coilf,
            cutn=cutn,
            ngam=ngam,
            i_int_model=i_int_model,
            i_els_model=i_els_model,
        )
