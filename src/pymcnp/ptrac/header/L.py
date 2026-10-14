import re

from . import _line
from ... import types
from ... import errors
from ... import _fields


class L(_fields.Fields, _line.HeaderLine):
    """
    Represents PTRAC header block l lines.

    Attributes:
        variables: Variable for lines/events.
    """

    _REGEX = re.compile(r'\A((?:\s(?:.{4})+\n)+)\Z', re.IGNORECASE)

    _ERROR = errors.PtracError
    _CODE = errors.PtracCode.SEMANTICS_LINE

    variables = _fields.Field(types.Tuple(types.Integer), 'Variable for lines/events', many=True)

    def from_mcnp(source: str):
        """
        Generates `L` from PTRAC.

        Parameters:
            source: PTRAC for `L`.

        Returns:
            `L`.

        Raises:
            PtracError: SYNTAX_LINE.
        """

        tokens = L._REGEX.match(source)

        if not tokens:
            raise errors.PtracError(errors.PtracCode.SYNTAX_LINE, source)

        variables = types.Tuple(types.Integer).from_mcnp(tokens[1])

        return L(
            variables,
        )

    def to_mcnp(self):
        """
        Generates PTRAC from `L`.

        Returns:
            PTRAC for `L`.
        """

        l_line = ' '

        for i, l in enumerate(self.variables):
            l_line += f'{str(l.value):>4}'

            if (i + 1) % 30 == 0 and i != 0:
                l_line += '\n '

        return l_line + '\n'
