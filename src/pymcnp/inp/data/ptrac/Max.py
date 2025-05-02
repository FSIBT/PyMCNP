import re
import typing
import dataclasses


from ._option import PtracOption
from ....utils import types
from ....utils import errors


class Max(PtracOption):
    """
    Represents INP max elements.

    Attributes:
        events: Maximum number of events to write.
    """

    _ATTRS = {
        'events': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Amax( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, events: types.IntegerOrJump):
        """
        Initializes ``Max``.

        Parameters:
            events: Maximum number of events to write.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if events is None or not (events != 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, events)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                events,
            ]
        )

        self.events: typing.Final[types.IntegerOrJump] = events


@dataclasses.dataclass
class MaxBuilder:
    """
    Builds ``Max``.

    Attributes:
        events: Maximum number of events to write.
    """

    events: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``MaxBuilder`` into ``Max``.

        Returns:
            ``Max`` for ``MaxBuilder``.
        """

        if isinstance(self.events, types.Integer):
            events = self.events
        elif isinstance(self.events, int):
            events = types.IntegerOrJump(self.events)
        elif isinstance(self.events, str):
            events = types.IntegerOrJump.from_mcnp(self.events)

        return Max(
            events=events,
        )
