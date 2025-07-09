import re
import typing

from . import _line
from ...utils import types
from ...utils import errors


class L(_line.HeaderLine):
    """
    Represents PTRAC header block l lines.

    Attributes:
        variables: Variable for lines/events.
    """

    _REGEX = re.compile(r'\A((?:\s(?:.{4})+\n)+)\Z')

    def __init__(self, variables: types.Tuple[types.Integer]):
        """
        Initializes ``L``.

        Parameters:
            variables: Variable for lines/events.

        Raises:
            PtracError: SEMANTICS_LINE.
        """

        if variables is None or None in variables:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, variables)

        self.variables: typing.Final[types.String] = variables

    def from_mcnp(source: str):
        """
        Generates ``L`` from PTRAC.

        Parameters:
            source: PTRAC for ``L``.

        Returns:
            ``L``.

        Raises:
            PtracError: SYNTAX_LINE.
        """

        tokens = L._REGEX.match(source)

        if not tokens:
            raise errors.PtracError(errors.PtracCode.SYNTAX_LINE, source)

        variables = types.Tuple.from_mcnp(tokens[1], types.Integer)

        return L(
            variables,
        )

    def to_mcnp(self):
        """
        Generates PTRAC from ``L``.

        Returns:
            PTRAC for ``L``.
        """

        l_line = ' '

        for i, l in enumerate(self.variables):
            l_line += f'{str(l.value):>4}'

            if (i + 1) % 30 == 0 and i != 0:
                l_line += '\n '

        return l_line + '\n'
