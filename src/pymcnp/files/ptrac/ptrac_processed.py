"""
Contains the ``ProcessedPtrac`` class for processing PTRAC.
"""

from .event import Event, EventType
from .ptrac import Ptrac


class ProcessedPtrac:
    """
    Processes PTRAC.

    ``ProcessedPtrac`` provides helper methods and stubs for processing PTRAC.
    Subclasses override its methods to specify how ``run`` processes PTRAC.

    Attributes:
        ptrac: ``Ptrac`` to process.
    """

    def __init__(self, ptrac: Ptrac):
        """
        Initializes ``ProcessedPtrac``.

        Parameters:
            ptrac: ``Ptrac`` to process.
        """

        self.ptrac: Ptrac = ptrac

    def prehook(self):
        """
        Runs before ``run``.
        """

        pass

    def posthook(self):
        """
        Runs after ``run``.
        """

        pass

    def process_source(event: Event):
        """
        Runs when ``run`` processes PTRAC source events.
        """

        raise NotImplementedError

    def process_bank(event: Event):
        """
        Runs when ``run`` processes PTRAC bank events.
        """

        raise NotImplementedError

    def process_surface(event: Event):
        """
        Runs when ``run`` processes PTRAC surface events.
        """

        raise NotImplementedError

    def process_collision(event: Event):
        """
        Runs when ``run`` processes PTRAC collision events.
        """

        raise NotImplementedError

    def process_terminal(event: Event):
        """
        Runs when ``run`` processes PTRAC termianl events.
        """

        raise NotImplementedError

    def process_flag(event: Event):
        """
        Runs when ``run`` processes PTRAC source events.
        """

        raise NotImplementedError

    def run(self):
        """
        Processes PTRAC.
        """

        self.prehook()

        for history in self.ptrac.history:
            for event in history:
                match event.event_type:
                    case EventType.SOURCE:
                        self.process_source(event)
                    case EventType.SURFACE:
                        self.process_surface(event)
                    case EventType.COLLISION:
                        self.process_collision(event)
                    case EventType.TERMINAL:
                        self.process_terminal(event)
                    case EventType.FLAG:
                        self.process_flag(event)
                    case _:
                        self.process_bank(event)

        self.posthook()
