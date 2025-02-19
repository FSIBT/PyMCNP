import re
import typing

from . import _line
from . import keyword_type
from ...utils import types
from ...utils import errors
from ...utils import _parser


class HistoryLine_J_4(_line.HistoryLine_):
    """
    Represents PTRAC history block j lines form #3a.

    Attributes:
        next_type: Next event type.
        node: Number of node in track from source.
        nsr: Source type.
        ncl: Problem numbers of the cells.
        mat: Material numbers of the cells.
        ncp: Count of collisions per track.
    """

    _REGEX = re.compile(r'\A(.{4})(.{4})(.{4})(.{4})(.{4})(.{4})\Z')

    def __init__(
        self,
        next_type: keyword_type.HistoryKeyword_Type,
        node: types.Integer,
        nsr: types.Integer,
        ncl: types.Integer,
        mat: types.Integer,
        ncp: types.Integer,
    ):
        """
        Initializes ``HistoryLine_J_4``.

        Parameters:
            next_type: Next event type.
            node: Number of node in track from source.
            nsr: Source type.
            ncl: Problem numbers of the cells.
            mat: Material numbers of the cells.
            ncp: Count of collisions per track.

        Raises:
            InpError: SEMANTICS_LINE_VALUE.
        """

        if next_type is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE_VALUE, next_type)

        if node is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE_VALUE, node)

        if nsr is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE_VALUE, nsr)

        if ncl is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE_VALUE, ncl)

        if mat is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE_VALUE, mat)

        if ncp is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE_VALUE, ncp)

        self.next_type: typing.Final[keyword_type.HistoryKeyword_Type] = next_type
        self.node: typing.Final[types.Integer] = node
        self.nsr: typing.Final[types.Integer] = nsr
        self.ncl: typing.Final[types.Integer] = ncl
        self.mat: typing.Final[types.Integer] = mat
        self.ncp: typing.Final[types.Integer] = ncp

    def from_mcnp(source: str):
        """
        Generates ``HistoryLine_J_4`` from PTRAC.

        Parameters:
            source: PTRAC for ``HistoryLine_J_4``.

        Returns:
            ``HistoryLine_J_4``.

        Raises:
            PtracError: SYNTAX_HISTORY_LINE.
        """

        source = _parser.preprocess_ptrac(source)
        tokens = HistoryLine_J_4._REGEX.match(source)

        if not tokens:
            raise errors.PtracError(errors.PtracCode.SYNTAX_HISTORY_LINE, source)

        next_type = keyword_type.HistoryKeyword_Type.from_mcnp(tokens[1])
        node = types.Integer.from_mcnp(tokens[2])
        nsr = types.Integer.from_mcnp(tokens[3])
        ncl = types.Integer.from_mcnp(tokens[4])
        mat = types.Integer.from_mcnp(tokens[5])
        ncp = types.Integer.from_mcnp(tokens[6])

        return HistoryLine_J_4(
            next_type,
            node,
            nsr,
            ncl,
            mat,
            ncp,
        )
