import re
import copy
import typing
import dataclasses


from . import _option
from ...utils import types
from ...utils import errors


class Tr_2(_option.DataOption):
    """
    Represents INP tr variation #2 elements.

    Attributes:
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
        'yx': types.Real,
        'yy': types.Real,
        'system': types.Integer,
    }

    _REGEX = re.compile(
        rf'\A([*])?tr(\d+)( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Real._REGEX.pattern[2:-2]})( {types.Integer._REGEX.pattern[2:-2]})?\Z'
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
        prefix: types.String = None,
        system: types.Integer = None,
    ):
        """
        Initializes ``Tr_2``.

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
            system: Coordinate system setting.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if prefix is not None and prefix.value not in {'*'}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, prefix)
        if suffix is None or not (1 <= suffix.value <= 999):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, suffix)
        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, x)
        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, y)
        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, z)
        if xx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, xx)
        if xy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, xy)
        if xz is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, xz)
        if yx is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, yx)
        if yy is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, yy)
        if system is not None and not (system.value == -1 or system.value == 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, system)

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

        self.prefix: typing.Final[types.String] = prefix
        self.suffix: typing.Final[types.Integer] = suffix
        self.x: typing.Final[types.Real] = x
        self.y: typing.Final[types.Real] = y
        self.z: typing.Final[types.Real] = z
        self.xx: typing.Final[types.Real] = xx
        self.xy: typing.Final[types.Real] = xy
        self.xz: typing.Final[types.Real] = xz
        self.yx: typing.Final[types.Real] = yx
        self.yy: typing.Final[types.Real] = yy
        self.system: typing.Final[types.Integer] = system


@dataclasses.dataclass
class TrBuilder_2(_option.DataOptionBuilder):
    """
    Builds ``Tr_2``.

    Attributes:
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
        system: Coordinate system setting.
    """

    suffix: str | int | types.Integer
    x: str | float | types.Real
    y: str | float | types.Real
    z: str | float | types.Real
    xx: str | float | types.Real
    xy: str | float | types.Real
    xz: str | float | types.Real
    yx: str | float | types.Real
    yy: str | float | types.Real
    prefix: str | types.String = None
    system: str | int | types.Integer = None

    def build(self):
        """
        Builds ``TrBuilder_2`` into ``Tr_2``.

        Returns:
            ``Tr_2`` for ``TrBuilder_2``.
        """

        prefix = self.prefix
        if isinstance(self.prefix, types.String):
            prefix = self.prefix
        elif isinstance(self.prefix, str):
            prefix = types.String.from_mcnp(self.prefix)

        suffix = self.suffix
        if isinstance(self.suffix, types.Integer):
            suffix = self.suffix
        elif isinstance(self.suffix, int):
            suffix = types.Integer(self.suffix)
        elif isinstance(self.suffix, str):
            suffix = types.Integer.from_mcnp(self.suffix)

        x = self.x
        if isinstance(self.x, types.Real):
            x = self.x
        elif isinstance(self.x, float) or isinstance(self.x, int):
            x = types.Real(self.x)
        elif isinstance(self.x, str):
            x = types.Real.from_mcnp(self.x)

        y = self.y
        if isinstance(self.y, types.Real):
            y = self.y
        elif isinstance(self.y, float) or isinstance(self.y, int):
            y = types.Real(self.y)
        elif isinstance(self.y, str):
            y = types.Real.from_mcnp(self.y)

        z = self.z
        if isinstance(self.z, types.Real):
            z = self.z
        elif isinstance(self.z, float) or isinstance(self.z, int):
            z = types.Real(self.z)
        elif isinstance(self.z, str):
            z = types.Real.from_mcnp(self.z)

        xx = self.xx
        if isinstance(self.xx, types.Real):
            xx = self.xx
        elif isinstance(self.xx, float) or isinstance(self.xx, int):
            xx = types.Real(self.xx)
        elif isinstance(self.xx, str):
            xx = types.Real.from_mcnp(self.xx)

        xy = self.xy
        if isinstance(self.xy, types.Real):
            xy = self.xy
        elif isinstance(self.xy, float) or isinstance(self.xy, int):
            xy = types.Real(self.xy)
        elif isinstance(self.xy, str):
            xy = types.Real.from_mcnp(self.xy)

        xz = self.xz
        if isinstance(self.xz, types.Real):
            xz = self.xz
        elif isinstance(self.xz, float) or isinstance(self.xz, int):
            xz = types.Real(self.xz)
        elif isinstance(self.xz, str):
            xz = types.Real.from_mcnp(self.xz)

        yx = self.yx
        if isinstance(self.yx, types.Real):
            yx = self.yx
        elif isinstance(self.yx, float) or isinstance(self.yx, int):
            yx = types.Real(self.yx)
        elif isinstance(self.yx, str):
            yx = types.Real.from_mcnp(self.yx)

        yy = self.yy
        if isinstance(self.yy, types.Real):
            yy = self.yy
        elif isinstance(self.yy, float) or isinstance(self.yy, int):
            yy = types.Real(self.yy)
        elif isinstance(self.yy, str):
            yy = types.Real.from_mcnp(self.yy)

        system = self.system
        if isinstance(self.system, types.Integer):
            system = self.system
        elif isinstance(self.system, int):
            system = types.Integer(self.system)
        elif isinstance(self.system, str):
            system = types.Integer.from_mcnp(self.system)

        return Tr_2(
            prefix=prefix,
            suffix=suffix,
            x=x,
            y=y,
            z=z,
            xx=xx,
            xy=xy,
            xz=xz,
            yx=yx,
            yy=yy,
            system=system,
        )

    @staticmethod
    def unbuild(ast: Tr_2):
        """
        Unbuilds ``Tr_2`` into ``TrBuilder_2``

        Returns:
            ``TrBuilder_2`` for ``Tr_2``.
        """

        return TrBuilder_2(
            prefix=copy.deepcopy(ast.prefix),
            suffix=copy.deepcopy(ast.suffix),
            x=copy.deepcopy(ast.x),
            y=copy.deepcopy(ast.y),
            z=copy.deepcopy(ast.z),
            xx=copy.deepcopy(ast.xx),
            xy=copy.deepcopy(ast.xy),
            xz=copy.deepcopy(ast.xz),
            yx=copy.deepcopy(ast.yx),
            yy=copy.deepcopy(ast.yy),
            system=copy.deepcopy(ast.system),
        )
