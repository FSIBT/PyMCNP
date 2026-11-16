import typing
import pathlib

from . import abc
from . import ptrac
from .Ptrac import Ptrac


class PtracFilter(abc.Utility):
    """
    Filters PTRAC files.
    """

    def check_source(self, event: ptrac.block.Event) -> bool:
        """
        Checks source events.

        Parameters:
            event: Source event to check.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        return True

    def check_bank(self, event: ptrac.block.Event) -> bool:
        """
        Checks bank events.

        Parameters:
            event: Bank event to check.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        return True

    def check_surface(self, event: ptrac.block.Event) -> bool:
        """
        Checks surface events.

        Parameters:
            event: Surface event to check.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        return True

    def check_collision(self, event: ptrac.block.Event) -> bool:
        """
        Checks collision events.

        Parameters:
            event: Collision event to check.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        return True

    def check_terminal(self, event: ptrac.block.Event) -> bool:
        """
        Checks terminal events.

        Parameters:
            event: Terminal event to check.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        return True

    def run(self, file: Ptrac) -> typing.Iterator[ptrac.block.Event]:
        """
        Filters ptrac files.

        Paths are streamed one event at a time in a single pass, so files of any size fit in memory.

        Parameters:
            file: Ptrac file or path to ptrac file to filter.

        Yields:
            Accepted events.
        """

        for history in file.histories:
            for event in history.events:
                if isinstance(event, ptrac.block.EventSource):
                    result = self.check_source(event)
                elif isinstance(event, ptrac.block.EventSurface):
                    result = self.check_surface(event)
                elif isinstance(event, ptrac.block.EventCollision):
                    result = self.check_collision(event)
                elif isinstance(event, ptrac.block.EventTermination):
                    result = self.check_terminal(event)
                elif isinstance(event, ptrac.block.EventBank):
                    result = self.check_bank(event)
                else:
                    assert False

                if result:
                    yield event

    def run_file(self, path: pathlib.Path | str) -> typing.Generator[typing.Any, None, None]:
        """
        Filters ptrac files.

        Paths are streamed one event at a time in a single pass, so files of any size fit in memory.

        Parameters:
            path: Path to ptrac file.
        """

        for generator_history in Ptrac.from_file_iter(path):
            for event, _ in generator_history:
                if isinstance(event, ptrac.block.EventSource):
                    result = self.check_source(event)
                elif isinstance(event, ptrac.block.EventSurface):
                    result = self.check_surface(event)
                elif isinstance(event, ptrac.block.EventCollision):
                    result = self.check_collision(event)
                elif isinstance(event, ptrac.block.EventTermination):
                    result = self.check_terminal(event)
                elif isinstance(event, ptrac.block.EventBank):
                    result = self.check_bank(event)
                else:
                    assert False

                if result:
                    yield event
