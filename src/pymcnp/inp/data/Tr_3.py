import re

from . import _option
from ...utils import types
from ...utils import errors


class Tr_3(_option.DataOption):
    """
    Represents INP tr variation #3 elements.

    Attributes:
        prefix: Star prefix.
        suffix: Data card option suffix.
        x: Displacement vector x component.
        y: Displacement vector y component.
        z: Displacement vector z component.
        xx: Rotation matrix xx' component.
        xy: Rotation matrix xy' component.
        xz: Rotation matrix xz' component.
        system: Coordinate system setting.
    """

    _KEYWORD = 'tr'

    _ATTRS = {
        'prefix': types.String,
        'suffix': types.Integer,
        'x': types.Real,
        'y': types.Real,
        'z': types.Real,
        'xx': types.Real,
        'xy': types.Real,
        'xz': types.Real,
        'system': types.Integer,
    }

    _REGEX = re.compile(
        rf'\A([*])?tr(\d+)( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})?\Z'
    )

    def __init__(
        self,
        suffix: str | int | types.Integer,
        x: str | int | float | types.Real,
        y: str | int | float | types.Real,
        z: str | int | float | types.Real,
        xx: str | int | float | types.Real,
        xy: str | int | float | types.Real,
        xz: str | int | float | types.Real,
        prefix: str | types.String = None,
        system: str | int | types.Integer = None,
    ):
        """
        Initializes ``Tr_3``.

        Parameters:
            prefix: Star prefix.
            suffix: Data card option suffix.
            x: Displacement vector x component.
            y: Displacement vector y component.
            z: Displacement vector z component.
            xx: Rotation matrix xx' component.
            xy: Rotation matrix xy' component.
            xz: Rotation matrix xz' component.
            system: Coordinate system setting.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.prefix: types.String = prefix
        self.suffix: types.Integer = suffix
        self.x: types.Real = x
        self.y: types.Real = y
        self.z: types.Real = z
        self.xx: types.Real = xx
        self.xy: types.Real = xy
        self.xz: types.Real = xz
        self.system: types.Integer = system

    @property
    def prefix(self) -> types.String:
        """
        Gets ``prefix``.

        Returns:
            ``prefix``.
        """

        return self._prefix

    @prefix.setter
    def prefix(self, prefix: str | types.String) -> None:
        """
        Sets ``prefix``.

        Parameters:
            prefix: Star prefix.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if prefix is not None:
            if isinstance(prefix, types.String):
                prefix = prefix
            elif isinstance(prefix, str):
                prefix = types.String.from_mcnp(prefix)
            else:
                raise TypeError

        if prefix is not None and prefix not in {'*'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, prefix)

        self._prefix: types.String = prefix

    @property
    def suffix(self) -> types.Integer:
        """
        Gets ``suffix``.

        Returns:
            ``suffix``.
        """

        return self._suffix

    @suffix.setter
    def suffix(self, suffix: str | int | types.Integer) -> None:
        """
        Sets ``suffix``.

        Parameters:
            suffix: Data card option suffix.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if suffix is not None:
            if isinstance(suffix, types.Integer):
                suffix = suffix
            elif isinstance(suffix, int):
                suffix = types.Integer(suffix)
            elif isinstance(suffix, str):
                suffix = types.Integer.from_mcnp(suffix)
            else:
                raise TypeError

        if suffix is None or not (suffix >= 1 and suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)

        self._suffix: types.Integer = suffix

    @property
    def x(self) -> types.Real:
        """
        Gets ``x``.

        Returns:
            ``x``.
        """

        return self._x

    @x.setter
    def x(self, x: str | int | float | types.Real) -> None:
        """
        Sets ``x``.

        Parameters:
            x: Displacement vector x component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if x is not None:
            if isinstance(x, types.Real):
                x = x
            elif isinstance(x, int):
                x = types.Real(x)
            elif isinstance(x, float):
                x = types.Real(x)
            elif isinstance(x, str):
                x = types.Real.from_mcnp(x)
            else:
                raise TypeError

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x)

        self._x: types.Real = x

    @property
    def y(self) -> types.Real:
        """
        Gets ``y``.

        Returns:
            ``y``.
        """

        return self._y

    @y.setter
    def y(self, y: str | int | float | types.Real) -> None:
        """
        Sets ``y``.

        Parameters:
            y: Displacement vector y component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if y is not None:
            if isinstance(y, types.Real):
                y = y
            elif isinstance(y, int):
                y = types.Real(y)
            elif isinstance(y, float):
                y = types.Real(y)
            elif isinstance(y, str):
                y = types.Real.from_mcnp(y)
            else:
                raise TypeError

        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y)

        self._y: types.Real = y

    @property
    def z(self) -> types.Real:
        """
        Gets ``z``.

        Returns:
            ``z``.
        """

        return self._z

    @z.setter
    def z(self, z: str | int | float | types.Real) -> None:
        """
        Sets ``z``.

        Parameters:
            z: Displacement vector z component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if z is not None:
            if isinstance(z, types.Real):
                z = z
            elif isinstance(z, int):
                z = types.Real(z)
            elif isinstance(z, float):
                z = types.Real(z)
            elif isinstance(z, str):
                z = types.Real.from_mcnp(z)
            else:
                raise TypeError

        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z)

        self._z: types.Real = z

    @property
    def xx(self) -> types.Real:
        """
        Gets ``xx``.

        Returns:
            ``xx``.
        """

        return self._xx

    @xx.setter
    def xx(self, xx: str | int | float | types.Real) -> None:
        """
        Sets ``xx``.

        Parameters:
            xx: Rotation matrix xx' component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if xx is not None:
            if isinstance(xx, types.Real):
                xx = xx
            elif isinstance(xx, int):
                xx = types.Real(xx)
            elif isinstance(xx, float):
                xx = types.Real(xx)
            elif isinstance(xx, str):
                xx = types.Real.from_mcnp(xx)
            else:
                raise TypeError

        if xx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, xx)

        self._xx: types.Real = xx

    @property
    def xy(self) -> types.Real:
        """
        Gets ``xy``.

        Returns:
            ``xy``.
        """

        return self._xy

    @xy.setter
    def xy(self, xy: str | int | float | types.Real) -> None:
        """
        Sets ``xy``.

        Parameters:
            xy: Rotation matrix xy' component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if xy is not None:
            if isinstance(xy, types.Real):
                xy = xy
            elif isinstance(xy, int):
                xy = types.Real(xy)
            elif isinstance(xy, float):
                xy = types.Real(xy)
            elif isinstance(xy, str):
                xy = types.Real.from_mcnp(xy)
            else:
                raise TypeError

        if xy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, xy)

        self._xy: types.Real = xy

    @property
    def xz(self) -> types.Real:
        """
        Gets ``xz``.

        Returns:
            ``xz``.
        """

        return self._xz

    @xz.setter
    def xz(self, xz: str | int | float | types.Real) -> None:
        """
        Sets ``xz``.

        Parameters:
            xz: Rotation matrix xz' component.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if xz is not None:
            if isinstance(xz, types.Real):
                xz = xz
            elif isinstance(xz, int):
                xz = types.Real(xz)
            elif isinstance(xz, float):
                xz = types.Real(xz)
            elif isinstance(xz, str):
                xz = types.Real.from_mcnp(xz)
            else:
                raise TypeError

        if xz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, xz)

        self._xz: types.Real = xz

    @property
    def system(self) -> types.Integer:
        """
        Gets ``system``.

        Returns:
            ``system``.
        """

        return self._system

    @system.setter
    def system(self, system: str | int | types.Integer) -> None:
        """
        Sets ``system``.

        Parameters:
            system: Coordinate system setting.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if system is not None:
            if isinstance(system, types.Integer):
                system = system
            elif isinstance(system, int):
                system = types.Integer(system)
            elif isinstance(system, str):
                system = types.Integer.from_mcnp(system)
            else:
                raise TypeError

        if system is not None and not (system == -1 or system == 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, system)

        self._system: types.Integer = system
