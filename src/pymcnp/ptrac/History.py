from __future__ import annotations
import re
import typing

from . import history
from .Header import Header
from ..utils import types
from ..utils import errors
from ..utils import _parser
from ..utils import _object


class History(_object.McnpElement_):
    """
    Represents PTRAC history blocks.

    Attributes:
        i_line: PTRAC history i-line.
        events: PTRAC history events.
    """

    _REGEX = re.compile(
        r'\s(.{10})(.{10})(.{10})(.{13})\n' r'(.+\n)*?((?:       9000).+?)\n(.+?)\n' r'((.+\n)*)'
    )

    def __init__(
        self,
        i_line: types.Tuple[types.Integer, history.EventType, types.Real],
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
    def from_mcnp(source: str, header: Header) -> tuple[History, str]:
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

        source = _parser.preprocess_ptrac(source)
        tokens = History._REGEX.match(source)

        if not tokens:
            raise errors.PtracError(errors.PtracCode.SYNTAX_BLOCK, source)

        i_line = types.Tuple(
            [
                types.Integer(tokens[1]),
                history.EventType(tokens[2].strip()),
                types.Integer(tokens[3]),
                types.Real(tokens[4]),
            ]
        )

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
                        na = header.n_line
                        nb = header.n_line
                    elif next_type == history.EventType.COLLISION:
                        na = header.n_line
                        nb = header.n_line
                    elif next_type == history.EventType.TERMINATION:
                        na = header.n_line
                        nb = header.n_line
                    else:
                        na = header.n_line
                        nb = header.n_line

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

        events = events(i_line[2], [tokens[5], tokens[6]])

        return (
            History(i_line, events),
            tokens[8],
        )
