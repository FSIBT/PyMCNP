import re
import typing

from .. import Header

from . import event
from . import _block
from ...utils import errors


class Event(_block.HistoryBlock):
    """
    Represents PTRAC history block events.

    Attributes:
        j_line: Event j-line.
        p_line: Event p-line.
    """

    _REGEX = re.compile(
        rf'\A((?:{event.J_0._REGEX.pattern[2:-2]})|(?:{event.J_1._REGEX.pattern[2:-2]})|(?:{event.J_2._REGEX.pattern[2:-2]})|(?:{event.J_3._REGEX.pattern[2:-2]})|(?:{event.J_4._REGEX.pattern[2:-2]})|(?:{event.J_5._REGEX.pattern[2:-2]})|(?:{event.J_6._REGEX.pattern[2:-2]})|(?:{event.J_7._REGEX.pattern[2:-2]}))\n((?:{event.P_0._REGEX.pattern[2:-2]})|(?:{event.P_1._REGEX.pattern[2:-2]}))\n\Z'
    )

    def __init__(
        self,
        j_line: typing.Union[event.J_0, event.J_1, event.J_2, event.J_3, event.J_4, event.J_5, event.J_6, event.J_7],
        p_line: typing.Union[event.P_0, event.P_1],
    ):
        """
        Initializes ``Event``.

        Parameters:
            j_line: Event j-line.
            p_line: Event p-line.

        Raises:
            PtracError: SEMANTICS_LINE.
        """

        if j_line is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, j_line)

        if p_line is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, p_line)

        self.j_line: typing.Final[typing.Union[event.J_0, event.J_1, event.J_2, event.J_3, event.J_4, event.J_5, event.J_6, event.J_7]] = j_line
        self.p_line: typing.Final[typing.Union[event.P_0, event.P_1]] = p_line

    def from_mcnp(source: str, next_type: event.j.EventType, header: Header):
        """
        Generates ``Event`` from PTRAC.

        Parameters:
            source: PTRAC for ``Event``.

        Returns:
            ``Event``.

        Raises:
            PtracError: SYNTAX_LINE.
        """

        tokens = Event._REGEX.match(source)

        if not tokens:
            raise errors.PtracError(errors.PtracCode.SYNTAX_LINE, source)

        # if next_type == event.j.EventType.SOURCE:
        #     if (header.n_line, header.n_line) == (5, 3):
        #         j_line = event.J_0.from_mcnp(tokens[1])
        #         p_line = event.P_0.from_mcnp(tokens[54])
        #     elif (header.n_line, header.n_line) == (6, 3):
        #         j_line = event.J_2.from_mcnp(tokens[1])
        #         p_line = event.P_0.from_mcnp(tokens[54])
        #     elif (header.n_line, header.n_line) == (6, 9):
        #         j_line = event.J_4.from_mcnp(tokens[1])
        #         p_line = event.P_1.from_mcnp(tokens[54])
        #     elif (header.n_line, header.n_line) == (7, 9):
        #         j_line = event.J_6.from_mcnp(tokens[1])
        #         p_line = event.P_1.from_mcnp(tokens[54])
        #     else:
        #         assert False
        # else:
        #     if next_type == event.j.EventType.SURFACE:
        #         na = header.n_line.n6
        #         nb = header.n_line.n7
        #     elif next_type == event.j.EventType.COLLISION:
        #         na = header.n_line.n8
        #         nb = header.n_line.n9
        #     elif next_type == event.j.EventType.TERMINAL:
        #         na = header.n_line.n10
        #         nb = header.n_line.n11
        #     else:
        #         na = header.n_line.n4
        #         nb = header.n_line.n5

        #     if (na, nb) == (5, 3):
        #         j_line = event.J_0.from_mcnp(tokens[1])
        #         p_line = event.P_0.from_mcnp(tokens[54])
        #     elif (na, nb) == (6, 3):
        #         j_line = event.J_2.from_mcnp(tokens[1])
        #         p_line = event.P_0.from_mcnp(tokens[54])
        #     elif (na, nb) == (6, 9):
        #         j_line = event.J_4.from_mcnp(tokens[1])
        #         p_line = event.P_1.from_mcnp(tokens[54])
        #     elif (na, nb) == (7, 9):
        #         j_line = event.J_6.from_mcnp(tokens[1])
        #         p_line = event.P_1.from_mcnp(tokens[54])
        #     else:
        #         assert False

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
        Generates PTRAC from ``Event``.

        Returns:
            PTRAC for ``Event``.
        """

        return f'{self.j_line}\n{self.p_line}\n'
