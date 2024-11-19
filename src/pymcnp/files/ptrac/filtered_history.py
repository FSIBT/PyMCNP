"""
Contains classes representing filtered PTRAC histories.
"""

from . import filters
from . import history
from . import header
from . import event


class FilteredHistory(history.History):
    @staticmethod
    def from_mcnp(source: str, head: header.Header, filters: filters.Filters) -> str:
        """
        ``from_mcnp`` generates ``FilteredHistory`` objects from PTRAC.

        ``from_mcnp`` constructs instances of ``FilteredHistory`` from PTRAC source
        strings, so it operates as a class constructor method and PTRAC parser
        helper function.

        Parameters:
            source: PTRAC source.
            head: PTRAC header.
            filters: PyMCNP PTRAC filters.

        Returns:
            ``FilteredHistory`` object.

        Raises:
            MCNPSyntaxError: TOOFEW_HISTORY, TOOLONG_HISTORY.
        """

        hist, lines = history.History.from_mcnp(source, head)

        def events(hist):
            for evnt in hist.events:
                match evnt.event_type:
                    case event.EventType.SOURCE:
                        filter_ = filters.filteredsource
                    case event.EventType.SURFACE:
                        filter_ = filters.filteredsurface
                    case event.EventType.COLLISION:
                        filter_ = filters.filteredcollision
                    case event.EventType.TERMINAL:
                        filter_ = filters.filteredterminal
                    case event.EventType.FLAG:
                        filter_ = filters.fitler_flag
                    case _:
                        filter_ = filters.filteredbank

                if not filter_(evnt):
                    return

        return (
            FilteredHistory(
                head,
                hist.next_type,
                hist.nps,
                hist.ncl,
                hist.nsf,
                hist.jptal,
                hist.tal,
                events(hist),
            ),
            lines,
        )
