import re
import typing

from . import line_
from .EventType import EventType
from ...utils import types
from ...utils import errors
from ...utils import _parser


class J_3(line_.HistoryLine_):
    """
    Represents PTRAC history block j lines form #2b.

    Attributes:
        next_type: Next event type.
        node: Number of node in track from source.
        nsx_nsf_nter: NSR or NSF or NTER.
        ntyn_mtp_angle_branch: NTYN/MTP or 13 or 15.
        ipt: Particle type.
        ncl: Problem numbers of the cells.
        mat: Material numbers of the cells.
    """

    _REGEX = re.compile(r'\A(.{4})(.{4})(.{4})(.{4})(.{4})(.{4})(.{4})\Z')

    def __init__(
        self,
        next_type: EventType,
        node: types.Integer,
        nsx_nsf_nter: types.Integer,
        ntyn_mtp_angle_branch: types.Integer,
        ipt: types.Integer,
        ncl: types.Integer,
        mat: types.Integer,
    ):
        """
        Initializes ``J_3``.

        Parameters:
            next_type: Next event type.
            node: Number of node in track from source.
            nsx_nsf_nter: NSR or NSF or NTER.
            ntyn_mtp_angle_branch: NTYN/MTP or 13 or 15.
            ipt: Particle type.
            ncl: Problem numbers of the cells.
            mat: Material numbers of the cells.

        Raises:
            InpError: SEMANTICS_LINE_VALUE.
        """

        if next_type is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE_VALUE, next_type)

        if node is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE_VALUE, node)

        if nsx_nsf_nter is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE_VALUE, nsx_nsf_nter)

        if ntyn_mtp_angle_branch is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE_VALUE, ntyn_mtp_angle_branch)

        if ipt is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE_VALUE, ipt)

        if ncl is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE_VALUE, ncl)

        if mat is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE_VALUE, mat)

        self.next_type: typing.Final[EventType] = next_type
        self.node: typing.Final[types.Integer] = node
        self.nsx_nsf_nter: typing.Final[types.Integer] = nsx_nsf_nter
        self.ntyn_mtp_angle_branch: typing.Final[types.Integer] = ntyn_mtp_angle_branch
        self.ipt: typing.Final[types.Integer] = ipt
        self.ncl: typing.Final[types.Integer] = ncl
        self.mat: typing.Final[types.Integer] = mat

    def from_mcnp(source: str):
        """
        Generates ``J_3`` from PTRAC.

        Parameters:
            source: PTRAC for ``J_3``.

        Returns:
            ``J_3``.

        Raises:
            PtracError: SYNTAX_HISTORY_LINE.
        """

        source = _parser.preprocess_ptrac(source)
        tokens = J_3._REGEX.match(source)

        if not tokens:
            raise errors.PtracError(errors.PtracCode.SYNTAX_HISTORY_LINE, source)

        next_type = EventType.from_mcnp(tokens[1])
        node = types.Integer.from_mcnp(tokens[2])
        nsx_nsf_nter = types.Integer.from_mcnp(tokens[3])
        ntyn_mtp_angle_branch = types.Integer.from_mcnp(tokens[4])
        ipt = types.Integer.from_mcnp(tokens[5])
        ncl = types.Integer.from_mcnp(tokens[6])
        mat = types.Integer.from_mcnp(tokens[7])

        return J_3(
            next_type,
            node,
            nsx_nsf_nter,
            ntyn_mtp_angle_branch,
            ipt,
            ncl,
            mat,
        )
