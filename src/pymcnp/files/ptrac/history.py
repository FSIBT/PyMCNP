"""
Contains classes representing INP histories.
"""

from __future__ import annotations
from typing import Final, Generator

from .event import Event, EventType
from .header import Header
from ..utils import types
from ..utils import errors
from ..utils import _parser
from ..utils import _object


class History(_object.PyMcnpObject):
    """
    Represents PTRAC event histories.

    ``History`` implements ``_object.PyMcnpObject``.

    Attributes:
        header: History context, i.e. PTRAC header.
        next_type: Event type of the next event.
        nps: Count of source particles started.
        ncl: Problem numbers of the cells.
        nsf: Problem transformation of the surfaces.
        jptal: Basic tally information.
        tal: Tally scores accumulation.
        events: List of events in the PTRAC
    """

    def __init__(
        self,
        header: Header,
        next_type: EventType,
        nps: int,
        ncl: int,
        nsf: int,
        jptal: int,
        tal: int,
        events: Generator[Event, None, None],
    ):
        """
        Initializes ``History``.

        Parameters:
            header: History context, i.e. PTRAC header.
            next_type: Event type of the next event.
            nps: Count of source particles started.
            ncl: Problem numbers of the cells.
            nsf: Problem transformation of the surfaces.
            jptal: Basic tally information.
            tal: Tally scores accumulation.
            events: List of events in the PTRAC

        Raises:
            McnpError: INVALID_HISTORY_NEXTTYPE.
            McnpError: INVALID_HISTORY_NPS.
            McnpError: INVALID_HISTORY_NCL.
            McnpError: INVALID_HISTORY_NSF.
            McnpError: INVALID_HISTORY_JPTAL.
            McnpError: INVALID_HISTORY_TAL.
            McnpError: INVALID_PTRAC_HEADER.
            McnpError: INVALID_PTRAC_EVENT.
        """

        self.next_type: Final[EventType] = next_type
        self.nps: Final[int] = nps
        self.ncl: Final[int] = ncl
        self.nsf: Final[int] = nsf
        self.jptal: Final[int] = jptal
        self.tal: Final[int] = tal
        self.header: Final[Header] = header
        self.events: Final[Generator[Event]] = events

    @staticmethod
    def from_mcnp(source: str, header: Header) -> tuple[History, str]:
        """
        Generates ``History`` objects from PTRAC.

        ``from_mcnp`` translates from PTRAC to PyMCNP; it parses PTRAC.

        Parameters:
            source: PTRAC for ``History``.
            head: PTRAC header.

        Returns:
            ``History`` object.

        Raises:
            McnpError: TOOFEW_HISTORY.
        """

        nps = None
        ncl = None
        nsf = None
        jptal = None
        tal = None
        next_type = None

        source = _parser.Preprocessor.process_ptrac(source)
        lines = _parser.Parser(
            source.split('\n'),
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source),
        )

        # Processing I Line
        tokens = _parser.Parser.from_fortran(
            (header.numbers[0].value - 1) * [10] + [13],
            lines.popl()[1:],
            errors.McnpError(errors.McnpCode.TOOFEW_HEADER),
        )

        for i in range(0, header.numbers[0].value):
            match header.ids[i].value:
                case 1:
                    nps = types.McnpInteger.from_mcnp(tokens.popl().strip())
                case 2:
                    next_type = EventType.from_mcnp(tokens.popl().strip())
                    first_next_type = next_type
                case 3:
                    ncl = types.McnpInteger.from_mcnp(tokens.popl().strip())
                case 4:
                    nsf = types.McnpInteger.from_mcnp(tokens.popl().strip())
                case 5:
                    jptal = types.McnpInteger.from_mcnp(tokens.popl().strip())
                case 6:
                    tal = types.McnpReal.from_mcnp(tokens.popl().strip())
                case _:
                    assert False

        # Processing J & P Lines
        event_lines = _parser.Parser([], errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, source))

        def events(next_type, lines):
            while next_type != EventType.FLAG:
                event = Event.from_mcnp(lines.popl() + '\n' + lines.popl(), header, next_type)
                next_type = event.next_type
                yield event

        while lines and lines.peekl() and not lines.peekl().startswith('       9000'):
            event_lines.pushr(lines.popl())
        event_lines.pushr(lines.popl())
        event_lines.pushr(lines.popl())

        return (
            History(
                header,
                first_next_type,
                nps,
                ncl,
                nsf,
                jptal,
                tal,
                events(next_type, event_lines),
            ),
            '\n'.join(list(lines.deque)),
        )

    def to_mcnp(self):
        """
        Generates PTRAC from ``History`` objects.

        ``to_mcnp`` translates from PTRAC to PyMCNP.

        Returns:
            INP for ``History``.
        """

        assert False, 'NotImplemented'
