import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Wwge(DataOption_, keyword='wwge'):
    """
    Represents INP wwge elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'bounds': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Awwge((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, bounds: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Wwge``.

        Parameters:
            bounds: Upper energy bound for weight-window group to be generated.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if bounds is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bounds)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                bounds,
            ]
        )

        self.bounds: typing.Final[types.Tuple[types.RealOrJump]] = bounds
