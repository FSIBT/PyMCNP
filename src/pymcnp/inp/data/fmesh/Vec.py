import re

from . import _option
from .... import types
from .... import errors


class Vec(_option.FmeshOption):
    """
    Represents INP vec elements.
    """

    _KEYWORD = 'vec'

    _ATTRS = {
        'x': types.Real,
        'y': types.Real,
        'z': types.Real,
    }

    _REGEX = re.compile(rf'\Avec( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, x: str | int | float | types.Real, y: str | int | float | types.Real, z: str | int | float | types.Real):
        """
        Initializes ``Vec``.

        Parameters:
            x: Plane vector x component.
            y: Plane vector y component.
            z: Plane vector z component.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.x: types.Real = x
        self.y: types.Real = y
        self.z: types.Real = z

    @property
    def x(self) -> types.Real:
        """
        Plane vector x component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._x

    @x.setter
    def x(self, x: str | int | float | types.Real) -> None:
        """
        Sets ``x``.

        Parameters:
            x: Plane vector x component.

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
        Plane vector y component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._y

    @y.setter
    def y(self, y: str | int | float | types.Real) -> None:
        """
        Sets ``y``.

        Parameters:
            y: Plane vector y component.

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
        Plane vector z component

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._z

    @z.setter
    def z(self, z: str | int | float | types.Real) -> None:
        """
        Sets ``z``.

        Parameters:
            z: Plane vector z component.

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
