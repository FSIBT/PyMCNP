import re
import typing

from . import history
from .. import types
from .. import errors
from ..utils import _object


class History(_object.McnpNonterminal):
    """
    Represents PTRAC history blocks.

    Attributes:
        i_line: PTRAC history i-line.
        events: PTRAC history events.
    """

    _REGEX = re.compile(r'\A(.+)\n' rf'((?:{history.Event._REGEX.pattern[2:-2]})+)\Z')

    def __init__(
        self,
        i_line: history.I,
        events: types.Tuple[history.Event],
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

        if events is None or None in events:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_BLOCK, events)

        self.i_line: typing.Final[history.I] = i_line
        self.events: typing.Final[types.Tuple[history.Event]] = events

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``History`` from PTRAC.

        Parameters:
            source: PTRAC for ``History``.

        Returns:
            ``History``.

        Raises:
            PtracError: SYNTAX_BLOCK.
        """

        tokens = History._REGEX.match(source)

        if not tokens:
            raise errors.PtracError(errors.PtracCode.SYNTAX_BLOCK, source)

        i_line = history.I.from_mcnp(tokens[1])

        events = []
        for match in re.finditer(history.Event._REGEX.pattern[2:-2], tokens[2]):
            event = history.Event.from_mcnp(match[0])
            events.append(event)

        events = types.Tuple(events)

        return History(i_line, events)

    def to_mcnp(self):
        """
        Generates PTRAC from ``History``.

        Returns:
            PTRAC for ``History``.
        """

        return f'{self.i_line}\n{''.join(map(str, self.events))}'
