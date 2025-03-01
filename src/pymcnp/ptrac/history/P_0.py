import re
import typing

from . import line_
from ...utils import types
from ...utils import errors
from ...utils import _parser


class P_0(line_.HistoryLine_):
    """
    Represents PTRAC history block p lines form #1.

    Attributes:
        x: X coordinate of the particle position.
        y: Y coordinate of the particle position.
        z: Z coordinate of the particle position.
    """

    _REGEX = re.compile(r'\A(.{4})(.{4})(.{4})\Z')

    def __init__(
        self,
        x: types.Integer,
        y: types.Integer,
        z: types.Integer,
    ):
        """
        Initializes ``P_0``.

        Parameters:
            x: X coordinate of the particle position.
            y: Y coordinate of the particle position.
            z: Z coordinate of the particle position.

        Raises:
            InpError: SEMANTICS_LINE_VALUE.
        """

        if x is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE_VALUE, x)

        if y is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE_VALUE, y)

        if z is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE_VALUE, z)

        self.x: typing.Final[types.Integer] = x
        self.y: typing.Final[types.Integer] = y
        self.z: typing.Final[types.Integer] = z

    def from_mcnp(source: str):
        """
        Generates ``P_0`` from PTRAC.

        Parameters:
            source: PTRAC for ``P_0``.

        Returns:
            ``P_0``.

        Raises:
            PtracError: SYNTAX_HISTORY_LINE.
        """

        source = _parser.preprocess_ptrac(source)
        tokens = P_0._REGEX.match(source)

        if not tokens:
            raise errors.PtracError(errors.PtracCode.SYNTAX_HISTORY_LINE, source)

        x = types.Integer.from_mcnp(tokens[1])
        y = types.Integer.from_mcnp(tokens[2])
        z = types.Integer.from_mcnp(tokens[3])

        return P_0(
            x,
            y,
            z,
        )
