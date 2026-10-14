import re

from . import event
from . import _line
from ... import types
from ... import errors
from ... import _fields


class I(_fields.Fields, _line.HistoryLine):
    """
    Represents PTRAC history block I lines.

    Attributes:
        nps: I nps.
        event_type: I first event type.
        number: Cell/surface/tally number.
        tfc: TFC bin tally.
    """

    _REGEX = re.compile(r'\A\s(.{10})(.{10})(.{10})?(.{13})?\Z', re.IGNORECASE)

    _ERROR = errors.PtracError
    _CODE = errors.PtracCode.SEMANTICS_LINE

    nps = _fields.Field(types.Integer, 'I nps')
    event_type = _fields.Field(event.j.EventType, 'I first event type')
    number = _fields.Field(types.Integer, 'Cell/surface/tally number', optional=True)
    tfc = _fields.Field(types.Real, 'TFC bin tally', optional=True)

    def from_mcnp(source: str):
        """
        Generates `I` from PTRAC.

        Parameters:
            source: PTRAC for `I`.

        Returns:
            `I`.

        Raises:
            PtracError: SYNTAX_LINE.
        """

        tokens = I._REGEX.match(source)

        if not tokens:
            raise errors.PtracError(errors.PtracCode.SYNTAX_LINE, source)

        nps = types.Integer.from_mcnp(tokens[1])
        event_type = event.j.EventType.from_mcnp(tokens[2].strip())
        number = types.Integer.from_mcnp(tokens[3]) if tokens[3] else None
        tfc = types.Real.from_mcnp(tokens[4]) if tokens[4] else None

        return I(
            nps,
            event_type,
            number,
            tfc,
        )

    def to_mcnp(self):
        """
        Generates PTRAC from `I`.

        Returns:
            PTRAC for `I`.
        """

        if self.tfc:
            tfc = f' {self.tfc:5.0a}'
        else:
            tfc = ''

        if self.number:
            number = f'{str(self.number):>10}'
        else:
            number = ''

        return f' {str(self.nps):>10}{str(self.event_type):>10}{number}{tfc}'
