import re
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Tr_1(DataOption, keyword='tr'):
    """
    Represents INP tr variation #1 elements.

    Attributes:
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
        system: Coordinate system setting.
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
        'yz': types.RealOrJump,
        'system': types.IntegerOrJump,
    }

    _REGEX = re.compile(
        rf'\Atr(\d+)( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})?\Z'
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
        yz: types.RealOrJump,
        system: types.IntegerOrJump = None,
    ):
        """
        Initializes ``Tr_1``.

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
                yz,
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
        self.yz: typing.Final[types.RealOrJump] = yz
        self.system: typing.Final[types.IntegerOrJump] = system


@dataclasses.dataclass
class TrBuilder_1:
    """
    Builds ``Tr_1``.

    Attributes:
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
        system: Coordinate system setting.
    """

    suffix: str | int | types.Integer
    x: str | float | types.RealOrJump
    y: str | float | types.RealOrJump
    z: str | float | types.RealOrJump
    xx: str | float | types.RealOrJump
    xy: str | float | types.RealOrJump
    xz: str | float | types.RealOrJump
    yx: str | float | types.RealOrJump
    yy: str | float | types.RealOrJump
    yz: str | float | types.RealOrJump
    system: str | int | types.IntegerOrJump = None

    def build(self):
        """
        Builds ``TrBuilder_1`` into ``Tr_1``.

        Returns:
            ``Tr_1`` for ``TrBuilder_1``.
        """

        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        if isinstance(self.x, types.Real):
            x = self.x
        elif isinstance(self.x, float) or isinstance(self.x, int):
            x = types.RealOrJump(self.x)
        elif isinstance(self.x, str):
            x = types.RealOrJump.from_mcnp(self.x)

        if isinstance(self.y, types.Real):
            y = self.y
        elif isinstance(self.y, float) or isinstance(self.y, int):
            y = types.RealOrJump(self.y)
        elif isinstance(self.y, str):
            y = types.RealOrJump.from_mcnp(self.y)

        if isinstance(self.z, types.Real):
            z = self.z
        elif isinstance(self.z, float) or isinstance(self.z, int):
            z = types.RealOrJump(self.z)
        elif isinstance(self.z, str):
            z = types.RealOrJump.from_mcnp(self.z)

        if isinstance(self.xx, types.Real):
            xx = self.xx
        elif isinstance(self.xx, float) or isinstance(self.xx, int):
            xx = types.RealOrJump(self.xx)
        elif isinstance(self.xx, str):
            xx = types.RealOrJump.from_mcnp(self.xx)

        if isinstance(self.xy, types.Real):
            xy = self.xy
        elif isinstance(self.xy, float) or isinstance(self.xy, int):
            xy = types.RealOrJump(self.xy)
        elif isinstance(self.xy, str):
            xy = types.RealOrJump.from_mcnp(self.xy)

        if isinstance(self.xz, types.Real):
            xz = self.xz
        elif isinstance(self.xz, float) or isinstance(self.xz, int):
            xz = types.RealOrJump(self.xz)
        elif isinstance(self.xz, str):
            xz = types.RealOrJump.from_mcnp(self.xz)

        if isinstance(self.yx, types.Real):
            yx = self.yx
        elif isinstance(self.yx, float) or isinstance(self.yx, int):
            yx = types.RealOrJump(self.yx)
        elif isinstance(self.yx, str):
            yx = types.RealOrJump.from_mcnp(self.yx)

        if isinstance(self.yy, types.Real):
            yy = self.yy
        elif isinstance(self.yy, float) or isinstance(self.yy, int):
            yy = types.RealOrJump(self.yy)
        elif isinstance(self.yy, str):
            yy = types.RealOrJump.from_mcnp(self.yy)

        if isinstance(self.yz, types.Real):
            yz = self.yz
        elif isinstance(self.yz, float) or isinstance(self.yz, int):
            yz = types.RealOrJump(self.yz)
        elif isinstance(self.yz, str):
            yz = types.RealOrJump.from_mcnp(self.yz)

        system = None
        if isinstance(self.system, types.Integer):
            system = self.system
        elif isinstance(self.system, int):
            system = types.IntegerOrJump(self.system)
        elif isinstance(self.system, str):
            system = types.IntegerOrJump.from_mcnp(self.system)

        return Tr_1(
            suffix=suffix,
            x=x,
            y=y,
            z=z,
            xx=xx,
            xy=xy,
            xz=xz,
            yx=yx,
            yy=yy,
            yz=yz,
            system=system,
        )
