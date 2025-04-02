import re
import typing


from .option_ import SdefOption_
from ....utils import types
from ....utils import errors


class Tme_1(SdefOption_, keyword='tme'):
    """
    Represents INP tme_1 elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'time': types.EmbeddedDistributionNumber,
    }

    _REGEX = re.compile(rf'\Atme( {types.EmbeddedDistributionNumber._REGEX.pattern})\Z')

    def __init__(self, time: types.EmbeddedDistributionNumber):
        """
        Initializes ``Tme_1``.

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

        self.time: typing.Final[types.EmbeddedDistributionNumber] = time
