import re
import typing


from .option_ import DataOption_
from ...utils import types
from ...utils import errors


class Lat(DataOption_, keyword='lat'):
    """
    Represents INP lat elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'type': types.Tuple[types.IntegerOrJump],
    }

    _REGEX = re.compile(rf'\Alat((?: {types.IntegerOrJump._REGEX.pattern})+?)\Z')

    def __init__(self, type: types.Tuple[types.IntegerOrJump]):
        """
        Initializes ``Lat``.

        Parameters:
            type: Tuple of lattice types.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if type is None or not (filter(lambda entry: not (entry == 1 or entry == 2), type)):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, type)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                type,
            ]
        )

        self.type: typing.Final[types.Tuple[types.IntegerOrJump]] = type
