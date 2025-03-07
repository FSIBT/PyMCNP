import re
import typing


from .option_ import PtracOption_
from ....utils import types
from ....utils import errors


class Max(PtracOption_, keyword='max'):
    """
    Represents INP max elements.

    Attributes:
        InpError: SEMANTICS_OPTION_VALUE.
    """

    _ATTRS = {
        'events': types.Integer,
    }

    _REGEX = re.compile(rf'max( {types.Integer._REGEX.pattern})')

    def __init__(self, events: types.Integer):
        """
        Initializes ``Max``.

        Parameters:
            events: Maximum number of events to write.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if events is None or not (events != 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, events)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                events,
            ]
        )

        self.events: typing.Final[types.Integer] = events
