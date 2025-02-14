import re
import typing

from . import _line
from ...utils import types
from ...utils import _parser


class HistoryLine_P_0(_line.HistoryLine_):
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
        Initializes ``HistoryLine_P_0``.

        Parameters:
            x: X coordinate of the particle position.
            y: Y coordinate of the particle position.
            z: Z coordinate of the particle position.

        Raises:
            McnpError: INVALID_HEADER_CODE.
        """

        if x is None:
            raise Exception

        if y is None:
            raise Exception

        if z is None:
            raise Exception

        self.x: typing.Final[types.Integer] = x
        self.y: typing.Final[types.Integer] = y
        self.z: typing.Final[types.Integer] = z

    def from_mcnp(source: str):
        """
        Generates ``HistoryLine_P_0`` from PTRAC.

        Parameters:
            source: PTRAC for ``HistoryLine_P_0``.

        Returns:
            ``HistoryLine_P_0``.

        Raises:
            McnpError: TOOFEW_HISTORY.
        """

        source = _parser.preprocess_ptrac(source)
        tokens = HistoryLine_P_0._REGEX.match(source)

        if not tokens:
            raise Exception

        x = types.Integer.from_mcnp(tokens[1])
        y = types.Integer.from_mcnp(tokens[2])
        z = types.Integer.from_mcnp(tokens[3])

        return HistoryLine_P_0(
            x,
            y,
            z,
        )
