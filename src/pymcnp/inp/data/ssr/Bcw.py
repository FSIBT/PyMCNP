import re
import typing


from .option_ import SsrOption_
from ....utils import types
from ....utils import errors


class Bcw(SsrOption_, keyword='bcw'):
    """
    Represents INP bcw elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'radius': types.RealOrJump,
        'zb': types.RealOrJump,
        'ze': types.RealOrJump,
    }

    _REGEX = re.compile(
        rf'\Abcw( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})\Z'
    )

    def __init__(self, radius: types.RealOrJump, zb: types.RealOrJump, ze: types.RealOrJump):
        """
        Initializes ``Bcw``.

        Parameters:
            radius: Radius of cylindrical window.
            zb: Bottom of cylindrical window.
            ze: Top of cylindrical window.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if radius is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, radius)
        if zb is None or not (0 < zb):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, zb)
        if ze is None or not (0 < zb < ze):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ze)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                radius,
                zb,
                ze,
            ]
        )

        self.radius: typing.Final[types.RealOrJump] = radius
        self.zb: typing.Final[types.RealOrJump] = zb
        self.ze: typing.Final[types.RealOrJump] = ze
