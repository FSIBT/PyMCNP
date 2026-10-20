import pathlib

from . import abc
from . import ptrac
from .Ptrac import Ptrac
from .Ptrac import _events


class PtracProcessor(abc.Utility):
    """
    Processes `Ptrac`.
    """

    def prehook(self):
        """
        Runs before processing.
        """

    def posthook(self):
        """
        Runs after processing.
        """

    def process_source(self, event: ptrac.Event):
        """
        Processes source events.

        Parameters:
            event: Source event to process.
        """

    def process_bank(self, event: ptrac.Event):
        """
        Processes bank events.

        Parameters:
            event: Bank event to process.
        """

    def process_surface(self, event: ptrac.Event):
        """
        Processes surface events.

        Parameters:
            event: Surface event to process.
        """

    def process_collision(self, event: ptrac.Event):
        """
        Processes collision events.

        Parameters:
            event: Collision event to process.
        """

    def process_terminal(self, event: ptrac.Event):
        """
        Processes terminal events.

        Parameters:
            event: Terminal event to process.
        """

    def run(self, file: Ptrac | pathlib.Path | str):
        """
        Processes ptrac files.

        Paths are streamed one event at a time in a single pass, so files of any size fit in memory.

        Parameters:
            file: Ptrac file or path to ptrac file to process.
        """

        self.prehook()

        for event in _events(file):
            match event.type:
                case ptrac.EventType.SOURCE:
                    self.process_source(event)
                case ptrac.EventType.SURFACE:
                    self.process_surface(event)
                case ptrac.EventType.COLLISION:
                    self.process_collision(event)
                case ptrac.EventType.TERMINAL:
                    self.process_terminal(event)
                case _:
                    self.process_bank(event)

        self.posthook()
