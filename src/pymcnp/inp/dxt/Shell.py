import re

from . import _entry
from ... import types
from ... import errors


class Shell(_entry.DxtEntry):
    """
    Represents INP `shell` elements.
    """

    _KEYWORD = ''

    _ATTRS = {
        'x': types.Real,
        'y': types.Real,
        'z': types.Real,
        'inner_radius': types.Integer,
        'outer_radius': types.Integer,
    }

    _REGEX = re.compile(
        rf'\A({types.Real._REGEX.pattern[2:-2]}) ({types.Real._REGEX.pattern[2:-2]}) ({types.Real._REGEX.pattern[2:-2]}) ({types.Integer._REGEX.pattern[2:-2]}) ({types.Integer._REGEX.pattern[2:-2]})\Z',
        re.IGNORECASE,
    )

    def __init__(
        self, x: str | int | float | types.Real, y: str | int | float | types.Real, z: str | int | float | types.Real, inner_radius: str | int | types.Integer, outer_radius: str | int | types.Integer
    ):
        """
        Initializes `Shell`.

        Parameters:
            x: Vector x coordinate.
            y: Vector y coordinate.
            z: Vector z coordinate.
            inner_radius: Inner sphere radius.
            outer_radius: Outer sphere radius.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.x: types.Real = x
        self.y: types.Real = y
        self.z: types.Real = z
        self.inner_radius: types.Integer = inner_radius
        self.outer_radius: types.Integer = outer_radius

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
    def z(self) -> types.Real:
        """
        Vector z coordinate

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
            z: Vector z coordinate.

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
    def inner_radius(self) -> types.Integer:
        """
        Inner sphere radius

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._inner_radius

    @inner_radius.setter
    def inner_radius(self, inner_radius: str | int | types.Integer) -> None:
        """
        Sets `inner_radius`.

        Parameters:
            inner_radius: Inner sphere radius.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if inner_radius is not None:
            if isinstance(inner_radius, types.Integer):
                inner_radius = inner_radius
            elif isinstance(inner_radius, int):
                inner_radius = types.Integer(inner_radius)
            elif isinstance(inner_radius, str):
                inner_radius = types.Integer.from_mcnp(inner_radius)

        if inner_radius is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, inner_radius)

        self._inner_radius: types.Integer = inner_radius

    @property
    def outer_radius(self) -> types.Integer:
        """
        Outer sphere radius

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._outer_radius

    @outer_radius.setter
    def outer_radius(self, outer_radius: str | int | types.Integer) -> None:
        """
        Sets `outer_radius`.

        Parameters:
            outer_radius: Outer sphere radius.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if outer_radius is not None:
            if isinstance(outer_radius, types.Integer):
                outer_radius = outer_radius
            elif isinstance(outer_radius, int):
                outer_radius = types.Integer(outer_radius)
            elif isinstance(outer_radius, str):
                outer_radius = types.Integer.from_mcnp(outer_radius)

        if outer_radius is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, outer_radius)

        self._outer_radius: types.Integer = outer_radius
