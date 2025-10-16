import re

import numpy

from . import _option
from ... import types
from ... import errors


class Wed(_option.SurfaceOption):
    """
    Represents INP `wed` elements.
    """

    _KEYWORD = 'wed'

    _ATTRS = {
        'vx': types.Real,
        'vy': types.Real,
        'vz': types.Real,
        'v1x': types.Real,
        'v1y': types.Real,
        'v1z': types.Real,
        'v2x': types.Real,
        'v2y': types.Real,
        'v2z': types.Real,
        'v3x': types.Real,
        'v3y': types.Real,
        'v3z': types.Real,
    }

    _REGEX = re.compile(
        rf'\Awed( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        vx: str | int | float | types.Real,
        vy: str | int | float | types.Real,
        vz: str | int | float | types.Real,
        v1x: str | int | float | types.Real,
        v1y: str | int | float | types.Real,
        v1z: str | int | float | types.Real,
        v2x: str | int | float | types.Real,
        v2y: str | int | float | types.Real,
        v2z: str | int | float | types.Real,
        v3x: str | int | float | types.Real,
        v3y: str | int | float | types.Real,
        v3z: str | int | float | types.Real,
    ):
        """
        Initializes `Wed`.

        Parameters:
            vx: Wedge position vector x component.
            vy: Wedge position vector y component.
            vz: Wedge position vector z component.
            v1x: Wedge side vector #1 x component.
            v1y: Wedge side vector #1 y component.
            v1z: Wedge side vector #1 z component.
            v2x: Wedge side vector #2 x component.
            v2y: Wedge side vector #2 y component.
            v2z: Wedge side vector #2 z component.
            v3x: Wedge height vector x component.
            v3y: Wedge height vector y component.
            v3z: Wedge height vector z component.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.vx: types.Real = vx
        self.vy: types.Real = vy
        self.vz: types.Real = vz
        self.v1x: types.Real = v1x
        self.v1y: types.Real = v1y
        self.v1z: types.Real = v1z
        self.v2x: types.Real = v2x
        self.v2y: types.Real = v2y
        self.v2z: types.Real = v2z
        self.v3x: types.Real = v3x
        self.v3y: types.Real = v3y
        self.v3z: types.Real = v3z

    @property
    def vx(self) -> types.Real:
        """
        Wedge position vector x component

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
            vx: Wedge position vector x component.

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
        Wedge position vector y component

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
            vy: Wedge position vector y component.

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
        Wedge position vector z component

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
            vz: Wedge position vector z component.

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
    def v1x(self) -> types.Real:
        """
        Wedge side vector #1 x component

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
            v1x: Wedge side vector #1 x component.

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
        Wedge side vector #1 y component

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
            v1y: Wedge side vector #1 y component.

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
        Wedge side vector #1 z component

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
            v1z: Wedge side vector #1 z component.

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
        Wedge side vector #2 x component

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
            v2x: Wedge side vector #2 x component.

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
        Wedge side vector #2 y component

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
            v2y: Wedge side vector #2 y component.

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

        if v2y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v2y)

        self._v2y: types.Real = v2y

    @property
    def v2z(self) -> types.Real:
        """
        Wedge side vector #2 z component

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
            v2z: Wedge side vector #2 z component.

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

        if v2z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v2z)

        self._v2z: types.Real = v2z

    @property
    def v3x(self) -> types.Real:
        """
        Wedge height vector x component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._v3x

    @v3x.setter
    def v3x(self, v3x: str | int | float | types.Real) -> None:
        """
        Sets `v3x`.

        Parameters:
            v3x: Wedge height vector x component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if v3x is not None:
            if isinstance(v3x, types.Real):
                v3x = v3x
            elif isinstance(v3x, int) or isinstance(v3x, float):
                v3x = types.Real(v3x)
            elif isinstance(v3x, str):
                v3x = types.Real.from_mcnp(v3x)

        if v3x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v3x)

        self._v3x: types.Real = v3x

    @property
    def v3y(self) -> types.Real:
        """
        Wedge height vector y component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._v3y

    @v3y.setter
    def v3y(self, v3y: str | int | float | types.Real) -> None:
        """
        Sets `v3y`.

        Parameters:
            v3y: Wedge height vector y component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if v3y is not None:
            if isinstance(v3y, types.Real):
                v3y = v3y
            elif isinstance(v3y, int) or isinstance(v3y, float):
                v3y = types.Real(v3y)
            elif isinstance(v3y, str):
                v3y = types.Real.from_mcnp(v3y)

        if v3y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v3y)

        self._v3y: types.Real = v3y

    @property
    def v3z(self) -> types.Real:
        """
        Wedge height vector z component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._v3z

    @v3z.setter
    def v3z(self, v3z: str | int | float | types.Real) -> None:
        """
        Sets `v3z`.

        Parameters:
            v3z: Wedge height vector z component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if v3z is not None:
            if isinstance(v3z, types.Real):
                v3z = v3z
            elif isinstance(v3z, int) or isinstance(v3z, float):
                v3z = types.Real(v3z)
            elif isinstance(v3z, str):
                v3z = types.Real.from_mcnp(v3z)

        if v3z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, v3z)

        self._v3z: types.Real = v3z
