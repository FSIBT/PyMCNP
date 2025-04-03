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
