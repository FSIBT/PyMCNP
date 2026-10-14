import re

from . import _line
from ... import types
from ... import errors
from ... import _fields


class V(_fields.Fields, _line.HeaderLine):
    """
    Represents PTRAC header block l lines.

    Attributes:
        variables: Variable for lines/events.
    """

    _REGEX = re.compile(r'\A((?:.{5,121}?\n)+)\Z', re.IGNORECASE)

    _ERROR = errors.PtracError
    _CODE = errors.PtracCode.SEMANTICS_LINE

    variables = _fields.Field(types.Tuple(types.Real), 'Variable for lines/events', many=True)

    def from_mcnp(source: str):
        """
        Generates `V` from PTRAC.

        Parameters:
            source: PTRAC for `V`.

        Returns:
            `V`.

        Raises:
            PtracError: SYNTAX_HISTORY_LINE.
        """

        tokens = V._REGEX.match(source)

        if not tokens:
            raise errors.PtracError(errors.PtracCode.SYNTAX_LINE, source)

        variables = types.Tuple(types.Real).from_mcnp(tokens[1])

        return V(
            variables,
        )

    def to_mcnp(self):
        """
        Generates PTRAC from `V`.

        Returns:
            PTRAC for `V`.
        """

        v_line = ' '

        for i, v in enumerate(self.variables):
            v_line += f' {v:4.0a}'
            if (i + 1) % 10 == 0 and i != 0:
                v_line += '\n '

        v_line = v_line[:-1]

        return v_line
