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
        'ba1': types.Real,
        'ba2': types.Real,
        'u': types.Real,
    }

    _REGEX = re.compile(
        rf'bap( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})( {types.Real._REGEX.pattern})'
    )

    def __init__(self, ba1: types.Real, ba2: types.Real, u: types.Real):
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

        self.ba1: typing.Final[types.Real] = ba1
        self.ba2: typing.Final[types.Real] = ba2
        self.u: typing.Final[types.Real] = u
