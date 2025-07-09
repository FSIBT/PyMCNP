from . import ptrac
from .Ptrac import Ptrac


class PtracProcessed:
    """
    Processes PTRAC.

    Attributes:
        ptrac: ``Ptrac`` to process.
    """

    def __init__(self, ptrac: Ptrac):
        """
        Initializes ``PtracProcessed``.

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

    def process_source(self, event: ptrac.history.event.j.EventType):
        """
        Runs when ``run`` processes PTRAC source events.
        """

        raise NotImplementedError

    def process_bank(self, event: ptrac.history.event.j.EventType):
        """
        Runs when ``run`` processes PTRAC bank events.
        """

        raise NotImplementedError

    def process_surface(self, event: ptrac.history.event.j.EventType):
        """
        Runs when ``run`` processes PTRAC surface events.
        """

        raise NotImplementedError

    def process_collision(self, event: ptrac.history.event.j.EventType):
        """
        Runs when ``run`` processes PTRAC collision events.
        """

        raise NotImplementedError

    def process_terminal(self, event: ptrac.history.event.j.EventType):
        """
        Runs when ``run`` processes PTRAC termianl events.
        """

        raise NotImplementedError

    def process_flag(self, event: ptrac.history.event.j.EventType):
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
                    case ptrac.history.event.j.EventType.SOURCE:
                        self.process_source(event)
                    case ptrac.history.event.j.EventType.SURFACE:
                        self.process_surface(event)
                    case ptrac.history.event.j.EventType.COLLISION:
                        self.process_collision(event)
                    case ptrac.history.event.j.EventType.TERMINAL:
                        self.process_terminal(event)
                    case ptrac.history.event.j.EventType.FLAG:
                        self.process_flag(event)
                    case _:
                        self.process_bank(event)

        self.posthook()
