import re

from . import _option
from ...utils import types
from ...utils import errors


class Phys_0(_option.DataOption):
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

    _KEYWORD = 'phys:n'

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
        rf'\Aphys:n( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?( {types.Integer._REGEX.pattern[2:-2]})?\Z'
    )

    def __init__(
        self,
        emax: str | int | float | types.Real = None,
        emcnf: str | int | float | types.Real = None,
        iunr: str | int | types.Integer = None,
        coilf: str | int | float | types.Real = None,
        cutn: str | int | types.Integer = None,
        ngam: str | int | types.Integer = None,
        i_int_model: str | int | types.Integer = None,
        i_els_model: str | int | types.Integer = None,
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

        self.emax: types.Real = emax
        self.emcnf: types.Real = emcnf
        self.iunr: types.Integer = iunr
        self.coilf: types.Real = coilf
        self.cutn: types.Integer = cutn
        self.ngam: types.Integer = ngam
        self.i_int_model: types.Integer = i_int_model
        self.i_els_model: types.Integer = i_els_model

    @property
    def emax(self) -> types.Real:
        """
        Gets ``emax``.

        Returns:
            ``emax``.
        """

        return self._emax

    @emax.setter
    def emax(self, emax: str | int | float | types.Real) -> None:
        """
        Sets ``emax``.

        Parameters:
            emax: Upper limit for neutron energy.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if emax is not None:
            if isinstance(emax, types.Real):
                emax = emax
            elif isinstance(emax, int):
                emax = types.Real(emax)
            elif isinstance(emax, float):
                emax = types.Real(emax)
            elif isinstance(emax, str):
                emax = types.Real.from_mcnp(emax)
            else:
                raise TypeError

        self._emax: types.Real = emax

    @property
    def emcnf(self) -> types.Real:
        """
        Gets ``emcnf``.

        Returns:
            ``emcnf``.
        """

        return self._emcnf

    @emcnf.setter
    def emcnf(self, emcnf: str | int | float | types.Real) -> None:
        """
        Sets ``emcnf``.

        Parameters:
            emcnf: Analog energy limit.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if emcnf is not None:
            if isinstance(emcnf, types.Real):
                emcnf = emcnf
            elif isinstance(emcnf, int):
                emcnf = types.Real(emcnf)
            elif isinstance(emcnf, float):
                emcnf = types.Real(emcnf)
            elif isinstance(emcnf, str):
                emcnf = types.Real.from_mcnp(emcnf)
            else:
                raise TypeError

        self._emcnf: types.Real = emcnf

    @property
    def iunr(self) -> types.Integer:
        """
        Gets ``iunr``.

        Returns:
            ``iunr``.
        """

        return self._iunr

    @iunr.setter
    def iunr(self, iunr: str | int | types.Integer) -> None:
        """
        Sets ``iunr``.

        Parameters:
            iunr: Unresolved resonanace controls.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if iunr is not None:
            if isinstance(iunr, types.Integer):
                iunr = iunr
            elif isinstance(iunr, int):
                iunr = types.Integer(iunr)
            elif isinstance(iunr, str):
                iunr = types.Integer.from_mcnp(iunr)
            else:
                raise TypeError

        if iunr is not None and not (isinstance(iunr.value, types.Jump) or iunr in {0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, iunr)

        self._iunr: types.Integer = iunr

    @property
    def coilf(self) -> types.Real:
        """
        Gets ``coilf``.

        Returns:
            ``coilf``.
        """

        return self._coilf

    @coilf.setter
    def coilf(self, coilf: str | int | float | types.Real) -> None:
        """
        Sets ``coilf``.

        Parameters:
            coilf: Light-ion and heavy-ion recoil and NCIA control.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if coilf is not None:
            if isinstance(coilf, types.Real):
                coilf = coilf
            elif isinstance(coilf, int):
                coilf = types.Real(coilf)
            elif isinstance(coilf, float):
                coilf = types.Real(coilf)
            elif isinstance(coilf, str):
                coilf = types.Real.from_mcnp(coilf)
            else:
                raise TypeError

        self._coilf: types.Real = coilf

    @property
    def cutn(self) -> types.Integer:
        """
        Gets ``cutn``.

        Returns:
            ``cutn``.
        """

        return self._cutn

    @cutn.setter
    def cutn(self, cutn: str | int | types.Integer) -> None:
        """
        Sets ``cutn``.

        Parameters:
            cutn: Table-based physics cutoff controls.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if cutn is not None:
            if isinstance(cutn, types.Integer):
                cutn = cutn
            elif isinstance(cutn, int):
                cutn = types.Integer(cutn)
            elif isinstance(cutn, str):
                cutn = types.Integer.from_mcnp(cutn)
            else:
                raise TypeError

        self._cutn: types.Integer = cutn

    @property
    def ngam(self) -> types.Integer:
        """
        Gets ``ngam``.

        Returns:
            ``ngam``.
        """

        return self._ngam

    @ngam.setter
    def ngam(self, ngam: str | int | types.Integer) -> None:
        """
        Sets ``ngam``.

        Parameters:
            ngam: Secondary photon production controls.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if ngam is not None:
            if isinstance(ngam, types.Integer):
                ngam = ngam
            elif isinstance(ngam, int):
                ngam = types.Integer(ngam)
            elif isinstance(ngam, str):
                ngam = types.Integer.from_mcnp(ngam)
            else:
                raise TypeError

        if ngam is not None and not (isinstance(ngam.value, types.Jump) or ngam in {0, 1, 2}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ngam)

        self._ngam: types.Integer = ngam

    @property
    def i_int_model(self) -> types.Integer:
        """
        Gets ``i_int_model``.

        Returns:
            ``i_int_model``.
        """

        return self._i_int_model

    @i_int_model.setter
    def i_int_model(self, i_int_model: str | int | types.Integer) -> None:
        """
        Sets ``i_int_model``.

        Parameters:
            i_int_model: Treataement of nuclear interactions controls.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if i_int_model is not None:
            if isinstance(i_int_model, types.Integer):
                i_int_model = i_int_model
            elif isinstance(i_int_model, int):
                i_int_model = types.Integer(i_int_model)
            elif isinstance(i_int_model, str):
                i_int_model = types.Integer.from_mcnp(i_int_model)
            else:
                raise TypeError

        if i_int_model is not None and not (isinstance(i_int_model.value, types.Jump) or i_int_model in {-1, 0, 1, 2, 3}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, i_int_model)

        self._i_int_model: types.Integer = i_int_model

    @property
    def i_els_model(self) -> types.Integer:
        """
        Gets ``i_els_model``.

        Returns:
            ``i_els_model``.
        """

        return self._i_els_model

    @i_els_model.setter
    def i_els_model(self, i_els_model: str | int | types.Integer) -> None:
        """
        Sets ``i_els_model``.

        Parameters:
            i_els_model: Treatment of nuclear elastic scattering controls.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if i_els_model is not None:
            if isinstance(i_els_model, types.Integer):
                i_els_model = i_els_model
            elif isinstance(i_els_model, int):
                i_els_model = types.Integer(i_els_model)
            elif isinstance(i_els_model, str):
                i_els_model = types.Integer.from_mcnp(i_els_model)
            else:
                raise TypeError

        if i_els_model is not None and not (isinstance(i_els_model.value, types.Jump) or i_els_model in {-1, 0, 1}):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, i_els_model)

        self._i_els_model: types.Integer = i_els_model
