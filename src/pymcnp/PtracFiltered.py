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
    def filter_source(event: ptrac.history.EventType) -> bool:
        """
        Runs when ``run`` filters PTRAC source events.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        raise NotImplementedError

    @staticmethod
    def filter_bank(event: ptrac.history.EventType) -> bool:
        """
        Runs when ``run`` filters PTRAC bank events.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        raise NotImplementedError

    @staticmethod
    def filter_surface(event: ptrac.history.EventType) -> bool:
        """
        Runs when ``run`` filters PTRAC surface events.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        raise NotImplementedError

    @staticmethod
    def filter_collision(event: ptrac.history.EventType) -> bool:
        """
        Runs when ``run`` filters PTRAC collision events.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        raise NotImplementedError

    @staticmethod
    def filter_terminal(event: ptrac.history.EventType) -> bool:
        """
        Runs when ``run`` filters PTRAC terminal events.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        raise NotImplementedError

    @staticmethod
    def filter_flag(event: ptrac.history.EventType) -> bool:
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
            for history in self.ptrac.history:
                for event in self.ptracFile.history.events:
                    match event.event_type:
                        case ptrac.history.EventType.SOURCE:
                            _filter = self.filter_source
                        case ptrac.history.EventType.SURFACE:
                            _filter = self.filter_surface
                        case ptrac.history.EventType.COLLISION:
                            _filter = self.filter_collision
                        case ptrac.history.EventType.TERMINAL:
                            _filter = self.filter_terminal
                        case ptrac.history.EventType.FLAG:
                            _filter = self.filter_flag
                        case _:
                            _filter = self.filter_bank

                    if _filter(event):
                        yield event
                    else:
                        continue
            return

        return histories
