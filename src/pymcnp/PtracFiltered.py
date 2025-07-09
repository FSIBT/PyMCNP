from . import ptrac
from .Ptrac import Ptrac


class PtracFiltered:
    """
    Filters PTRAC files.

    Attributes:
        ptrac: ``Ptrac`` to filter.
    """

    def __init__(self, ptrac: Ptrac):
        """
        Initializes ``PtracFiltered``.

        Parameters:
            ptrac: ``Ptrac`` to filter.
        """

        self.ptrac: Ptrac = ptrac

    @staticmethod
    def check_source(event: ptrac.history.event.j.EventType) -> bool:
        """
        Runs when ``run`` filters PTRAC source events.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        raise NotImplementedError

    @staticmethod
    def check_bank(event: ptrac.history.event.j.EventType) -> bool:
        """
        Runs when ``run`` filters PTRAC bank events.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        raise NotImplementedError

    @staticmethod
    def check_surface(event: ptrac.history.event.j.EventType) -> bool:
        """
        Runs when ``run`` filters PTRAC surface events.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        raise NotImplementedError

    @staticmethod
    def check_collision(event: ptrac.history.event.j.EventType) -> bool:
        """
        Runs when ``run`` filters PTRAC collision events.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        raise NotImplementedError

    @staticmethod
    def check_terminal(event: ptrac.history.event.j.EventType) -> bool:
        """
        Runs when ``run`` filters PTRAC terminal events.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        raise NotImplementedError

    @staticmethod
    def check_flag(event: ptrac.history.event.j.EventType) -> bool:
        """
        Runs when ``run`` filters PTRAC flag events.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        raise NotImplementedError

    def run(self):
        """
        Filters PTRAC.
        """

        def histories():
            for history in self.ptrac.histories:
                for event in self.ptracFile.history.events:
                    match event.event_type:
                        case ptrac.history.event.j.EventType.SOURCE:
                            check = self.check_source
                        case ptrac.history.event.j.EventType.SURFACE:
                            check = self.check_surface
                        case ptrac.history.event.j.EventType.COLLISION:
                            check = self.check_collision
                        case ptrac.history.event.j.EventType.TERMINAL:
                            check = self.check_terminal
                        case ptrac.history.event.j.EventType.FLAG:
                            check = self.check_flag
                        case _:
                            check = self.check_bank

                    if check(event):
                        yield event
                    else:
                        continue

        return histories
