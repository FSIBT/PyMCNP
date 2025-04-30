import re
import typing

from . import history
from .Header import Header
from ..utils import types
from ..utils import errors
from ..utils import _object


class History(_object.McnpElement_):
    """
    Represents PTRAC history blocks.

    Attributes:
        i_line: PTRAC history i-line.
        events: PTRAC history events.
    """

    _REGEX = re.compile(
        r'\s(.+)\n'
        rf'((?:\s(?:(?:{history.J_0._REGEX.pattern})|(?:{history.J_1._REGEX.pattern})|(?:{history.J_2._REGEX.pattern})|(?:{history.J_3._REGEX.pattern})|(?:{history.J_4._REGEX.pattern})|(?:{history.J_5._REGEX.pattern})|(?:{history.J_6._REGEX.pattern})|(?:{history.J_7._REGEX.pattern}))\n\s(?:(?:{history.P_0._REGEX.pattern})|(?:{history.P_1._REGEX.pattern}))\n)+)'
    )

    def __init__(
        self,
        i_line: history.I,
        events: typing.Generator,
    ):
        """
        Initializes ``History``.

        Parameters:
            i_line: PTRAC history i-line.
            events: PTRAC history events.

        Raises:
            PtracError: SEMANTICS_BLOCK.
        """

        if i_line is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_BLOCK, i_line)

        if events is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_BLOCK, events)

        self.i_line: typing.Final[types.Tuple[types.Integer, history.EventType, types.Real]] = (
            i_line
        )
        self.events: typing.Final[typing.Generator] = events

    @staticmethod
    def from_mcnp(source: str, header: Header):
        """
        Generates ``History`` from PTRAC.

        Parameters:
            source: PTRAC for ``History``.
            header: PTRAC header.

        Returns:
            ``History``.

        Raises:
            PtracError: SYNTAX_BLOCK.
        """

        tokens = History._REGEX.match(source)

        if not tokens:
            raise errors.PtracError(errors.PtracCode.SYNTAX_BLOCK, source)

        i_line = history.I.from_mcnp(tokens[1])

        def events(next_type, lines):
            while next_type != history.EventType.FLAG:
                if next_type == history.EventType.SOURCE:
                    if (header.n_line, header.n_line) == (5, 3):
                        j_line = history.J_0.from_mcnp(lines.pop(0))
                        p_line = history.P_0.from_mcnp(lines.pop(0))
                    elif (header.n_line, header.n_line) == (6, 3):
                        j_line = history.J_2.from_mcnp(lines.pop(0))
                        p_line = history.P_0.from_mcnp(lines.pop(0))
                    elif (header.n_line, header.n_line) == (6, 9):
                        j_line = history.J_4.from_mcnp(lines.pop(0))
                        p_line = history.P_1.from_mcnp(lines.pop(0))
                    elif (header.n_line, header.n_line) == (7, 9):
                        j_line = history.J_6.from_mcnp(lines.pop(0))
                        p_line = history.P_1.from_mcnp(lines.pop(0))
                    else:
                        assert False
                else:
                    if next_type == history.EventType.SURFACE:
                        na = header.n_line[5]
                        nb = header.n_line[6]
                    elif next_type == history.EventType.COLLISION:
                        na = header.n_line[7]
                        nb = header.n_line[8]
                    elif next_type == history.EventType.TERMINAL:
                        na = header.n_line[9]
                        nb = header.n_line[10]
                    else:
                        na = header.n_line[3]
                        nb = header.n_line[4]

                    if (na, nb) == (5, 3):
                        j_line = history.J_0.from_mcnp(lines.pop(0))
                        p_line = history.P_0.from_mcnp(lines.pop(0))
                    elif (na, nb) == (6, 3):
                        j_line = history.J_2.from_mcnp(lines.pop(0))
                        p_line = history.P_0.from_mcnp(lines.pop(0))
                    elif (na, nb) == (6, 9):
                        j_line = history.J_4.from_mcnp(lines.pop(0))
                        p_line = history.P_1.from_mcnp(lines.pop(0))
                    elif (na, nb) == (7, 9):
                        j_line = history.J_6.from_mcnp(lines.pop(0))
                        p_line = history.P_1.from_mcnp(lines.pop(0))
                    else:
                        assert False

                yield (j_line, p_line)
                next_type = j_line.next_type

        events = events(i_line.event_type, tokens[2][1:].split('\n '))

        return History(i_line, events)

    def to_mcnp(self):
        """
        Generates PTRAC from ``History``.

        Returns:
            PTRAC for ``History``.
        """

        events = ''
        for j_line, p_line in self.events:
            events += ' '
            events += j_line.to_mcnp()
            events += '\n  '
            events += p_line.to_mcnp()

        return f' {self.i_line.to_mcnp()}\n{events}'
