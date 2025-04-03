import re
import typing


from .option_ import ActOption_
from ....utils import types
from ....utils import errors


class Thresh(ActOption_, keyword='thresh'):
    """
    Represents INP thresh elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'fraction': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Athresh( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, fraction: types.RealOrJump):
        """
        Initializes ``Thresh``.

        Parameters:
            fraction: Fraction of highest-amplitude discrete delayed-gamma lines retained.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if fraction is None or not (0 <= fraction <= 1):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, fraction)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                fraction,
            ]
        )

        self.fraction: typing.Final[types.RealOrJump] = fraction
