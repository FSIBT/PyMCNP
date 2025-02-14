import re
import typing

from . import _option
from ...utils import types
from ...utils import errors
from ...utils import _parser


class DataOption_Tr(_option.DataOption_, keyword='tr'):
    """
    Represents INP data card tr options.

    Attributes:
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
        suffix: Data card option suffix.
    """

    _REGEX = re.compile(
        r'\Atr(\d+?)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)( \S+)\Z'
    )

    def __init__(
        self,
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
        suffix: types.Integer,
    ):
        """
        Initializes ``DataOption_Tr``.

        Parameters:
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
            suffix: Data card option suffix.

        Returns:
            ``DataOption_Tr``.

        Raises:
            McnpError: SEMANTICS_DATA_OPTION_ENTRY_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_ENTRY_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_ENTRY_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_ENTRY_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_ENTRY_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_ENTRY_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_ENTRY_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_ENTRY_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_ENTRY_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_ENTRY_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_ENTRY_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_ENTRY_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_VALUE.
            McnpError: SEMANTICS_DATA_OPTION_SUFFIX.
        """

        if x is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_ENTRY_VALUE, x)
        if y is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_ENTRY_VALUE, y)
        if z is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_ENTRY_VALUE, z)
        if xx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_ENTRY_VALUE, xx)
        if xy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_ENTRY_VALUE, xy)
        if xz is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_ENTRY_VALUE, xz)
        if yx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_ENTRY_VALUE, yx)
        if yy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_ENTRY_VALUE, yy)
        if yz is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_ENTRY_VALUE, yz)
        if zx is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_ENTRY_VALUE, zx)
        if zy is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_ENTRY_VALUE, zy)
        if zz is None:
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_ENTRY_VALUE, zz)
        if system is None or not (system == -1 or system == 1):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_VALUE, system)
        if suffix is None or not (1 <= suffix <= 999):
            raise errors.McnpError(errors.McnpCode.SEMANTICS_DATA_OPTION_SUFFIX, suffix)

        self.value: typing.Final[tuple[any]] = types._Tuple(
            [x, y, z, xx, xy, xz, yx, yy, yz, zx, zy, zz, system]
        )
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
        self.suffix: typing.Final[types.Integer] = suffix

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``DataOption_Tr`` from INP.

        Parameters:
            source: INP data card option.

        Returns:
            ``DataOption_Tr``.

        Raises:
            McnpError: SYNTAX_DATA_OPTION.
        """

        source, comments = _parser.preprocess_inp(source)
        tokens = DataOption_Tr._REGEX.match(source)

        if not tokens:
            raise errors.McnpError(errors.McnpCode.SYNTAX_DATA_OPTION, source)

        suffix = types.Integer.from_mcnp(tokens[1])
        x = types.Real.from_mcnp(tokens[2])
        y = types.Real.from_mcnp(tokens[3])
        z = types.Real.from_mcnp(tokens[4])
        xx = types.Real.from_mcnp(tokens[5])
        xy = types.Real.from_mcnp(tokens[6])
        xz = types.Real.from_mcnp(tokens[7])
        yx = types.Real.from_mcnp(tokens[8])
        yy = types.Real.from_mcnp(tokens[9])
        yz = types.Real.from_mcnp(tokens[10])
        zx = types.Real.from_mcnp(tokens[11])
        zy = types.Real.from_mcnp(tokens[12])
        zz = types.Real.from_mcnp(tokens[13])
        system = types.Integer.from_mcnp(tokens[14])

        return DataOption_Tr(x, y, z, xx, xy, xz, yx, yy, yz, zx, zy, zz, system, suffix)
