import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Phys_0(DataOption):
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
        'emax': types.Real,
        'emcnf': types.Real,
        'iunr': types.Integer,
        'coilf': types.Real,
        'cutn': types.Integer,
        'ngam': types.Integer,
        'i_int_model': types.Integer,
        'i_els_model': types.Integer,
    }

    _REGEX = re.compile(
        rf'\Aphys:n( {types.Real._REGEX.pattern})?( {types.Real._REGEX.pattern})?( {types.Integer._REGEX.pattern})?( {types.Real._REGEX.pattern})?( {types.Integer._REGEX.pattern})?( {types.Integer._REGEX.pattern})?( {types.Integer._REGEX.pattern})?( {types.Integer._REGEX.pattern})?\Z'
    )

    def __init__(
        self,
        emax: types.Real = None,
        emcnf: types.Real = None,
        iunr: types.Integer = None,
        coilf: types.Real = None,
        cutn: types.Integer = None,
        ngam: types.Integer = None,
        i_int_model: types.Integer = None,
        i_els_model: types.Integer = None,
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
            InpError: SEMANTICS_OPTION.
        """

        if iunr is not None and not (isinstance(iunr.value, types.Jump) or iunr.value in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, iunr)
        if ngam is not None and not (isinstance(ngam.value, types.Jump) or ngam.value in {0, 1, 2}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ngam)
        if i_int_model is not None and not (
            isinstance(i_int_model.value, types.Jump) or i_int_model.value in {-1, 0, 1, 2, 3}
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, i_int_model)
        if i_els_model is not None and not (
            isinstance(i_els_model.value, types.Jump) or i_els_model.value in {-1, 0, 1}
        ):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, i_els_model)

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

        self.emax: typing.Final[types.Real] = emax
        self.emcnf: typing.Final[types.Real] = emcnf
        self.iunr: typing.Final[types.Integer] = iunr
        self.coilf: typing.Final[types.Real] = coilf
        self.cutn: typing.Final[types.Integer] = cutn
        self.ngam: typing.Final[types.Integer] = ngam
        self.i_int_model: typing.Final[types.Integer] = i_int_model
        self.i_els_model: typing.Final[types.Integer] = i_els_model


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

    emax: str | float | types.Real = None
    emcnf: str | float | types.Real = None
    iunr: str | int | types.Integer = None
    coilf: str | float | types.Real = None
    cutn: str | int | types.Integer = None
    ngam: str | int | types.Integer = None
    i_int_model: str | int | types.Integer = None
    i_els_model: str | int | types.Integer = None

    def build(self):
        """
        Builds ``PhysBuilder_0`` into ``Phys_0``.

        Returns:
            ``Phys_0`` for ``PhysBuilder_0``.
        """

        emax = self.emax
        if isinstance(self.emax, types.Real):
            emax = self.emax
        elif isinstance(self.emax, float) or isinstance(self.emax, int):
            emax = types.Real(self.emax)
        elif isinstance(self.emax, str):
            emax = types.Real.from_mcnp(self.emax)

        emcnf = self.emcnf
        if isinstance(self.emcnf, types.Real):
            emcnf = self.emcnf
        elif isinstance(self.emcnf, float) or isinstance(self.emcnf, int):
            emcnf = types.Real(self.emcnf)
        elif isinstance(self.emcnf, str):
            emcnf = types.Real.from_mcnp(self.emcnf)

        iunr = self.iunr
        if isinstance(self.iunr, types.Integer):
            iunr = self.iunr
        elif isinstance(self.iunr, int):
            iunr = types.Integer(self.iunr)
        elif isinstance(self.iunr, str):
            iunr = types.Integer.from_mcnp(self.iunr)

        coilf = self.coilf
        if isinstance(self.coilf, types.Real):
            coilf = self.coilf
        elif isinstance(self.coilf, float) or isinstance(self.coilf, int):
            coilf = types.Real(self.coilf)
        elif isinstance(self.coilf, str):
            coilf = types.Real.from_mcnp(self.coilf)

        cutn = self.cutn
        if isinstance(self.cutn, types.Integer):
            cutn = self.cutn
        elif isinstance(self.cutn, int):
            cutn = types.Integer(self.cutn)
        elif isinstance(self.cutn, str):
            cutn = types.Integer.from_mcnp(self.cutn)

        ngam = self.ngam
        if isinstance(self.ngam, types.Integer):
            ngam = self.ngam
        elif isinstance(self.ngam, int):
            ngam = types.Integer(self.ngam)
        elif isinstance(self.ngam, str):
            ngam = types.Integer.from_mcnp(self.ngam)

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
