from . import abc
from . import ptrac
from .Ptrac import Ptrac


class PtracProcessor(abc.Utility):
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

    def process_source(self, event: ptrac.block.Event):
        """
        Processes source events.

        Parameters:
            event: Source event to process.
        """

        pass

    def process_bank(self, event: ptrac.block.Event):
        """
        Processes bank events.

        Parameters:
            event: Bank event to process.
        """

        pass

    def process_surface(self, event: ptrac.block.Event):
        """
        Processes surface events.

        Parameters:
            event: Surface event to process.
        """

        pass

    def process_collision(self, event: ptrac.block.Event):
        """
        Processes collision events.

        Parameters:
            event: Collision event to process.
        """

        pass

    def process_terminal(self, event: ptrac.block.Event):
        """
        Processes terminal events.

        Parameters:
            event: Terminal event to process.
        """

        pass

    def run(self, file: Ptrac):
        """
        Processes ptrac files.

        Parameters:
            file: Ptrac file to process.
        """

        self.prehook()

        for history in file.histories:
            kind = history.i.event_type
            for event in history.events:
                match kind.strip():
                    case '1000':
                        self.process_source(event)
                    case '3000':
                        self.process_surface(event)
                    case '4000':
                        self.process_collision(event)
                    case '5000':
                        self.process_terminal(event)
                    case _:
                        self.process_bank(event)

                kind = event.j.type

        self.posthook()
