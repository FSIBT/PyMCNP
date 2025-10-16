import re

import numpy

from . import _option
from ... import _show
from ... import types
from ... import errors


class C_x(_option.SurfaceOption):
    """
    Represents INP `c/x` elements.
    """

    _KEYWORD = 'c/x'

    _ATTRS = {
        'y': types.Real,
        'z': types.Real,
        'r': types.Real,
    }

    _REGEX = re.compile(rf'\Ac/x( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, y: str | int | float | types.Real, z: str | int | float | types.Real, r: str | int | float | types.Real):
        """
        Initializes `C_x`.

        Parameters:
            y: Parallel-to-x-axis cylinder center y component.
            z: Parallel-to-x-axis cylinder center z component.
            r: Parallel-to-x-axis cylinder radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.y: types.Real = y
        self.z: types.Real = z
        self.r: types.Real = r

    @property
    def y(self) -> types.Real:
        """
        Parallel-to-x-axis cylinder center y component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._y

    @y.setter
    def y(self, y: str | int | float | types.Real) -> None:
        """
        Sets `y`.

        Parameters:
            y: Parallel-to-x-axis cylinder center y component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if y is not None:
            if isinstance(y, types.Real):
                y = y
            elif isinstance(y, int) or isinstance(y, float):
                y = types.Real(y)
            elif isinstance(y, str):
                y = types.Real.from_mcnp(y)

        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y)

        self._y: types.Real = y

    @property
    def z(self) -> types.Real:
        """
        Parallel-to-x-axis cylinder center z component

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
            z: Parallel-to-x-axis cylinder center z component.

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
        Parallel-to-x-axis cylinder radius

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
            r: Parallel-to-x-axis cylinder radius.

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

    def to_show(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates `Visualization` from `C_x`.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            `_show.Shape` for `C_x`.
        """

        vis = shapes.CylinderUnbounded(float(self.r))
        vis = vis.rotate(numpy.array((0, 1, 0)), 90, (0, 0, 0))
        vis = vis.translate(numpy.array((0, float(self.y), float(self.z))))

        return vis
