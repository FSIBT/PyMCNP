import re
import copy
import typing
import dataclasses


from ._option import DataOption
from ...utils import types
from ...utils import errors


class Tr_3(DataOption):
    """
    Represents INP tr variation #3 elements.

    Attributes:
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
        rf'\Atr(\d+)( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Integer._REGEX.pattern})?\Z'
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
        system: types.Integer = None,
    ):
        """
        Initializes ``Tr_3``.

        Parameters:
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
        self.system: typing.Final[types.Integer] = system


@dataclasses.dataclass
class TrBuilder_3:
    """
    Builds ``Tr_3``.

    Attributes:
        suffix: Data card option suffix.
        x: Displacement vector x component.
        y: Displacement vector y component.
        z: Displacement vector z component.
        xx: Rotation matrix xx' component.
        xy: Rotation matrix xy' component.
        xz: Rotation matrix xz' component.
        system: Coordinate system setting.
    """

    suffix: str | int | types.Integer
    x: str | float | types.Real
    y: str | float | types.Real
    z: str | float | types.Real
    xx: str | float | types.Real
    xy: str | float | types.Real
    xz: str | float | types.Real
    system: str | int | types.Integer = None

    def build(self):
        """
        Builds ``TrBuilder_3`` into ``Tr_3``.

        Returns:
            ``Tr_3`` for ``TrBuilder_3``.
        """

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

        system = self.system
        if isinstance(self.system, types.Integer):
            system = self.system
        elif isinstance(self.system, int):
            system = types.Integer(self.system)
        elif isinstance(self.system, str):
            system = types.Integer.from_mcnp(self.system)

        return Tr_3(
            suffix=suffix,
            x=x,
            y=y,
            z=z,
            xx=xx,
            xy=xy,
            xz=xz,
            system=system,
        )

    @staticmethod
    def unbuild(ast: Tr_3):
        """
        Unbuilds ``Tr_3`` into ``TrBuilder_3``

        Returns:
            ``TrBuilder_3`` for ``Tr_3``.
        """

        return Tr_3(
            suffix=copy.deepcopy(ast.suffix),
            x=copy.deepcopy(ast.x),
            y=copy.deepcopy(ast.y),
            z=copy.deepcopy(ast.z),
            xx=copy.deepcopy(ast.xx),
            xy=copy.deepcopy(ast.xy),
            xz=copy.deepcopy(ast.xz),
            system=copy.deepcopy(ast.system),
        )
