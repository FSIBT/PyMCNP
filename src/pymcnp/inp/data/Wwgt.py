import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Wwgt(DataOption_, keyword='wwgt'):
    """
    Represents INP wwgt elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'bounds': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'\Awwgt((?: {types.Real._REGEX.pattern})+?)\Z')

    def __init__(self, bounds: types.Tuple[types.Real]):
        """
        Initializes ``Wwgt``.

        Parameters:
            bounds: Upper time bound for weight-window group to be generated.

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

        self.bounds: typing.Final[types.Tuple[types.Real]] = bounds
