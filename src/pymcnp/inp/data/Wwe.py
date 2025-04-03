import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Wwe(DataOption_, keyword='wwe'):
    """
    Represents INP wwe elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'designator': types.Designator,
        'bounds': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Awwe:(\S+)((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, designator: types.Designator, bounds: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Wwe``.

        Parameters:
            designator: Data card particle designator.
            bounds: Upper energy/time bound.

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
