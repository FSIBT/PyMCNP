import re
import typing

from . import _line
from .EventType import EventType
from ...utils import types
from ...utils import errors


class I(_line.HistoryLine):
    """
    Represents PTRAC history block I lines.

    Attributes:
        nps: I nps.
        event_type: I first event type.
        number: Cell/surface/tally number.
        tfc: TFC bin tally.
    """

    _REGEX = re.compile(r'\A(.{10})(.{10})(.{10})(.{13})\Z')

    def __init__(
        self,
        nps: types.Integer,
        event_type: EventType,
        number: types.Integer,
        tfc: types.Real,
    ):
        """
        Initializes ``I``.

        Parameters:
            nps: I nps.
            event_type: I first event type.
            number: Cell/surface/tally number.
            tfc: TFC bin tally.

        Raises:
            PtracError: SEMANTICS_LINE.
        """

        if nps is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, nps)

        if event_type is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, event_type)

        if number is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, number)

        if tfc is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, tfc)

        self.nps: typing.Final[types.Integer] = nps
        self.event_type: typing.Final[EventType] = event_type
        self.number: typing.Final[types.Integer] = number
        self.tfc: typing.Final[types.Real] = tfc

    def from_mcnp(source: str):
        """
        Generates ``I`` from PTRAC.

        Parameters:
            source: PTRAC for ``I``.

        Returns:
            ``I``.

        Raises:
            PtracError: SYNTAX_HISTORY_LINE.
        """

        tokens = I._REGEX.match(source)

        if not tokens:
            raise errors.PtracError(errors.PtracCode.SYNTAX_HISTORY_LINE, source)

        nps = types.Integer.from_mcnp(tokens[1])
        event_type = EventType.from_mcnp(tokens[2].strip())
        number = types.Integer.from_mcnp(tokens[3])
        tfc = types.Real.from_mcnp(tokens[4])

        return I(
            nps,
            event_type,
            number,
            tfc,
        )

    def to_mcnp(self):
        """
        Generates PTRAC from ``I``.

        Returns:
            PTRAC for ``I``.
        """

        return f'{self.nps:>10}{self.event_type:>10}{self.number:>10}{self.tfc:>13.5E}'
