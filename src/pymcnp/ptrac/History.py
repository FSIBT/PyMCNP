import re

from . import history
from .. import types
from .. import errors
from .. import _symbol
from .. import _fields


class History(_fields.Fields, _symbol.Nonterminal):
    """
    Represents PTRAC history blocks.

    Attributes:
        i_line: PTRAC history i-line.
        events: PTRAC history events.
    """

    _REGEX = re.compile(r'\A(.+)\n' rf'((?:{history.Event._REGEX.pattern[2:-2]})+)\Z', re.IGNORECASE)

    _ERROR = errors.PtracError
    _CODE = errors.PtracCode.SEMANTICS_BLOCK

    i_line = _fields.Field(history.I, 'PTRAC history i-line')
    events = _fields.Field(types.Tuple(history.Event), 'PTRAC history events', many=True)

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `History` from PTRAC.

        Parameters:
            source: PTRAC for `History`.

        Returns:
            `History`.

        Raises:
            PtracError: SYNTAX_BLOCK.
        """

        tokens = History._REGEX.match(source)

        if not tokens:
            raise errors.PtracError(errors.PtracCode.SYNTAX_BLOCK, source)

        i_line = history.I.from_mcnp(tokens[1])
        events = types.Generator(history.Event).from_mcnp(tokens[2])

        return History(i_line, events)

    def to_mcnp(self):
        """
        Generates PTRAC from `History`.

        Returns:
            PTRAC for `History`.
        """

        return f'{self.i_line}\n{"".join(map(str, self.events))}'
