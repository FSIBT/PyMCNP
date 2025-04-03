import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Hsrc(DataOption_, keyword='hsrc'):
    """
    Represents INP hsrc elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'x_number': types.IntegerOrJump,
        'x_minimum': types.RealOrJump,
        'x_maximum': types.RealOrJump,
        'y_number': types.IntegerOrJump,
        'y_minimum': types.RealOrJump,
        'y_maximum': types.RealOrJump,
        'z_number': types.IntegerOrJump,
        'z_minimum': types.RealOrJump,
        'z_maximum': types.RealOrJump,
    }

    _REGEX = re.compile(
        rf'\Ahsrc( {types.IntegerOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.IntegerOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})\Z'
    )

    def __init__(
        self,
        x_number: types.IntegerOrJump,
        x_minimum: types.RealOrJump,
        x_maximum: types.RealOrJump,
        y_number: types.IntegerOrJump,
        y_minimum: types.RealOrJump,
        y_maximum: types.RealOrJump,
        z_number: types.IntegerOrJump,
        z_minimum: types.RealOrJump,
        z_maximum: types.RealOrJump,
    ):
        """
        Initializes ``Hsrc``.

        Parameters:
            x_number: Number of mesh intervals in x direction.
            x_minimum: Minimum x-value for mesh.
            x_maximum: Maximum x-value for mesh.
            y_number: Number of mesh intervals in y direction.
            y_minimum: Minimum y-value for mesh.
            y_maximum: Maximum y-value for mesh.
            z_number: Number of mesh intervals in z direction.
            z_minimum: Minimum z-value for mesh.
            z_maximum: Maximum z-value for mesh.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if x_number is None or not (x_number > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x_number)
        if x_minimum is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x_minimum)
        if x_maximum is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x_maximum)
        if y_number is None or not (y_number > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, y_number)
        if y_minimum is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, y_minimum)
        if y_maximum is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, y_maximum)
        if z_number is None or not (z_number > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, z_number)
        if z_minimum is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, z_minimum)
        if z_maximum is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, z_maximum)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x_number,
                x_minimum,
                x_maximum,
                y_number,
                y_minimum,
                y_maximum,
                z_number,
                z_minimum,
                z_maximum,
            ]
        )

        self.x_number: typing.Final[types.IntegerOrJump] = x_number
        self.x_minimum: typing.Final[types.RealOrJump] = x_minimum
        self.x_maximum: typing.Final[types.RealOrJump] = x_maximum
        self.y_number: typing.Final[types.IntegerOrJump] = y_number
        self.y_minimum: typing.Final[types.RealOrJump] = y_minimum
        self.y_maximum: typing.Final[types.RealOrJump] = y_maximum
        self.z_number: typing.Final[types.IntegerOrJump] = z_number
        self.z_minimum: typing.Final[types.RealOrJump] = z_minimum
        self.z_maximum: typing.Final[types.RealOrJump] = z_maximum
