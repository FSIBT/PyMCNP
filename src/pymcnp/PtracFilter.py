from . import _doer
from . import ptrac
from .Ptrac import Ptrac


class PtracFilter(_doer.Doer):
    """
    Filters PTRAC files.
    """

    @staticmethod
    def check_source(event: ptrac.history.event.j.EventType) -> bool:
        """
        Runs when filtering source events.

        Parameters:
            event: Event to filter.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        return True

    @staticmethod
    def check_bank(event: ptrac.history.event.j.EventType) -> bool:
        """
        Runs when filtering bank events.

        Parameters:
            event: Event to filter.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        return True

    @staticmethod
    def check_surface(event: ptrac.history.event.j.EventType) -> bool:
        """
        Runs when filtering surface events.

        Parameters:
            event: Event to filter.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        return True

    @staticmethod
    def check_collision(event: ptrac.history.event.j.EventType) -> bool:
        """
        Runs when filtering collision events.

        Parameters:
            event: Event to filter.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        return True

    @staticmethod
    def check_terminal(event: ptrac.history.event.j.EventType) -> bool:
        """
        Runs when filtering terminal events.

        Parameters:
            event: Event to filter.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        return True

    def __call__(self, file: Ptrac):
        """
        Filters `Ptrac`.

        Parameters:
            file: File to filter.

        Yields:
            Accepted events.
        """

        def histories():
            for history in file.histories:
                kind = history.i_line.event_type
                for event in history.events:
                    match kind:
                        case ptrac.history.event.j.EventType.SOURCE:
                            check = self.check_source
                        case ptrac.history.event.j.EventType.SURFACE:
                            check = self.check_surface
                        case ptrac.history.event.j.EventType.COLLISION:
                            check = self.check_collision
                        case ptrac.history.event.j.EventType.TERMINAL:
                            check = self.check_terminal
                        case _:
                            check = self.check_bank

                    kind = event.j_line.next_type

                    if check(event):
                        yield event
                    else:
                        continue

        return histories()
