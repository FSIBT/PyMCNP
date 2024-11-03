"""
``history`` contains classes representing PTRAC histories.

``history`` packages the ``History`` class, providing an object-oriented,
importable interface for PTRAC event histories.
"""

from __future__ import annotations
from typing import Final

from .event import Event
from .header import Header
from ..utils import _parser
from ..utils import errors
from ..utils import types


class History:
    """
    ``History`` represents PTRAC event histories.

    ``History`` implements PTRAC event histories as a Python class. Its
    attributes store PTRAC event hisotry metadata and data parameters, and its
    methods provide entry points and endpoints for working with PTRAC. It
    represents the PTRAC event history syntax element.

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
        next_type: Event.EventType,
        nps: int,
        ncl: int,
        nsf: int,
        jptal: int,
        tal: int,
        events: tuple[Event],
    ):
        """
        ``__init__`` initializes ``History``.

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
            MCNPSemanticError: INVALID_HISTORY_NEXTTYPE.
            MCNPSemanticError: INVALID_HISTORY_NPS.
            MCNPSemanticError: INVALID_HISTORY_NCL.
            MCNPSemanticError: INVALID_HISTORY_NSF.
            MCNPSemanticError: INVALID_HISTORY_JPTAL.
            MCNPSemanticError: INVALID_HISTORY_TAL.
            MCNPSemanticError: INVALID_PTRAC_HEADER.
            MCNPSemanticError: INVALID_PTRAC_EVENT.
        """

        # TODO: Add error checking here!

        self.next_type: Final[Event.EventType] = next_type
        self.nps: Final[int] = nps
        self.ncl: Final[int] = ncl
        self.nsf: Final[int] = nsf
        self.jptal: Final[int] = jptal
        self.tal: Final[int] = tal
        self.header: Final[Header] = header
        self.events: Final[tuple[Event]] = events

    @staticmethod
    def from_mcnp(source: str, header: Header) -> tuple[History, str]:
        """
        ``from_mcnp`` generates ``History`` objects from PTRAC.

        ``from_mcnp`` constructs instances of ``History`` from PTRAC source
        strings, so it operates as a class constructor method and PTRAC parser
        helper function.

        Parameters:
            source: PTRAC for
            header: PTRAC header.

        Returns:
            ``History`` object.

        Raises:
            MCNPSyntaxError: TOOFEW_HISTORY, TOOLONG_HISTORY.
        """

        nps = None
        ncl = None
        nsf = None
        jptal = None
        tal = None

        source = _parser.Preprocessor.process_ptrac(source)
        lines = _parser.Parser(
            source.split('\n'), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOFEW_HISTORY)
        )

        # Processing I Line
        tokens = _parser.Parser(
            lines.popl().strip().split(' '),
            errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOFEW_HISTORY),
        )
        if len(tokens) != header.numbers[0].value:
            raise SyntaxError

        for i in range(0, header.numbers[0].value):
            match header.ids[i]:
                case '1':
                    nps = types.McnpInteger.from_mcnp(tokens.popl())
                case '2':
                    next_type = Event.EventType.from_mcnp(tokens.popl())
                case '3':
                    ncl = types.McnpInteger.from_mcnp(tokens.popl())
                case '4':
                    nsf = types.McnpInteger.from_mcnp(tokens.popl())
                case '5':
                    jptal = types.McnpInteger.from_mcnp(tokens.popl())
                case '6':
                    tal = types.McnpReal.from_mcnp(tokens.popl())

        # Processing J & P Lines
        events = []

        tokens = _parser.Parser(
            lines.peekl().split(' '), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOFEW_HISTORY)
        )

        next_type = next_type
        while next_type != Event.EventType.FLAG:
            event = Event.from_mcnp(lines.popl() + '\n' + lines.popl(), header, next_type)
            events.append(event)
            next_type = event.next_type

        events = tuple(events)

        return History(header, next_type, nps, ncl, nsf, jptal, tal, events), '\n'.join(
            list(lines.deque)
        )

    def to_arguments(self) -> dict:
        """
        ``to_arguments`` makes dictionaries from ``History`` objects.

        ``to_arguments`` creates Python dictionaries from ``History`` objects,
        so it provides an MCNP endpoint. The dictionary keys follow the MCNP
        manual.

        Returns:
            Dictionary for ``History`` object.
        """

        return {
            'nps': self.nps,
            'ncl': self.ncl,
            'nsf': self.nsf,
            'jptal': self.jptal,
            'tal': self.tal,
            'events': [event.to_arguments() for event in self.events],
        }
