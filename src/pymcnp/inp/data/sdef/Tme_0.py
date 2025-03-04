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
        'time': types.Real,
    }

    _REGEX = re.compile(r'tme( \S+)')

    def __init__(self, time: types.Real):
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

        self.time: typing.Final[types.Real] = time
