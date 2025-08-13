import re

from . import _entry
from ... import types
from ... import errors


class Sphere(_entry.FEntry_1):
    """
    Represents INP `sphere` elements.
    """

    _KEYWORD = ''

    _ATTRS = {
        'x': types.Real,
        'y': types.Real,
        'z': types.Integer,
        'ro': types.Integer,
    }

    _REGEX = re.compile(rf'\A({types.Real._REGEX.pattern[2:-2]}) ({types.Real._REGEX.pattern[2:-2]}) ({types.Integer._REGEX.pattern[2:-2]}) ({types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, x: str | int | float | types.Real, y: str | int | float | types.Real, z: str | int | types.Integer, ro: str | int | types.Integer):
        """
        Initializes `Sphere`.

        Parameters:
            x: Vector x coordinate.
            y: Vector y coordinate.
            z: Vector z coordinate.
            ro: Sphere exclusion radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.x: types.Real = x
        self.y: types.Real = y
        self.z: types.Integer = z
        self.ro: types.Integer = ro

    @property
    def x(self) -> types.Real:
        """
        Vector x coordinate

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
            x: Vector x coordinate.

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
    def y(self) -> types.Real:
        """
        Vector y coordinate

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
            y: Vector y coordinate.

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
    def z(self) -> types.Integer:
        """
        Vector z coordinate

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._z

    @z.setter
    def z(self, z: str | int | types.Integer) -> None:
        """
        Sets `z`.

        Parameters:
            z: Vector z coordinate.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if z is not None:
            if isinstance(z, types.Integer):
                z = z
            elif isinstance(z, int):
                z = types.Integer(z)
            elif isinstance(z, str):
                z = types.Integer.from_mcnp(z)

        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z)

        self._z: types.Integer = z

    @property
    def ro(self) -> types.Integer:
        """
        Sphere exclusion radius

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._ro

    @ro.setter
    def ro(self, ro: str | int | types.Integer) -> None:
        """
        Sets `ro`.

        Parameters:
            ro: Sphere exclusion radius.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if ro is not None:
            if isinstance(ro, types.Integer):
                ro = ro
            elif isinstance(ro, int):
                ro = types.Integer(ro)
            elif isinstance(ro, str):
                ro = types.Integer.from_mcnp(ro)

        if ro is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, ro)

        self._ro: types.Integer = ro
