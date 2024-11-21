"""
Contains the ``FilteredPtrac`` for filtering PTRAC file.
"""

from .event import Event, EventType
from .ptrac import Ptrac


class FilteredPtrac:
    """
    Filters PTRAC files.

    ``FilteredPtrac`` provides helper methods and stubs for processing PTRAC.
    Subclasses override its methods to specify how ``run`` processes PTRAC.

    Attributes:
        ptrac: ``Ptrac`` to filter.
    """

    def __init__(self, ptrac: Ptrac):
        """
        Initializes ``FilteredPtrac``.

        Parameters:
            ptrac: ``Ptrac`` to filter.
        """

        self.ptrac: Ptrac = ptrac

    @staticmethod
    def filter_source(event: Event) -> bool:
        """
        Runs when ``run`` filters PTRAC source events.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        raise NotImplementedError

    @staticmethod
    def filter_bank(event: Event) -> bool:
        """
        Runs when ``run`` filters PTRAC bank events.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        raise NotImplementedError

    @staticmethod
    def filter_surface(event: Event) -> bool:
        """
        Runs when ``run`` filters PTRAC surface events.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        raise NotImplementedError

    @staticmethod
    def filter_collision(event: Event) -> bool:
        """
        Runs when ``run`` filters PTRAC collision events.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        raise NotImplementedError

    @staticmethod
    def filter_terminal(event: Event) -> bool:
        """
        Runs when ``run`` filters PTRAC terminal events.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        raise NotImplementedError

    @staticmethod
    def filter_flag(event: Event) -> bool:
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
                        case EventType.SOURCE:
                            _filter = self.filter_source
                        case EventType.SURFACE:
                            _filter = self.filter_surface
                        case EventType.COLLISION:
                            _filter = self.filter_collision
                        case EventType.TERMINAL:
                            _filter = self.filter_terminal
                        case EventType.FLAG:
                            _filter = self.filter_flag
                        case _:
                            _filter = self.filter_bank

                    if _filter(event):
                        yield event
                    else:
                        continue
            return

        return histories
