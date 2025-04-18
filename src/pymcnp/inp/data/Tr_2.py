import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Tr_2(DataOption_, keyword='tr'):
    """
    Represents INP tr_2 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'x': types.RealOrJump,
        'y': types.RealOrJump,
        'z': types.RealOrJump,
        'xx': types.RealOrJump,
        'xy': types.RealOrJump,
        'xz': types.RealOrJump,
        'yx': types.RealOrJump,
        'yy': types.RealOrJump,
        'system': types.IntegerOrJump,
    }

    _REGEX = re.compile(
        rf'\Atr(\d+)( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})?\Z'
    )

    def __init__(
        self,
        suffix: types.Integer,
        x: types.RealOrJump,
        y: types.RealOrJump,
        z: types.RealOrJump,
        xx: types.RealOrJump,
        xy: types.RealOrJump,
        xz: types.RealOrJump,
        yx: types.RealOrJump,
        yy: types.RealOrJump,
        system: types.IntegerOrJump = None,
    ):
        """
        Initializes ``Tr_2``.

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
        if system is not None and not (system == -1 or system == 1):
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
                system,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.x: typing.Final[types.RealOrJump] = x
        self.y: typing.Final[types.RealOrJump] = y
        self.z: typing.Final[types.RealOrJump] = z
        self.xx: typing.Final[types.RealOrJump] = xx
        self.xy: typing.Final[types.RealOrJump] = xy
        self.xz: typing.Final[types.RealOrJump] = xz
        self.yx: typing.Final[types.RealOrJump] = yx
        self.yy: typing.Final[types.RealOrJump] = yy
        self.system: typing.Final[types.IntegerOrJump] = system
