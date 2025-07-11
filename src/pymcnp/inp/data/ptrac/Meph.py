import re

from . import _option
from ....utils import types
from ....utils import errors


class Meph(_option.PtracOption):
    """
    Represents INP meph elements.

    Attributes:
        events: Maximum number of events per history to write.
    """

    _KEYWORD = 'meph'

    _ATTRS = {
        'events': types.Integer,
    }

    _REGEX = re.compile(rf'\Ameph( {types.Integer._REGEX.pattern[2:-2]})\Z')

    def __init__(self, events: str | int | types.Integer):
        """
        Initializes ``Meph``.

        Parameters:
            events: Maximum number of events per history to write.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.events: types.Integer = events

    @property
    def events(self) -> types.Integer:
        """
        Gets ``events``.

        Returns:
            ``events``.
        """

        return self._events

    @events.setter
    def events(self, events: str | int | types.Integer) -> None:
        """
        Sets ``events``.

        Parameters:
            events: Maximum number of events per history to write.

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        if events is not None:
            if isinstance(events, types.Integer):
                events = events
            elif isinstance(events, int):
                events = types.Integer(events)
            elif isinstance(events, str):
                events = types.Integer.from_mcnp(events)
            else:
                raise TypeError

        if events is None or not (events > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, events)

        self._events: types.Integer = events
