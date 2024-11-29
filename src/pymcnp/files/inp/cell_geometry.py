"""
Contains classes representing INP cell card geometry formulas.
"""

import re

from . import _card
from ..utils import errors
from ..utils import _parser


class CellGeometry(_card.CardEntry):
    """
    Represents INP cell card geometry formulas.

    ``CellGeometry`` implements ``_card.CardMnemonic``.

    Attributes:
        string: Geometry formula string representation.
    """

    _OPERATIONS_ORDER = {'#': 0, ' ': 1, ':': 2}

    def __init__(self, formula: str):
        """
        Initializes ``CellGeometry``.

        Parameters:
            formula: INP for cell geometry.

        Raises:
            McnpError: EXPECTED_TOKEN.
            McnpError: INVALID_CELL_GEOMETRY.
        """

        if not formula:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_GEOMETRY, formula)

        # Running Shunting-Yard Algorithm
        ops_stack = _parser.Parser(
            [],
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, formula),
        )
        out_stack = _parser.Parser(
            [],
            errors.McnpError(errors.McnpCode.EXPECTED_TOKEN, formula),
        )
        inp_stack = re.findall(
            r'#|:| : |[()]| [()]|[()] | [()] | |[+-]?\d+',
            formula,
        )

        if ''.join(inp_stack) != formula:
            raise errors.McnpError(errors.McnpCode.INVALID_CELL_GEOMETRY, formula)

        for token in inp_stack:
            if re.match(r'[+-]?\d+', token):
                # Processing Surface Number

                entry = int(token)
                if entry is None or not (entry != 0 and -99_999_999 <= entry <= 99_999_999):
                    raise errors.McnpError(errors.McnpCode.INVALID_CELL_GEOMETRY, formula)

                out_stack.pushr(token)

            elif re.match(r'#', token):
                # Processing Unary Operator
                ops_stack.pushr(token)

            elif re.match(r'([(]| [(]|[(] | [(] )', token):
                # Processing Left Parenthesis
                ops_stack.pushr('(')

            elif re.match(r'([)]| [)]|[)] | [)] )', token):
                # Processing Right Parenthesis
                while ops_stack.peekr() != '(':
                    out_stack.pushr(ops_stack.popr())

                ops_stack.popr()

            elif re.match(r':| : | |: | :', token):
                # Processing Binary Operator
                token = token.strip() if token != ' ' else token

                while (
                    ops_stack
                    and ops_stack.peekr() not in {'(', ')'}
                    and self._OPERATIONS_ORDER[ops_stack.peekr()] >= self._OPERATIONS_ORDER[token]
                ):
                    out_stack.pushr(ops_stack.popr())

                ops_stack.pushr(token)

            else:
                # Unrecognized Character
                assert False

        while ops_stack:
            out_stack.pushr(ops_stack.popr())

        self.formula = formula

    @staticmethod
    def from_mcnp(source: str) -> str:
        """
        Generates ``CellGeometry`` objects from INP.

        ``from_mcnp`` translates from INP to PyMCNP; it parses INP.

        Parameters:
            source: INP for cell card geometry.

        Returns:
            ``CellGeometry`` object.
        """

        return CellGeometry(source)

    def to_mcnp(self) -> str:
        """
        Generates INP from ``CellGeometry``.

        ``to_mcnp`` translates from PyMCNP to INP.

        Returns:
            INP for ``CellGeometry``.
        """

        return self.formula
