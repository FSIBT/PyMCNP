import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Wwt(DataOption_, keyword='wwt'):
    """
    Represents INP wwt elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'designator': types.Designator,
        'bounds': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Awwt:(\S+)((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, designator: types.Designator, bounds: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Wwt``.

        Parameters:
            designator: Data card particle designator.
            bounds: Upper time bound.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if designator is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, designator)
        if bounds is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bounds)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                bounds,
            ]
        )

        self.designator: typing.Final[types.Designator] = designator
        self.bounds: typing.Final[types.Tuple[types.RealOrJump]] = bounds
