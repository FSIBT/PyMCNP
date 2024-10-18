"""
``history`` contains classes representing PTRAC histories.

``history`` packages the ``History`` class, providing an object-oriented,
importable interface for PTRAC event histories.
"""

from __future__ import annotations

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
        events: List of events in the PTRAC history.
    """

    def __init__(self):
        """
        ``__init__`` initializes ``History``.
        """

        self.header: Header = None
        self.next_type: Event.EventType = None
        self.nps: int = None
        self.ncl: int = None
        self.nsf: int = None
        self.jptal: int = None
        self.tal: int = None

        self.events: list[Event] = None

    def set_nps(self, nps: int) -> None:
        """
        ``set_nps`` stores PTRAC history nps variable.

        ``set_code`` checks given arguments before assigning the given value
        to ``code.nps``. If given an unrecognized argument, it raises
        semantic errors.

        Parameters:
            nps: Count of source particles started.

        Raises:
            MCNPSemanticError: INVALID_HISTORY_NPS.
        """

        if nps is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_HISTORY_NPS)

        self.nps = nps

    def set_ncl(self, ncl: int) -> None:
        """
        ``set_ncl`` stores PTRAC history ncl variable.

        ``set_ncl`` checks given arguments before assigning the given value
        to ``code.ncl``. If given an unrecognized argument, it raises
        semantic errors.

        Parameters:
            ncl: Problem numbers of the cells.

        Raises:
            MCNPSemanticError: INVALID_HISTORY_NCL.
        """

        if ncl is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_HISTORY_NCL)

        self.ncl = ncl

    def set_nsf(self, nsf: int) -> None:
        """
        ``set_nsf`` stores PTRAC history nsf variable.

        ``set_nsf`` checks given arguments before assigning the given value
        to ``code.nsf``. If given an unrecognized argument, it raises
        semantic errors.

        Parameters:
            nsf: Problem transformation of the surfaces.

        Raises:
            MCNPSemanticError: INVALID_HISTORY_NSF.
        """

        if nsf is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_HISTORY_NSF)

        self.nsf = nsf

    def set_jptal(self, jptal: int) -> None:
        """
        ``set_jptal`` stores PTRAC history jptal variable.

        ``set_jptal`` checks given arguments before assigning the given value
        to ``code.jptal``. If given an unrecognized argument, it raises
        semantic errors.

        Parameters:
            jptal: Basic tally information.

        Raises:
            MCNPSemanticError: INVALID_HISTORY_JPTAL.
        """

        if jptal is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_HISTORY_JPTAL)

        self.jptal = jptal

    def set_tal(self, tal: int) -> None:
        """
        ``set_tal`` stores PTRAC history tal variable.

        ``set_tal`` checks given arguments before assigning the given value
        to ``code.tal``. If given an unrecognized argument, it raises
        semantic errors.

        Parameters:
            tal: Tally scores accumulation.

        Raises:
            MCNPSemanticError: INVALID_HISTORY_TAL.
        """

        if tal is None:
            raise errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_HISTORY_TAL)

        self.tal = tal

    def set_next_type(self, next_type: Event.EventType) -> None:
        """
        ``set_next_type`` stores PTRAC history first event type variable.

        ``set_next_type`` checks given arguments before assigning the given
        value to ``code.next_type``. If given an unrecognized argument, it
        raises semantic errors.

        Parameters:
            next_type: Event type of the next event.

        Raises:
            MCNPSemanticError: INVALID_HISTORY_NEXTTYPE.
        """

        if next_type is None:
            return errors.MCNPSemanticError(errors.MCNPSemanticCodes.INVALID_HISTORY_NEXTTYPE)

        self.next_type = next_type

    @classmethod
    def from_mcnp(cls, source: str, header: Header) -> tuple[History, str]:
        """
        ``from_mcnp`` generates ``History`` objects from PTRAC.

        ``from_mcnp`` constructs instances of ``History`` from PTRAC source
        strings, so it operates as a class constructor method and PTRAC parser
        helper function.

        Parameters:
            source: PTRAC for history.
            header: PTRAC header.

        Returns:
            ``History`` object.

        Raises:
            MCNPSyntaxError: TOOFEW_HISTORY, TOOLONG_HISTORY.
        """

        history = cls()
        history.header = header

        source = _parser.Preprocessor.process_ptrac(source)
        lines = _parser.Parser(
            source.split('\n'), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOFEW_HISTORY)
        )

        # Processing I Line
        tokens = _parser.Parser(
            lines.popl().strip().split(' '),
            errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOFEW_HISTORY),
        )
        if len(tokens) != header.numbers[0]:
            raise SyntaxError

        for i in range(0, header.numbers[0]):
            match header.ids[i]:
                case '1':
                    value = types.cast_fortran_integer(tokens.popl())
                    history.set_nps(value)
                case '2':
                    value = Event.EventType.from_mcnp(tokens.popl())
                    history.set_next_type(value)
                case '3':
                    value = types.cast_fortran_integer(tokens.popl())
                    history.set_ncl(value)
                case '4':
                    value = types.cast_fortran_integer(tokens.popl())
                    history.set_nsf(value)
                case '5':
                    value = types.cast_fortran_integer(tokens.popl())
                    history.set_jptal(value)
                case '6':
                    value = types.cast_fortran_real(tokens.popl())
                    history.set_tal(value)

        # Processing J & P Lines
        events = []

        tokens = _parser.Parser(
            lines.peekl().split(' '), errors.MCNPSyntaxError(errors.MCNPSyntaxCodes.TOFEW_HISTORY)
        )

        next_type = history.next_type
        while next_type != Event.EventType.FLAG:
            event = Event().from_mcnp(lines.popl() + '\n' + lines.popl(), history.header, next_type)
            events.append(event)
            next_type = event.next_type

        history.events = tuple(events)

        return history, '\n'.join(list(lines.deque))

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
