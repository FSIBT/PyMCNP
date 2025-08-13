from . import _doer
from . import ptrac
from .Ptrac import Ptrac


class PtracProcessor(_doer.Doer):
    """
    Processes `Ptrac`.
    """

    def prehook(self):
        """
        Runs before processing.
        """

        pass

    def posthook(self):
        """
        Runs after processing.
        """

        pass

    def process_source(self, event: ptrac.history.event.j.EventType):
        """
        Runs when processing source events.

        Parameters:
            event: Event to process.
        """

        pass

    def process_bank(self, event: ptrac.history.event.j.EventType):
        """
        Runs when processing bank events.

        Parameters:
            event: Event to process.
        """

        pass

    def process_surface(self, event: ptrac.history.event.j.EventType):
        """
        Runs when processing surface events.

        Parameters:
            event: Event to process.
        """

        pass

    def process_collision(self, event: ptrac.history.event.j.EventType):
        """
        Runs when processing collision events.

        Parameters:
            event: Event to process.
        """

        pass

    def process_terminal(self, event: ptrac.history.event.j.EventType):
        """
        Runs when processing termianl events.

        Parameters:
            event: Event to process.
        """

        pass

    def __call__(self, file: Ptrac):
        """
        Processes `Ptrac`.

        Parameters:
            file: File to process.
        """

        self.prehook()

        for history in file.histories:
            kind = history.i_line.event_type
            for event in history.events:
                match kind:
                    case ptrac.history.event.j.EventType.SOURCE:
                        self.process_source(event)
                    case ptrac.history.event.j.EventType.SURFACE:
                        self.process_surface(event)
                    case ptrac.history.event.j.EventType.COLLISION:
                        self.process_collision(event)
                    case ptrac.history.event.j.EventType.TERMINAL:
                        self.process_terminal(event)
                    case _:
                        self.process_bank(event)

                kind = event.j_line.next_type

        self.posthook()
