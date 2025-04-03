import re
import typing


from .option_ import FmeshOption_
from ....utils import types
from ....utils import errors


class Inc(FmeshOption_, keyword='inc'):
    """
    Represents INP inc elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'lower': types.RealOrJump,
        'upper': types.RealOrJump,
    }

    _REGEX = re.compile(
        rf'\Ainc( {types.RealOrJump._REGEX.pattern})( {types.RealOrJump._REGEX.pattern})?\Z'
    )

    def __init__(self, lower: types.RealOrJump, upper: types.RealOrJump = None):
        """
        Initializes ``Inc``.

        Parameters:
            lower: Collision for FMESH tally lower bound.
            upper: Collision for FMESH tally upper bound.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if lower is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, lower)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                lower,
                upper,
            ]
        )

        self.lower: typing.Final[types.RealOrJump] = lower
        self.upper: typing.Final[types.RealOrJump] = upper
