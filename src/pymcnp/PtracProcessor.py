import typing
import pathlib

from . import abc
from . import ptrac
from .Ptrac import Ptrac


class PtracProcessor(abc.Utility):
    """
    Processes ``Ptrac``.
    """

    def prehook(self):
        """
        Runs before processing.
        """

    def posthook(self):
        """
        Runs after processing.
        """

    def process_source(self, event: ptrac.block.Event):
        """
        Processes source events.

        Parameters:
            event: Source event to process.

        Returns:
            Result to yield.
        """

    def process_bank(self, event: ptrac.block.Event):
        """
        Processes bank events.

        Parameters:
            event: Bank event to process.

        Returns:
            Result to yield.
        """

    def process_surface(self, event: ptrac.block.Event):
        """
        Processes surface events.

        Parameters:
            event: Surface event to process.

        Returns:
            Result to yield.
        """

    def process_collision(self, event: ptrac.block.Event):
        """
        Processes collision events.

        Parameters:
            event: Collision event to process.

        Returns:
            Result to yield.
        """

    def process_terminal(self, event: ptrac.block.Event):
        """
        Processes terminal events.

        Parameters:
            event: Terminal event to process.

        Returns:
            Result to yield.
        """

    def run(self, file: Ptrac) -> typing.Generator[typing.Any, None, None]:
        """
        Processes ptrac files.

        Paths are streamed one event at a time in a single pass, so files of any size fit in memory.

        Parameters:
            file: Ptrac file.

        Returns:
            Results of the ``process_*`` methods that are not ``None``, in event order.
        """

        self.prehook()

        for history in file.histories:
            for event in history.events:
                if isinstance(event, ptrac.block.EventSource):
                    result = self.process_source(event)
                elif isinstance(event, ptrac.block.EventSurface):
                    result = self.process_surface(event)
                elif isinstance(event, ptrac.block.EventCollision):
                    result = self.process_collision(event)
                elif isinstance(event, ptrac.block.EventTermination):
                    result = self.process_terminal(event)
                elif isinstance(event, ptrac.block.EventBank):
                    result = self.process_bank(event)
                else:
                    assert False

                if result is not None:
                    yield result

        self.posthook()

    def run_file(self, path: pathlib.Path | str) -> typing.Generator[typing.Any, None, None]:
        """
        Processes ptrac files.

        Paths are streamed one event at a time in a single pass, so files of any size fit in memory.

        Parameters:
            path: Path to ptrac file.

        Returns:
            Results of the ``process_*`` methods that are not ``None``, in event order.
        """

        self.prehook()

        for generator_history in Ptrac.from_file_iter(path):
            for event, _ in generator_history:
                if isinstance(event, ptrac.block.EventSource):
                    result = self.process_source(event)
                elif isinstance(event, ptrac.block.EventSurface):
                    result = self.process_surface(event)
                elif isinstance(event, ptrac.block.EventCollision):
                    result = self.process_collision(event)
                elif isinstance(event, ptrac.block.EventTermination):
                    result = self.process_terminal(event)
                elif isinstance(event, ptrac.block.EventBank):
                    result = self.process_bank(event)
                else:
                    assert False

                if result is not None:
                    yield result

        self.posthook()
