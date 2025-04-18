import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Area(DataOption_, keyword='area'):
    """
    Represents INP area elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'areas': types.Tuple[types.RealOrJump],
    }

    _REGEX = re.compile(rf'\Aarea((?: {types.RealOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, areas: types.Tuple[types.RealOrJump]):
        """
        Initializes ``Area``.

        Parameters:
            areas: Tuple of surface areas.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if areas is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, areas)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                areas,
            ]
        )

        self.areas: typing.Final[types.Tuple[types.RealOrJump]] = areas
