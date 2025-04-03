import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Tr_4(DataOption_, keyword='tr'):
    """
    Represents INP tr_4 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'x': types.RealOrJump,
        'y': types.RealOrJump,
        'z': types.RealOrJump,
        'system': types.IntegerOrJump,
    }

    _REGEX = re.compile(
        rf'\Atr(\d+)( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})?\Z'
    )

    def __init__(
        self,
        suffix: types.Integer,
        x: types.RealOrJump,
        y: types.RealOrJump,
        z: types.RealOrJump,
        system: types.IntegerOrJump = None,
    ):
        """
        Initializes ``Tr_4``.

        Parameters:
            suffix: Data card option suffix.
            x: Displacement vector x component.
            y: Displacement vector y component.
            z: Displacement vector z component.
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
        if system is not None and not (system == -1 or system == 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, system)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x,
                y,
                z,
                system,
            ]
        )

        self.suffix: typing.Final[types.IntegerOrJump] = suffix
        self.x: typing.Final[types.RealOrJump] = x
        self.y: typing.Final[types.RealOrJump] = y
        self.z: typing.Final[types.RealOrJump] = z
        self.system: typing.Final[types.IntegerOrJump] = system
