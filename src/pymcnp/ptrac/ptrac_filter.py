"""
Contains the ``FilterPtrac`` for filtering PTRAC file.
"""

from .history import HistoryKeyword_Type
from .ptrac import Ptrac


class FilterPtrac:
    """
    Filters PTRAC files.

    ``FilterPtrac`` provides helper methods and stubs for processing PTRAC.
    Subclasses override its methods to specify how ``run`` processes PTRAC.

    Attributes:
        ptrac: ``Ptrac`` to filter.
    """

    def __init__(self, ptrac: Ptrac):
        """
        Initializes ``FilterPtrac``.

        Parameters:
            ptrac: ``Ptrac`` to filter.
        """

        self.ptrac: Ptrac = ptrac

    @staticmethod
    def filter_source(event: HistoryKeyword_Type) -> bool:
        """
        Runs when ``run`` filters PTRAC source events.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        raise NotImplementedError

    @staticmethod
    def filter_bank(event: HistoryKeyword_Type) -> bool:
        """
        Runs when ``run`` filters PTRAC bank events.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        raise NotImplementedError

    @staticmethod
    def filter_surface(event: HistoryKeyword_Type) -> bool:
        """
        Runs when ``run`` filters PTRAC surface events.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        raise NotImplementedError

    @staticmethod
    def filter_collision(event: HistoryKeyword_Type) -> bool:
        """
        Runs when ``run`` filters PTRAC collision events.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        raise NotImplementedError

    @staticmethod
    def filter_terminal(event: HistoryKeyword_Type) -> bool:
        """
        Runs when ``run`` filters PTRAC terminal events.

        Returns:
            True/False if the given event should/shouldn't be kept.
        """

        raise NotImplementedError

    @staticmethod
    def filter_flag(event: HistoryKeyword_Type) -> bool:
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
                        case HistoryKeyword_Type.SOURCE:
                            _filter = self.filter_source
                        case HistoryKeyword_Type.SURFACE:
                            _filter = self.filter_surface
                        case HistoryKeyword_Type.COLLISION:
                            _filter = self.filter_collision
                        case HistoryKeyword_Type.TERMINAL:
                            _filter = self.filter_terminal
                        case HistoryKeyword_Type.FLAG:
                            _filter = self.filter_flag
                        case _:
                            _filter = self.filter_bank

                    if _filter(event):
                        yield event
                    else:
                        continue
            return

        return histories
