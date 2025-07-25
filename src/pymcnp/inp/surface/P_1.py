import re

import numpy

from . import _option
from ... import _show
from ... import types
from ... import errors


class P_1(_option.SurfaceOption):
    """
    Represents INP p variation #1 elements.
    """

    _KEYWORD = 'p'

    _ATTRS = {
        'x1': types.Real,
        'y1': types.Real,
        'z1': types.Real,
        'x2': types.Real,
        'y2': types.Real,
        'z2': types.Real,
        'x3': types.Real,
        'y3': types.Real,
        'z3': types.Real,
    }

    _REGEX = re.compile(
        rf'\Ap( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )

    def __init__(
        self,
        x1: str | int | float | types.Real,
        y1: str | int | float | types.Real,
        z1: str | int | float | types.Real,
        x2: str | int | float | types.Real,
        y2: str | int | float | types.Real,
        z2: str | int | float | types.Real,
        x3: str | int | float | types.Real,
        y3: str | int | float | types.Real,
        z3: str | int | float | types.Real,
    ):
        """
        Initializes ``P_1``.

        Parameters:
            x1: point-defined general plane x-coordinate #1.
            y1: point-defined general plane y-coordinate #1.
            z1: point-defined general plane z-coordinate #1.
            x2: point-defined general plane x-coordinate #2.
            y2: point-defined general plane y-coordinate #2.
            z2: point-defined general plane z-coordinate #2.
            x3: point-defined general plane x-coordinate #3.
            y3: point-defined general plane y-coordinate #3.
            z3: point-defined general plane z-coordinate #3.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.x1: types.Real = x1
        self.y1: types.Real = y1
        self.z1: types.Real = z1
        self.x2: types.Real = x2
        self.y2: types.Real = y2
        self.z2: types.Real = z2
        self.x3: types.Real = x3
        self.y3: types.Real = y3
        self.z3: types.Real = z3

    @property
    def x1(self) -> types.Real:
        """
        Point-defined general plane x-coordinate #1

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._x1

    @x1.setter
    def x1(self, x1: str | int | float | types.Real) -> None:
        """
        Sets ``x1``.

        Parameters:
            x1: point-defined general plane x-coordinate #1.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if x1 is not None:
            if isinstance(x1, types.Real):
                x1 = x1
            elif isinstance(x1, int) or isinstance(x1, float):
                x1 = types.Real(x1)
            elif isinstance(x1, str):
                x1 = types.Real.from_mcnp(x1)

        if x1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x1)

        self._x1: types.Real = x1

    @property
    def y1(self) -> types.Real:
        """
        Point-defined general plane y-coordinate #1

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._y1

    @y1.setter
    def y1(self, y1: str | int | float | types.Real) -> None:
        """
        Sets ``y1``.

        Parameters:
            y1: point-defined general plane y-coordinate #1.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if y1 is not None:
            if isinstance(y1, types.Real):
                y1 = y1
            elif isinstance(y1, int) or isinstance(y1, float):
                y1 = types.Real(y1)
            elif isinstance(y1, str):
                y1 = types.Real.from_mcnp(y1)

        if y1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y1)

        self._y1: types.Real = y1

    @property
    def z1(self) -> types.Real:
        """
        Point-defined general plane z-coordinate #1

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._z1

    @z1.setter
    def z1(self, z1: str | int | float | types.Real) -> None:
        """
        Sets ``z1``.

        Parameters:
            z1: point-defined general plane z-coordinate #1.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if z1 is not None:
            if isinstance(z1, types.Real):
                z1 = z1
            elif isinstance(z1, int) or isinstance(z1, float):
                z1 = types.Real(z1)
            elif isinstance(z1, str):
                z1 = types.Real.from_mcnp(z1)

        if z1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z1)

        self._z1: types.Real = z1

    @property
    def x2(self) -> types.Real:
        """
        Point-defined general plane x-coordinate #2

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._x2

    @x2.setter
    def x2(self, x2: str | int | float | types.Real) -> None:
        """
        Sets ``x2``.

        Parameters:
            x2: point-defined general plane x-coordinate #2.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if x2 is not None:
            if isinstance(x2, types.Real):
                x2 = x2
            elif isinstance(x2, int) or isinstance(x2, float):
                x2 = types.Real(x2)
            elif isinstance(x2, str):
                x2 = types.Real.from_mcnp(x2)

        if x2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x2)

        self._x2: types.Real = x2

    @property
    def y2(self) -> types.Real:
        """
        Point-defined general plane y-coordinate #2

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._y2

    @y2.setter
    def y2(self, y2: str | int | float | types.Real) -> None:
        """
        Sets ``y2``.

        Parameters:
            y2: point-defined general plane y-coordinate #2.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if y2 is not None:
            if isinstance(y2, types.Real):
                y2 = y2
            elif isinstance(y2, int) or isinstance(y2, float):
                y2 = types.Real(y2)
            elif isinstance(y2, str):
                y2 = types.Real.from_mcnp(y2)

        if y2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y2)

        self._y2: types.Real = y2

    @property
    def z2(self) -> types.Real:
        """
        Point-defined general plane z-coordinate #2

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._z2

    @z2.setter
    def z2(self, z2: str | int | float | types.Real) -> None:
        """
        Sets ``z2``.

        Parameters:
            z2: point-defined general plane z-coordinate #2.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if z2 is not None:
            if isinstance(z2, types.Real):
                z2 = z2
            elif isinstance(z2, int) or isinstance(z2, float):
                z2 = types.Real(z2)
            elif isinstance(z2, str):
                z2 = types.Real.from_mcnp(z2)

        if z2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z2)

        self._z2: types.Real = z2

    @property
    def x3(self) -> types.Real:
        """
        Point-defined general plane x-coordinate #3

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._x3

    @x3.setter
    def x3(self, x3: str | int | float | types.Real) -> None:
        """
        Sets ``x3``.

        Parameters:
            x3: point-defined general plane x-coordinate #3.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if x3 is not None:
            if isinstance(x3, types.Real):
                x3 = x3
            elif isinstance(x3, int) or isinstance(x3, float):
                x3 = types.Real(x3)
            elif isinstance(x3, str):
                x3 = types.Real.from_mcnp(x3)

        if x3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x3)

        self._x3: types.Real = x3

    @property
    def y3(self) -> types.Real:
        """
        Point-defined general plane y-coordinate #3

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._y3

    @y3.setter
    def y3(self, y3: str | int | float | types.Real) -> None:
        """
        Sets ``y3``.

        Parameters:
            y3: point-defined general plane y-coordinate #3.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if y3 is not None:
            if isinstance(y3, types.Real):
                y3 = y3
            elif isinstance(y3, int) or isinstance(y3, float):
                y3 = types.Real(y3)
            elif isinstance(y3, str):
                y3 = types.Real.from_mcnp(y3)

        if y3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y3)

        self._y3: types.Real = y3

    @property
    def z3(self) -> types.Real:
        """
        Point-defined general plane z-coordinate #3

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._z3

    @z3.setter
    def z3(self, z3: str | int | float | types.Real) -> None:
        """
        Sets ``z3``.

        Parameters:
            z3: point-defined general plane z-coordinate #3.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if z3 is not None:
            if isinstance(z3, types.Real):
                z3 = z3
            elif isinstance(z3, int) or isinstance(z3, float):
                z3 = types.Real(z3)
            elif isinstance(z3, str):
                z3 = types.Real.from_mcnp(z3)

        if z3 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z3)

        self._z3: types.Real = z3

    def draw(self, shapes: _show.Endpoint = _show.pyvista) -> _show.Shape:
        """
        Generates ``Visualization`` from ``P_1``.

        Parameters:
            shapes: Collection of shapes.

        Returns:
            ``_show.Shape`` for ``P_1``
        """

        a = numpy.array((float(self.x2 - self.x1), float(self.y2 - self.y1), float(self.z2 - self.z1)))
        b = numpy.array((float(self.x3 - self.x1), float(self.y3 - self.y1), float(self.z3 - self.z1)))
        n = numpy.cross(a, b)

        vis = shapes.Plane(n[0], n[1], n[2], n[0] * float(self.x1) + n[1] * float(self.y1) + n[2] * float(self.z1))

        return vis
