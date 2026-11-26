import typing
import pathlib

from . import abc
from . import ptrac
from .Ptrac import Ptrac, _events


class PtracFilter(abc.Utility):
    """
    Filters PTRAC files.

    Every ``check_*`` method returns ``True`` by default, so the filter keeps every event until you override a check.
    Overriding one method restricts only that type of event, e.g., ``check_collision`` leaves source, bank, surface
    and terminal events in; override the other ``check_*`` methods too, with ``return False``, to drop them.
    """

    def check_source(self, event: ptrac.Event) -> bool:
        """
        Checks source events.

        Parameters:
            event: Source event to check.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        return True

    def check_bank(self, event: ptrac.Event) -> bool:
        """
        Checks bank events.

        Parameters:
            event: Bank event to check.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        return True

    def check_surface(self, event: ptrac.Event) -> bool:
        """
        Checks surface events.

        Parameters:
            event: Surface event to check.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        return True

    def check_collision(self, event: ptrac.Event) -> bool:
        """
        Checks collision events.

        Parameters:
            event: Collision event to check.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        return True

    def check_terminal(self, event: ptrac.Event) -> bool:
        """
        Checks terminal events.

        Parameters:
            event: Terminal event to check.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        return True

    def run(self, file: Ptrac | pathlib.Path | str) -> typing.Iterator[ptrac.Event]:
        """
        Filters ptrac files.

        Paths are streamed one event at a time in a single pass, so files of any size fit in memory.

        Parameters:
            file: Ptrac file or path to ptrac file to filter.

        Yields:
            Accepted events.
        """

        for event in _events(file):
            match event.type:
                case ptrac.EventType.SOURCE:
                    check = self.check_source
                case ptrac.EventType.SURFACE:
                    check = self.check_surface
                case ptrac.EventType.COLLISION:
                    check = self.check_collision
                case ptrac.EventType.TERMINAL:
                    check = self.check_terminal
                case _:
                    check = self.check_bank

            if check(event):
                yield event
