import re

import numpy

from . import _option
from ... import types
from ... import errors


class C_y(_option.SurfaceOption):
    """
    Represents INP `c/y` elements.
    """

    _KEYWORD = 'c/y'

    _ATTRS = {
        'x': types.Real,
        'z': types.Real,
        'r': types.Real,
    }

    _REGEX = re.compile(rf'\Ac/y( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, x: str | int | float | types.Real, z: str | int | float | types.Real, r: str | int | float | types.Real):
        """
        Initializes `C_y`.

        Parameters:
            x: Parallel-to-y-axis cylinder center x component.
            z: Parallel-to-y-axis cylinder center z component.
            r: Parallel-to-y-axis cylinder radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.x: types.Real = x
        self.z: types.Real = z
        self.r: types.Real = r

    @property
    def x(self) -> types.Real:
        """
        Parallel-to-y-axis cylinder center x component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._x

    @x.setter
    def x(self, x: str | int | float | types.Real) -> None:
        """
        Sets `x`.

        Parameters:
            x: Parallel-to-y-axis cylinder center x component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if x is not None:
            if isinstance(x, types.Real):
                x = x
            elif isinstance(x, int) or isinstance(x, float):
                x = types.Real(x)
            elif isinstance(x, str):
                x = types.Real.from_mcnp(x)

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x)

        self._x: types.Real = x

    @property
    def z(self) -> types.Real:
        """
        Parallel-to-y-axis cylinder center z component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._z

    @z.setter
    def z(self, z: str | int | float | types.Real) -> None:
        """
        Sets `z`.

        Parameters:
            z: Parallel-to-y-axis cylinder center z component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if z is not None:
            if isinstance(z, types.Real):
                z = z
            elif isinstance(z, int) or isinstance(z, float):
                z = types.Real(z)
            elif isinstance(z, str):
                z = types.Real.from_mcnp(z)

        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z)

        self._z: types.Real = z

    @property
    def r(self) -> types.Real:
        """
        Parallel-to-y-axis cylinder radius

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._r

    @r.setter
    def r(self, r: str | int | float | types.Real) -> None:
        """
        Sets `r`.

        Parameters:
            r: Parallel-to-y-axis cylinder radius.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if r is not None:
            if isinstance(r, types.Real):
                r = r
            elif isinstance(r, int) or isinstance(r, float):
                r = types.Real(r)
            elif isinstance(r, str):
                r = types.Real.from_mcnp(r)

        if r is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, r)

        self._r: types.Real = r
