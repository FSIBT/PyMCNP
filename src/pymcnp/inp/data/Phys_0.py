import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Phys_0(DataOption_, keyword='phys:n'):
    """
    Represents INP phys_0 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'emax': types.Real,
        'emcnf': types.Real,
        'iunr': types.Real,
        'coilf': types.Real,
        'cutn': types.Integer,
        'ngam': types.Integer,
        'i_int_model': types.Integer,
        'i_els_model': types.Integer,
    }

    _REGEX = re.compile(r'phys:n( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)')

    def __init__(
        self,
        emax: types.Real,
        emcnf: types.Real,
        iunr: types.Real,
        coilf: types.Real,
        cutn: types.Integer,
        ngam: types.Integer,
        i_int_model: types.Integer,
        i_els_model: types.Integer,
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

        self.emax: typing.Final[types.Real] = emax
        self.emcnf: typing.Final[types.Real] = emcnf
        self.iunr: typing.Final[types.Real] = iunr
        self.coilf: typing.Final[types.Real] = coilf
        self.cutn: typing.Final[types.Integer] = cutn
        self.ngam: typing.Final[types.Integer] = ngam
        self.i_int_model: typing.Final[types.Integer] = i_int_model
        self.i_els_model: typing.Final[types.Integer] = i_els_model
