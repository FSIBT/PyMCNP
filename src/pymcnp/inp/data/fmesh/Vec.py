import re
import typing


from .option_ import FmeshOption_
from ....utils import types
from ....utils import errors


class Vec(FmeshOption_, keyword='vec'):
    """
    Represents INP vec elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'x': types.Real,
        'y': types.Real,
        'z': types.Real,
    }

    _REGEX = re.compile(
        rf'\Avec( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})\Z'
    )

    def __init__(self, x: types.Real, y: types.Real, z: types.Real):
        """
        Initializes ``Vec``.

        Parameters:
            x: Plane vector x component.
            y: Plane vector y component.
            z: Plane vector z component.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if x is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, x)
        if y is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, y)
        if z is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, z)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                x,
                y,
                z,
            ]
        )

        self.x: typing.Final[types.Real] = x
        self.y: typing.Final[types.Real] = y
        self.z: typing.Final[types.Real] = z
