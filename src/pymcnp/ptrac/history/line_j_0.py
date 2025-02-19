import re
import typing

from . import _line
from . import keyword_type
from ...utils import types
from ...utils import errors
from ...utils import _parser


class HistoryLine_J_0(_line.HistoryLine_):
    """
    Represents PTRAC history block j lines form #1a.

    Attributes:
        next_type: Next J line event type.
        node: Number of node in track from source.
        nsr: Source type.
        ncl: Problem numbers of the cells.
        mat: Material numbers of the cells.
    """

    _REGEX = re.compile(r'\A(.{4})(.{4})(.{4})(.{4})(.{4})\Z')

    def __init__(
        self,
        next_type: keyword_type.HistoryKeyword_Type,
        pbl: types.Integer,
        nsr: types.Integer,
        ncl: types.Integer,
        mat: types.Integer,
    ):
        """
        Initializes ``HistoryLine_J_0``.

        Parameters:
            next_type: Next J line event type.
            pbl: Number of nodes in track from source.
            nsr: Source type.
            ncl: Problem numbers of the cells.
            mat: Material numbers of the cells.

        Raises:
            InpError: SEMANTICS_LINE_VALUE.
        """

        if next_type is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE_VALUE, next_type)

        if pbl is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE_VALUE, pbl)

        if nsr is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE_VALUE, nsr)

        if ncl is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE_VALUE, ncl)

        if mat is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE_VALUE, mat)

        self.next_type: typing.Final[keyword_type.HistoryKeyword_Type] = next_type
        self.pbl: typing.Final[types.Integer] = pbl
        self.nsr: typing.Final[types.Integer] = nsr
        self.ncl: typing.Final[types.Integer] = ncl
        self.mat: typing.Final[types.Integer] = mat

    def from_mcnp(source: str):
        """
        Generates ``HistoryLine_J_0`` from PTRAC.

        Parameters:
            source: PTRAC for ``HistoryLine_J_0``.

        Returns:
            ``HistoryLine_J_0``.

        Raises:
            PtracError: SYNTAX_HISTORY_LINE.
        """

        source = _parser.preprocess_ptrac(source)
        tokens = HistoryLine_J_0._REGEX.match(source)

        if not tokens:
            raise errors.PtracError(errors.PtracCode.SYNTAX_HISTORY_LINE, source)

        next_type = keyword_type.HistoryKeyword_Type.from_mcnp(tokens[1])
        pbl = types.Integer.from_mcnp(tokens[2])
        nsr = types.Integer.from_mcnp(tokens[3])
        ncl = types.Integer.from_mcnp(tokens[4])
        mat = types.Integer.from_mcnp(tokens[5])

        return HistoryLine_J_0(
            next_type,
            pbl,
            nsr,
            ncl,
            mat,
        )
