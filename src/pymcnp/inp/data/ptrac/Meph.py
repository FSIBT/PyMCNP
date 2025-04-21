import re
import typing
import dataclasses


from ._option import PtracOption
from ....utils import types
from ....utils import errors


class Meph(PtracOption, keyword='meph'):
    """
    Represents INP meph elements.

    Attributes:
        events: Maximum number of events per history to write.
    """

    _ATTRS = {
        'events': types.IntegerOrJump,
    }

    _REGEX = re.compile(rf'\Ameph( {types.IntegerOrJump._REGEX.pattern})\Z')

    def __init__(self, events: types.IntegerOrJump):
        """
        Initializes ``Meph``.

        Parameters:
            events: Maximum number of events per history to write.

        Raises:
            InpError: SEMANTICS_OPTION_VALUE.
        """

        if events is None or not (events > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION_VALUE, events)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                events,
            ]
        )

        self.events: typing.Final[types.IntegerOrJump] = events


@dataclasses.dataclass
class MephBuilder:
    """
    Builds ``Meph``.

    Attributes:
        events: Maximum number of events per history to write.
    """

    events: str | int | types.IntegerOrJump

    def build(self):
        """
        Builds ``MephBuilder`` into ``Meph``.

        Returns:
            ``Meph`` for ``MephBuilder``.
        """

        if isinstance(self.events, types.Integer):
            events = self.events
        elif isinstance(self.events, int):
            events = types.IntegerOrJump(self.events)
        elif isinstance(self.events, str):
            events = types.IntegerOrJump.from_mcnp(self.events)

        return Meph(
            events=events,
        )
