import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Embeb(DataOption_, keyword='embeb'):
    """
    Represents INP embeb elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'suffix': types.Integer,
        'bounds': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Aembeb(\d+)((?: {types.Real._REGEX.pattern})+?)\Z')

    def __init__(self, suffix: types.Integer, bounds: types.Tuple[types.Real]):
        """
        Initializes ``Embeb``.

        Parameters:
            suffix: Data card option suffix.
            bounds: Tuple of upper energy bounds.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if suffix is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, suffix)
        if bounds is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, bounds)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                bounds,
            ]
        )

        self.suffix: typing.Final[types.Integer] = suffix
        self.bounds: typing.Final[types.Tuple[types.Real]] = bounds
