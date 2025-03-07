import re
import typing


from .option_ import CellOption_
from ...utils import types
from ...utils import errors


class Vol(CellOption_, keyword='vol'):
    """
    Represents INP vol elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'volume': types.Real,
    }

    _REGEX = re.compile(rf'vol( {types.Real._REGEX.pattern})')

    def __init__(self, volume: types.Real):
        """
        Initializes ``Vol``.

        Parameters:
            volume: Cell volume.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if volume is None or not (volume >= 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, volume)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                volume,
            ]
        )

        self.volume: typing.Final[types.Real] = volume
