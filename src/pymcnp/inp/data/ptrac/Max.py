import re
import copy
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

    _KEYWORD = 'max'

    _ATTRS = {
        'events': types.Integer,
    }

    _REGEX = re.compile(rf'\Amax( {types.Integer._REGEX.pattern})\Z')

    def __init__(self, events: types.Integer):
        """
        Initializes ``Max``.

        Parameters:
            events: Maximum number of events to write.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        if events is None or not (events.value != 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, events)

        self.value: typing.Final[types.Tuple] = types.Tuple(
            [
                events,
            ]
        )

        self.events: typing.Final[types.Integer] = events


@dataclasses.dataclass
class MaxBuilder:
    """
    Builds ``Max``.

    Attributes:
        events: Maximum number of events to write.
    """

    events: str | int | types.Integer

    def build(self):
        """
        Builds ``MaxBuilder`` into ``Max``.

        Returns:
            ``Max`` for ``MaxBuilder``.
        """

        events = self.events
        if isinstance(self.events, types.Integer):
            events = self.events
        elif isinstance(self.events, int):
            events = types.Integer(self.events)
        elif isinstance(self.events, str):
            events = types.Integer.from_mcnp(self.events)

        return Max(
            events=events,
        )

    @staticmethod
    def unbuild(ast: Max):
        """
        Unbuilds ``Max`` into ``MaxBuilder``

        Returns:
            ``MaxBuilder`` for ``Max``.
        """

        return Max(
            events=copy.deepcopy(ast.events),
        )
