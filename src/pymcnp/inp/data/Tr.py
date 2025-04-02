import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Tr(DataOption_, keyword='tr'):
    """
    Represents INP tr elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
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
        rf'\Atr(\d+)( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Integer._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        suffix: types.Integer,
        x: types.Real,
        y: types.Real,
        z: types.Real,
        xx: types.Real,
        xy: types.Real,
        xz: types.Real,
        yx: types.Real,
        yy: types.Real,
        yz: types.Real,
        zx: types.Real,
        zy: types.Real,
        zz: types.Real,
        system: types.Integer,
    ):
        """
        Initializes ``Tr``.

        Parameters:
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
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None or not (1 <= suffix <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x)
        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, y)
        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, z)
        if xx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, xx)
        if xy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, xy)
        if xz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, xz)
        if yx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, yx)
        if yy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, yy)
        if yz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, yz)
        if zx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, zx)
        if zy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, zy)
        if zz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, zz)
        if system is None or not (system == -1 or system == 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, system)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x,
                y,
                z,
                xx,
                xy,
                xz,
                yx,
                yy,
                yz,
                zx,
                zy,
                zz,
                system,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.x: typing.Final[types.Real] = x
        self.y: typing.Final[types.Real] = y
        self.z: typing.Final[types.Real] = z
        self.xx: typing.Final[types.Real] = xx
        self.xy: typing.Final[types.Real] = xy
        self.xz: typing.Final[types.Real] = xz
        self.yx: typing.Final[types.Real] = yx
        self.yy: typing.Final[types.Real] = yy
        self.yz: typing.Final[types.Real] = yz
        self.zx: typing.Final[types.Real] = zx
        self.zy: typing.Final[types.Real] = zy
        self.zz: typing.Final[types.Real] = zz
        self.system: typing.Final[types.Integer] = system
