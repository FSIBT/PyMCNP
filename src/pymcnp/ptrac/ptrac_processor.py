"""
Contains the ``ProcessorPtrac`` class for processing PTRAC.
"""

from .history import HistoryKeyword_Type
from .ptrac import Ptrac


class ProcessorPtrac:
    """
    Processes PTRAC.

    ``ProcessorPtrac`` provides helper methods and stubs for processing PTRAC.
    Subclasses override its methods to specify how ``run`` processes PTRAC.

    Attributes:
        ptrac: ``Ptrac`` to process.
    """

    def __init__(self, ptrac: Ptrac):
        """
        Initializes ``ProcessorPtrac``.

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

    def process_source(self, event: HistoryKeyword_Type):
        """
        Runs when ``run`` processes PTRAC source events.
        """

        raise NotImplementedError

    def process_bank(self, event: HistoryKeyword_Type):
        """
        Runs when ``run`` processes PTRAC bank events.
        """

        raise NotImplementedError

    def process_surface(self, event: HistoryKeyword_Type):
        """
        Runs when ``run`` processes PTRAC surface events.
        """

        raise NotImplementedError

    def process_collision(self, event: HistoryKeyword_Type):
        """
        Runs when ``run`` processes PTRAC collision events.
        """

        raise NotImplementedError

    def process_terminal(self, event: HistoryKeyword_Type):
        """
        Runs when ``run`` processes PTRAC termianl events.
        """

        raise NotImplementedError

    def process_flag(self, event: HistoryKeyword_Type):
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
                    case HistoryKeyword_Type.SOURCE:
                        self.process_source(event)
                    case HistoryKeyword_Type.SURFACE:
                        self.process_surface(event)
                    case HistoryKeyword_Type.COLLISION:
                        self.process_collision(event)
                    case HistoryKeyword_Type.TERMINAL:
                        self.process_terminal(event)
                    case HistoryKeyword_Type.FLAG:
                        self.process_flag(event)
                    case _:
                        self.process_bank(event)

        self.posthook()
