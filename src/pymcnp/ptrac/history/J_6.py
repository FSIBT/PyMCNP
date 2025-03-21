import re
import typing

from . import line_
from .EventType import EventType
from ...utils import types
from ...utils import errors
from ...utils import _parser


class J_6(line_.HistoryLine_):
    """
    Represents PTRAC history block j lines form #4a.

    Attributes:
        next_type: Next event type.
        node: Number of node in track from source.
        nsr: Source type.
        ipt: Particle type.
        ncl: Problem numbers of the cells.
        mat: Material numbers of the cells.
        ncp: Count of collisions per track.
    """

    _REGEX = re.compile(r'\A(.{4})(.{4})(.{4})(.{4})(.{4})(.{4})\Z')

    def __init__(
        self,
        next_type: EventType,
        node: types.Integer,
        nsr: types.Integer,
        ipt: types.Integer,
        ncl: types.Integer,
        mat: types.Integer,
        ncp: types.Integer,
    ):
        """
        Initializes ``J_6``.

        Parameters:
            next_type: Next event type.
            node: Number of node in track from source.
            nsr: Source type.
            ipt: Particle type.
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

        if ipt is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE_VALUE, ipt)

        if ncl is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE_VALUE, ncl)

        if mat is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE_VALUE, mat)

        if ncp is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE_VALUE, ncp)

        self.next_type: typing.Final[EventType] = next_type
        self.node: typing.Final[types.Integer] = node
        self.nsr: typing.Final[types.Integer] = nsr
        self.ipt: typing.Final[types.Integer] = ipt
        self.ncl: typing.Final[types.Integer] = ncl
        self.mat: typing.Final[types.Integer] = mat
        self.ncp: typing.Final[types.Integer] = ncp

    def from_mcnp(source: str):
        """
        Generates ``J_6`` from PTRAC.

        Parameters:
            source: PTRAC for ``J_6``.

        Returns:
            ``J_6``.

        Raises:
            PtracError: SYNTAX_HISTORY_LINE.
        """

        source = _parser.preprocess_ptrac(source)
        tokens = J_6._REGEX.match(source)

        if not tokens:
            raise errors.PtracError(errors.PtracCode.SYNTAX_HISTORY_LINE, source)

        next_type = EventType.from_mcnp(tokens[1])
        node = types.Integer.from_mcnp(tokens[2])
        nsr = types.Integer.from_mcnp(tokens[3])
        ipt = types.Integer.from_mcnp(tokens[4])
        ncl = types.Integer.from_mcnp(tokens[5])
        mat = types.Integer.from_mcnp(tokens[6])
        ncp = types.Integer.from_mcnp(tokens[7])

        return J_6(
            next_type,
            node,
            nsr,
            ipt,
            ncl,
            mat,
            ncp,
        )
