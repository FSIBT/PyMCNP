import re
import typing


from .option_ import Df_1Option_
from ....utils import types
from ....utils import errors


class Iu(Df_1Option_, keyword='iu'):
    """
    Represents INP iu elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'units': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Aiu( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, units: types.IntegerOrJump):
        """
        Initializes ``Iu``.

        Parameters:
            units: Control units.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if units is None or units not in {1, 2}:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, units)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                units,
            ]
        )

        self.units: typing.Final[types.IntegerOrJump] = units
