import re
import typing


from .option_ import FmeshOption_
from ....utils import types
from ....utils import errors


class Eints(FmeshOption_, keyword='eints'):
    """
    Represents INP eints elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'count': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Aeints( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, count: types.IntegerOrJump):
        """
        Initializes ``Eints``.

        Parameters:
            count: Number of mesh points for each mesh energy.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if count is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, count)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                count,
            ]
        )

        self.count: typing.Final[types.IntegerOrJump] = count
