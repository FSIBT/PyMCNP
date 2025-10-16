import re

import numpy

from . import _option
from ... import types
from ... import errors


class Rec(_option.SurfaceOption):
    """
    Represents INP `rec` elements.
    """

    _KEYWORD = 'rec'

    _ATTRS = {
        'vx': types.Real,
        'vy': types.Real,
        'vz': types.Real,
        'hx': types.Real,
        'hy': types.Real,
        'hz': types.Real,
        'v1x': types.Real,
        'v1y': types.Real,
        'v1z': types.Real,
        'v2x': types.Real,
        'v2y': types.Real,
        'v2z': types.Real,
    }

    _REGEX = re.compile(
        rf'\Arec( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})?( {types.Real._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        vx: str | int | float | types.Real,
        vy: str | int | float | types.Real,
        vz: str | int | float | types.Real,
        hx: str | int | float | types.Real,
        hy: str | int | float | types.Real,
        hz: str | int | float | types.Real,
        v1x: str | int | float | types.Real,
        v1y: str | int | float | types.Real,
        v1z: str | int | float | types.Real,
        v2x: str | int | float | types.Real,
        v2y: str | int | float | types.Real = None,
        v2z: str | int | float | types.Real = None,
    ):
        """
        Initializes `Rec`.

        Parameters:
            vx: Elliptical cylinder position vector x component.
            vy: Elliptical cylinder position vector y component.
            vz: Elliptical cylinder position vector z component.
            hx: Elliptical cylinder height vector x component.
            hy: Elliptical cylinder height vector y component.
            hz: Elliptical cylinder height vector z component.
            v1x: Elliptical cylinder major axis vector x component.
            v1y: Elliptical cylinder major axis vector y component.
            v1z: Elliptical cylinder major axis vector z component.
            v2x: Elliptical cylinder minor axis vector x component.
            v2y: Elliptical cylinder minor axis vector y component.
            v2z: Elliptical cylinder minor axis vector z component.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.vx: types.Real = vx
        self.vy: types.Real = vy
        self.vz: types.Real = vz
        self.hx: types.Real = hx
        self.hy: types.Real = hy
        self.hz: types.Real = hz
        self.v1x: types.Real = v1x
        self.v1y: types.Real = v1y
        self.v1z: types.Real = v1z
        self.v2x: types.Real = v2x
        self.v2y: types.Real = v2y
        self.v2z: types.Real = v2z

    @property
    def vx(self) -> types.Real:
        """
        Elliptical cylinder position vector x component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._vx

    @vx.setter
    def vx(self, vx: str | int | float | types.Real) -> None:
        """
        Sets `vx`.

        Parameters:
            vx: Elliptical cylinder position vector x component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if vx is not None:
            if isinstance(vx, types.Real):
                vx = vx
            elif isinstance(vx, int) or isinstance(vx, float):
                vx = types.Real(vx)
            elif isinstance(vx, str):
                vx = types.Real.from_mcnp(vx)

        if vx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vx)

        self._vx: types.Real = vx

    @property
    def vy(self) -> types.Real:
        """
        Elliptical cylinder position vector y component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._vy

    @vy.setter
    def vy(self, vy: str | int | float | types.Real) -> None:
        """
        Sets `vy`.

        Parameters:
            vy: Elliptical cylinder position vector y component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if vy is not None:
            if isinstance(vy, types.Real):
                vy = vy
            elif isinstance(vy, int) or isinstance(vy, float):
                vy = types.Real(vy)
            elif isinstance(vy, str):
                vy = types.Real.from_mcnp(vy)

        if vy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vy)

        self._vy: types.Real = vy

    @property
    def vz(self) -> types.Real:
        """
        Elliptical cylinder position vector z component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._vz

    @vz.setter
    def vz(self, vz: str | int | float | types.Real) -> None:
        """
        Sets `vz`.

        Parameters:
            vz: Elliptical cylinder position vector z component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if vz is not None:
            if isinstance(vz, types.Real):
                vz = vz
            elif isinstance(vz, int) or isinstance(vz, float):
                vz = types.Real(vz)
            elif isinstance(vz, str):
                vz = types.Real.from_mcnp(vz)

        if vz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, vz)

        self._vz: types.Real = vz

    @property
    def hx(self) -> types.Real:
        """
        Elliptical cylinder height vector x component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._hx

    @hx.setter
    def hx(self, hx: str | int | float | types.Real) -> None:
        """
        Sets `hx`.

        Parameters:
            hx: Elliptical cylinder height vector x component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if hx is not None:
            if isinstance(hx, types.Real):
                hx = hx
            elif isinstance(hx, int) or isinstance(hx, float):
                hx = types.Real(hx)
            elif isinstance(hx, str):
                hx = types.Real.from_mcnp(hx)

        if hx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, hx)

        self._hx: types.Real = hx

    @property
    def hy(self) -> types.Real:
        """
        Elliptical cylinder height vector y component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._hy

    @hy.setter
    def hy(self, hy: str | int | float | types.Real) -> None:
        """
        Sets `hy`.

        Parameters:
            hy: Elliptical cylinder height vector y component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if hy is not None:
            if isinstance(hy, types.Real):
                hy = hy
            elif isinstance(hy, int) or isinstance(hy, float):
                hy = types.Real(hy)
            elif isinstance(hy, str):
                hy = types.Real.from_mcnp(hy)

        if hy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, hy)

        self._hy: types.Real = hy

    @property
    def hz(self) -> types.Real:
        """
        Elliptical cylinder height vector z component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._hz

    @hz.setter
    def hz(self, hz: str | int | float | types.Real) -> None:
        """
        Sets `hz`.

        Parameters:
            hz: Elliptical cylinder height vector z component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if hz is not None:
            if isinstance(hz, types.Real):
                hz = hz
            elif isinstance(hz, int) or isinstance(hz, float):
                hz = types.Real(hz)
            elif isinstance(hz, str):
                hz = types.Real.from_mcnp(hz)

        if hz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, hz)

        self._hz: types.Real = hz

    @property
    def v1x(self) -> types.Real:
        """
        Elliptical cylinder major axis vector x component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._v1x

    @v1x.setter
    def v1x(self, v1x: str | int | float | types.Real) -> None:
        """
        Sets `v1x`.

        Parameters:
            v1x: Elliptical cylinder major axis vector x component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if v1x is not None:
            if isinstance(v1x, types.Real):
                v1x = v1x
            elif isinstance(v1x, int) or isinstance(v1x, float):
                v1x = types.Real(v1x)
            elif isinstance(v1x, str):
                v1x = types.Real.from_mcnp(v1x)

        if v1x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v1x)

        self._v1x: types.Real = v1x

    @property
    def v1y(self) -> types.Real:
        """
        Elliptical cylinder major axis vector y component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._v1y

    @v1y.setter
    def v1y(self, v1y: str | int | float | types.Real) -> None:
        """
        Sets `v1y`.

        Parameters:
            v1y: Elliptical cylinder major axis vector y component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if v1y is not None:
            if isinstance(v1y, types.Real):
                v1y = v1y
            elif isinstance(v1y, int) or isinstance(v1y, float):
                v1y = types.Real(v1y)
            elif isinstance(v1y, str):
                v1y = types.Real.from_mcnp(v1y)

        if v1y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v1y)

        self._v1y: types.Real = v1y

    @property
    def v1z(self) -> types.Real:
        """
        Elliptical cylinder major axis vector z component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._v1z

    @v1z.setter
    def v1z(self, v1z: str | int | float | types.Real) -> None:
        """
        Sets `v1z`.

        Parameters:
            v1z: Elliptical cylinder major axis vector z component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if v1z is not None:
            if isinstance(v1z, types.Real):
                v1z = v1z
            elif isinstance(v1z, int) or isinstance(v1z, float):
                v1z = types.Real(v1z)
            elif isinstance(v1z, str):
                v1z = types.Real.from_mcnp(v1z)

        if v1z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v1z)

        self._v1z: types.Real = v1z

    @property
    def v2x(self) -> types.Real:
        """
        Elliptical cylinder minor axis vector x component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._v2x

    @v2x.setter
    def v2x(self, v2x: str | int | float | types.Real) -> None:
        """
        Sets `v2x`.

        Parameters:
            v2x: Elliptical cylinder minor axis vector x component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if v2x is not None:
            if isinstance(v2x, types.Real):
                v2x = v2x
            elif isinstance(v2x, int) or isinstance(v2x, float):
                v2x = types.Real(v2x)
            elif isinstance(v2x, str):
                v2x = types.Real.from_mcnp(v2x)

        if v2x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v2x)

        self._v2x: types.Real = v2x

    @property
    def v2y(self) -> types.Real:
        """
        Elliptical cylinder minor axis vector y component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._v2y

    @v2y.setter
    def v2y(self, v2y: str | int | float | types.Real) -> None:
        """
        Sets `v2y`.

        Parameters:
            v2y: Elliptical cylinder minor axis vector y component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if v2y is not None:
            if isinstance(v2y, types.Real):
                v2y = v2y
            elif isinstance(v2y, int) or isinstance(v2y, float):
                v2y = types.Real(v2y)
            elif isinstance(v2y, str):
                v2y = types.Real.from_mcnp(v2y)

        self._v2y: types.Real = v2y

    @property
    def v2z(self) -> types.Real:
        """
        Elliptical cylinder minor axis vector z component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._v2z

    @v2z.setter
    def v2z(self, v2z: str | int | float | types.Real) -> None:
        """
        Sets `v2z`.

        Parameters:
            v2z: Elliptical cylinder minor axis vector z component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if v2z is not None:
            if isinstance(v2z, types.Real):
                v2z = v2z
            elif isinstance(v2z, int) or isinstance(v2z, float):
                v2z = types.Real(v2z)
            elif isinstance(v2z, str):
                v2z = types.Real.from_mcnp(v2z)

        self._v2z: types.Real = v2z
