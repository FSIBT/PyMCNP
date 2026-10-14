import re


from . import event
from . import _block
from ... import errors
from ... import _fields


class Event(_fields.Fields, _block.HistoryBlock):
    """
    Represents PTRAC history block events.

    Attributes:
        j_line: Event j-line.
        p_line: Event p-line.
    """

    _REGEX = re.compile(
        rf'\A((?:{event.J_0._REGEX.pattern[2:-2]})|(?:{event.J_1._REGEX.pattern[2:-2]})|(?:{event.J_2._REGEX.pattern[2:-2]})|(?:{event.J_3._REGEX.pattern[2:-2]})|(?:{event.J_4._REGEX.pattern[2:-2]})|(?:{event.J_5._REGEX.pattern[2:-2]})|(?:{event.J_6._REGEX.pattern[2:-2]})|(?:{event.J_7._REGEX.pattern[2:-2]}))\n((?:{event.P_0._REGEX.pattern[2:-2]})|(?:{event.P_1._REGEX.pattern[2:-2]}))\n\Z',
        re.IGNORECASE,
    )

    _ERROR = errors.PtracError
    _CODE = errors.PtracCode.SEMANTICS_LINE

    j_line = _fields.Field(event.J_0 | event.J_1 | event.J_2 | event.J_3 | event.J_4 | event.J_5 | event.J_6 | event.J_7, 'Event j-line')
    p_line = _fields.Field(event.P_0 | event.P_1, 'Event p-line')

    def from_mcnp(source: str):
        """
        Generates `Event` from PTRAC.

        Parameters:
            source: PTRAC for `Event`.

        Returns:
            `Event`.

        Raises:
            PtracError: SYNTAX_LINE.
        """

        tokens = Event._REGEX.match(source)

        if not tokens:
            raise errors.PtracError(errors.PtracCode.SYNTAX_LINE, source)

        for variation in [event.J_0, event.J_1, event.J_2, event.J_3, event.J_4, event.J_5, event.J_6, event.J_7]:
            try:
                j_line = variation.from_mcnp(tokens[1])
                break
            except errors.PtracError:
                pass

        for variation in [event.P_0, event.P_1]:
            try:
                p_line = variation.from_mcnp(tokens[54])
                break
            except errors.PtracError:
                pass

        return Event(
            j_line,
            p_line,
        )

    def to_mcnp(self):
        """
        Generates PTRAC from `Event`.

        Returns:
            PTRAC for `Event`.
        """

        return f'{self.j_line}\n{self.p_line}\n'
