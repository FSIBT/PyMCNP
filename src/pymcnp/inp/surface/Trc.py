import re

import numpy

from . import _option
from ... import types
from ... import errors


class Trc(_option.SurfaceOption):
    """
    Represents INP `trc` elements.
    """

    _KEYWORD = 'trc'

    _ATTRS = {
        'vx': types.Real,
        'vy': types.Real,
        'vz': types.Real,
        'hx': types.Real,
        'hy': types.Real,
        'hz': types.Real,
        'r1': types.Real,
        'r2': types.Real,
    }

    _REGEX = re.compile(
        rf'\Atrc( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
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
        r1: str | int | float | types.Real,
        r2: str | int | float | types.Real,
    ):
        """
        Initializes `Trc`.

        Parameters:
            vx: Truncated cone position vector x component.
            vy: Truncated cone position vector y component.
            vz: Truncated cone position vector z component.
            hx: Truncated cone height vector x component.
            hy: Truncated cone height vector y component.
            hz: Truncated cone height vector z component.
            r1: Truncated cone lower cone radius.
            r2: Truncated cone upper cone radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.vx: types.Real = vx
        self.vy: types.Real = vy
        self.vz: types.Real = vz
        self.hx: types.Real = hx
        self.hy: types.Real = hy
        self.hz: types.Real = hz
        self.r1: types.Real = r1
        self.r2: types.Real = r2

    @property
    def vx(self) -> types.Real:
        """
        Truncated cone position vector x component

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
            vx: Truncated cone position vector x component.

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
        Truncated cone position vector y component

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
            vy: Truncated cone position vector y component.

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
        Truncated cone position vector z component

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
            vz: Truncated cone position vector z component.

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
        Truncated cone height vector x component

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
            hx: Truncated cone height vector x component.

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
        Truncated cone height vector y component

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
            hy: Truncated cone height vector y component.

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
        Truncated cone height vector z component

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
            hz: Truncated cone height vector z component.

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
    def r1(self) -> types.Real:
        """
        Truncated cone lower cone radius

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._r1

    @r1.setter
    def r1(self, r1: str | int | float | types.Real) -> None:
        """
        Sets `r1`.

        Parameters:
            r1: Truncated cone lower cone radius.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if r1 is not None:
            if isinstance(r1, types.Real):
                r1 = r1
            elif isinstance(r1, int) or isinstance(r1, float):
                r1 = types.Real(r1)
            elif isinstance(r1, str):
                r1 = types.Real.from_mcnp(r1)

        if r1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, r1)

        self._r1: types.Real = r1

    @property
    def r2(self) -> types.Real:
        """
        Truncated cone upper cone radius

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._r2

    @r2.setter
    def r2(self, r2: str | int | float | types.Real) -> None:
        """
        Sets `r2`.

        Parameters:
            r2: Truncated cone upper cone radius.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if r2 is not None:
            if isinstance(r2, types.Real):
                r2 = r2
            elif isinstance(r2, int) or isinstance(r2, float):
                r2 = types.Real(r2)
            elif isinstance(r2, str):
                r2 = types.Real.from_mcnp(r2)

        if r2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, r2)

        self._r2: types.Real = r2
