import re
import typing


from .option_ import SdefOption_
from ....utils import types
from ....utils import errors


class Tme_0(SdefOption_, keyword='tme'):
    """
    Represents INP tme_0 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'time': types.RealOrJump,
    }

    _REGEX = re.compile(rf'\Atme( {types.RealOrJump._REGEX.pattern})\Z')

    def __init__(self, time: types.RealOrJump):
        """
        Initializes ``Tme_0``.

        Parameters:
            time: Time in shakes.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if time is None:
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, time)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                time,
            ]
        )

        self.time: typing.Final[types.RealOrJump] = time
