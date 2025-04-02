import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Tr_3(DataOption_, keyword='tr'):
    """
    Represents INP tr_3 elements.

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
