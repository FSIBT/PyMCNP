import re

from . import _option
from ... import types
from ... import errors


class Meph(_option.PtracOption):
    """
    Represents INP `meph` elements.
    """

    _KEYWORD = 'meph'

    _ATTRS = {
        'events': types.Integer,
    }

    _REGEX = re.compile(rf'\Ameph( {types.Integer._REGEX.pattern[2:-2]})\Z', re.IGNORECASE)

    def __init__(self, events: str | int | types.Integer):
        """
        Initializes `Meph`.

        Parameters:
            events: Maximum number of events per history to write.

        Raises:
            InpError: SEMANTICS_OPTION.
        """

        self.events: types.Integer = events

    @property
    def events(self) -> types.Integer:
        """
        Maximum number of events per history to write

        Raises:
            InpError: SEMANTICS_OPTION.
            TypeError:
        """

        return self._events

    @events.setter
    def events(self, events: str | int | types.Integer) -> None:
        """
        Sets `events`.

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

        if events is None or not (events > 0):
            raise errors.InpError(errors.InpCode.SEMANTICS_OPTION, events)

        self._events: types.Integer = events
