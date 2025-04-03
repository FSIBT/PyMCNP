import re
import typing


from .option_ import SdefOption_
from ....utils import types
from ....utils import errors


class Bap(SdefOption_, keyword='bap'):
    """
    Represents INP bap elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'ba1': types.RealOrJump,
        'ba2': types.RealOrJump,
        'u': types.RealOrJump,
    }

    _REGEX = re.compile(
        rf'\Abap( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})\Z'
    )

    def __init__(self, ba1: types.RealOrJump, ba2: types.RealOrJump, u: types.RealOrJump):
        """
        Initializes ``Bap``.

        Parameters:
            ba1: Beam aperture half-width in the x transverse direction.
            ba2: Beam aperture half-width in the y transverse direction.
            u: Unused, arrbirary value.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if ba1 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ba1)
        if ba2 is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, ba2)
        if u is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, u)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                ba1,
                ba2,
                u,
            ]
        )

        self.ba1: typing.Final[types.RealOrJump] = ba1
        self.ba2: typing.Final[types.RealOrJump] = ba2
        self.u: typing.Final[types.RealOrJump] = u
