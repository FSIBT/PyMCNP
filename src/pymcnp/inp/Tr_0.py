import re

from . import _card
from .. import types
from .. import errors


class Tr_0(_card.Card):
    """
    Represents INP `tr` elements variation #0.
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
        'yx': types.Real,
        'yy': types.Real,
        'yz': types.Real,
        'zx': types.Real,
        'zy': types.Real,
        'zz': types.Real,
        'system': types.Integer,
    }

    _REGEX = re.compile(
        rf'\A([*])?tr(\d+)( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})?\Z',
        re.IGNORECASE,
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
        yx: str | int | float | types.Real,
        yy: str | int | float | types.Real,
        yz: str | int | float | types.Real,
        zx: str | int | float | types.Real,
        zy: str | int | float | types.Real,
        zz: str | int | float | types.Real,
        prefix: str | types.String = None,
        system: str | int | types.Integer = None,
    ):
        """
        Initializes `Tr_0`.

        Parameters:
            prefix: Star prefix.
            suffix: Data card option suffix.
            x: Displacement vector x component.
            y: Displacement vector y component.
            z: Displacement vector z component.
            xx: Rotation matrix xx' component.
            xy: Rotation matrix xy' component.
            xz: Rotation matrix xz' component.
            yx: Rotation matrix yx' component.
            yy: Rotation matrix yy' component.
            yz: Rotation matrix yz' component.
            zx: Rotation matrix zx' component.
            zy: Rotation matrix zy' component.
            zz: Rotation matrix zz' component.
            system: Coordinate system setting.

        Raises:
            InpError: SEMANTICS_CARD.
        """

        self.prefix: types.String = prefix
        self.suffix: types.Integer = suffix
        self.x: types.Real = x
        self.y: types.Real = y
        self.z: types.Real = z
        self.xx: types.Real = xx
        self.xy: types.Real = xy
        self.xz: types.Real = xz
        self.yx: types.Real = yx
        self.yy: types.Real = yy
        self.yz: types.Real = yz
        self.zx: types.Real = zx
        self.zy: types.Real = zy
        self.zz: types.Real = zz
        self.system: types.Integer = system

    @property
    def prefix(self) -> types.String:
        """
        Star prefix

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._prefix

    @prefix.setter
    def prefix(self, prefix: str | types.String) -> None:
        """
        Sets `prefix`.

        Parameters:
            prefix: Star prefix.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if prefix is not None:
            if isinstance(prefix, types.String):
                prefix = prefix
            elif isinstance(prefix, str):
                prefix = types.String.from_mcnp(prefix)

        if prefix is not None and prefix.value.lower() not in {'*'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, prefix)

        self._prefix: types.String = prefix

    @property
    def suffix(self) -> types.Integer:
        """
        Data card option suffix

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._suffix

    @suffix.setter
    def suffix(self, suffix: str | int | types.Integer) -> None:
        """
        Sets `suffix`.

        Parameters:
            suffix: Data card option suffix.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if suffix is not None:
            if isinstance(suffix, types.Integer):
                suffix = suffix
            elif isinstance(suffix, int):
                suffix = types.Integer(suffix)
            elif isinstance(suffix, str):
                suffix = types.Integer.from_mcnp(suffix)

        if suffix is None or not (suffix >= 1 and suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, suffix)

        self._suffix: types.Integer = suffix

    @property
    def x(self) -> types.Real:
        """
        Displacement vector x component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._x

    @x.setter
    def x(self, x: str | int | float | types.Real) -> None:
        """
        Sets `x`.

        Parameters:
            x: Displacement vector x component.

        Raises:
            InpError: SEMANTICS_CARD.
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
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, x)

        self._x: types.Real = x

    @property
    def y(self) -> types.Real:
        """
        Displacement vector y component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._y

    @y.setter
    def y(self, y: str | int | float | types.Real) -> None:
        """
        Sets `y`.

        Parameters:
            y: Displacement vector y component.

        Raises:
            InpError: SEMANTICS_CARD.
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
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, y)

        self._y: types.Real = y

    @property
    def z(self) -> types.Real:
        """
        Displacement vector z component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._z

    @z.setter
    def z(self, z: str | int | float | types.Real) -> None:
        """
        Sets `z`.

        Parameters:
            z: Displacement vector z component.

        Raises:
            InpError: SEMANTICS_CARD.
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
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, z)

        self._z: types.Real = z

    @property
    def xx(self) -> types.Real:
        """
        Rotation matrix xx' component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._xx

    @xx.setter
    def xx(self, xx: str | int | float | types.Real) -> None:
        """
        Sets `xx`.

        Parameters:
            xx: Rotation matrix xx' component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if xx is not None:
            if isinstance(xx, types.Real):
                xx = xx
            elif isinstance(xx, int) or isinstance(xx, float):
                xx = types.Real(xx)
            elif isinstance(xx, str):
                xx = types.Real.from_mcnp(xx)

        if xx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, xx)

        self._xx: types.Real = xx

    @property
    def xy(self) -> types.Real:
        """
        Rotation matrix xy' component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._xy

    @xy.setter
    def xy(self, xy: str | int | float | types.Real) -> None:
        """
        Sets `xy`.

        Parameters:
            xy: Rotation matrix xy' component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if xy is not None:
            if isinstance(xy, types.Real):
                xy = xy
            elif isinstance(xy, int) or isinstance(xy, float):
                xy = types.Real(xy)
            elif isinstance(xy, str):
                xy = types.Real.from_mcnp(xy)

        if xy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, xy)

        self._xy: types.Real = xy

    @property
    def xz(self) -> types.Real:
        """
        Rotation matrix xz' component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._xz

    @xz.setter
    def xz(self, xz: str | int | float | types.Real) -> None:
        """
        Sets `xz`.

        Parameters:
            xz: Rotation matrix xz' component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if xz is not None:
            if isinstance(xz, types.Real):
                xz = xz
            elif isinstance(xz, int) or isinstance(xz, float):
                xz = types.Real(xz)
            elif isinstance(xz, str):
                xz = types.Real.from_mcnp(xz)

        if xz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, xz)

        self._xz: types.Real = xz

    @property
    def yx(self) -> types.Real:
        """
        Rotation matrix yx' component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._yx

    @yx.setter
    def yx(self, yx: str | int | float | types.Real) -> None:
        """
        Sets `yx`.

        Parameters:
            yx: Rotation matrix yx' component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if yx is not None:
            if isinstance(yx, types.Real):
                yx = yx
            elif isinstance(yx, int) or isinstance(yx, float):
                yx = types.Real(yx)
            elif isinstance(yx, str):
                yx = types.Real.from_mcnp(yx)

        if yx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, yx)

        self._yx: types.Real = yx

    @property
    def yy(self) -> types.Real:
        """
        Rotation matrix yy' component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._yy

    @yy.setter
    def yy(self, yy: str | int | float | types.Real) -> None:
        """
        Sets `yy`.

        Parameters:
            yy: Rotation matrix yy' component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if yy is not None:
            if isinstance(yy, types.Real):
                yy = yy
            elif isinstance(yy, int) or isinstance(yy, float):
                yy = types.Real(yy)
            elif isinstance(yy, str):
                yy = types.Real.from_mcnp(yy)

        if yy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, yy)

        self._yy: types.Real = yy

    @property
    def yz(self) -> types.Real:
        """
        Rotation matrix yz' component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._yz

    @yz.setter
    def yz(self, yz: str | int | float | types.Real) -> None:
        """
        Sets `yz`.

        Parameters:
            yz: Rotation matrix yz' component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if yz is not None:
            if isinstance(yz, types.Real):
                yz = yz
            elif isinstance(yz, int) or isinstance(yz, float):
                yz = types.Real(yz)
            elif isinstance(yz, str):
                yz = types.Real.from_mcnp(yz)

        if yz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, yz)

        self._yz: types.Real = yz

    @property
    def zx(self) -> types.Real:
        """
        Rotation matrix zx' component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._zx

    @zx.setter
    def zx(self, zx: str | int | float | types.Real) -> None:
        """
        Sets `zx`.

        Parameters:
            zx: Rotation matrix zx' component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if zx is not None:
            if isinstance(zx, types.Real):
                zx = zx
            elif isinstance(zx, int) or isinstance(zx, float):
                zx = types.Real(zx)
            elif isinstance(zx, str):
                zx = types.Real.from_mcnp(zx)

        if zx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, zx)

        self._zx: types.Real = zx

    @property
    def zy(self) -> types.Real:
        """
        Rotation matrix zy' component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._zy

    @zy.setter
    def zy(self, zy: str | int | float | types.Real) -> None:
        """
        Sets `zy`.

        Parameters:
            zy: Rotation matrix zy' component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if zy is not None:
            if isinstance(zy, types.Real):
                zy = zy
            elif isinstance(zy, int) or isinstance(zy, float):
                zy = types.Real(zy)
            elif isinstance(zy, str):
                zy = types.Real.from_mcnp(zy)

        if zy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, zy)

        self._zy: types.Real = zy

    @property
    def zz(self) -> types.Real:
        """
        Rotation matrix zz' component

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._zz

    @zz.setter
    def zz(self, zz: str | int | float | types.Real) -> None:
        """
        Sets `zz`.

        Parameters:
            zz: Rotation matrix zz' component.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if zz is not None:
            if isinstance(zz, types.Real):
                zz = zz
            elif isinstance(zz, int) or isinstance(zz, float):
                zz = types.Real(zz)
            elif isinstance(zz, str):
                zz = types.Real.from_mcnp(zz)

        if zz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, zz)

        self._zz: types.Real = zz

    @property
    def system(self) -> types.Integer:
        """
        Coordinate system setting

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        return self._system

    @system.setter
    def system(self, system: str | int | types.Integer) -> None:
        """
        Sets `system`.

        Parameters:
            system: Coordinate system setting.

        Raises:
            InpError: SEMANTICS_CARD.
            TypeError:
        """

        if system is not None:
            if isinstance(system, types.Integer):
                system = system
            elif isinstance(system, int):
                system = types.Integer(system)
            elif isinstance(system, str):
                system = types.Integer.from_mcnp(system)

        if system is not None and not (system == -1 or system == 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_CARD, system)

        self._system: types.Integer = system
