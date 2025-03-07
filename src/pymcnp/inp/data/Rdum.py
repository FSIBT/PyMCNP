import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Rdum(DataOption_, keyword='rdum'):
    """
    Represents INP rdum elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'floats': types.Tuple[types.Real],
    }

    _REGEX = re.compile(rf'rdum(( {types.Real._REGEX.pattern})+)')

    def __init__(self, floats: types.Tuple[types.Real]):
        """
        Initializes ``Rdum``.

        Parameters:
            floats: Floating point array.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if floats is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, floats)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                floats,
            ]
        )

        self.floats: typing.Final[types.Tuple[types.Real]] = floats
