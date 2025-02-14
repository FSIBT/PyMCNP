import re
import typing

from . import _line
from . import keyword_type
from ...utils import types
from ...utils import _parser


class HistoryLine_J_7(_line.HistoryLine_):
    """
    Represents PTRAC history block j lines form #4b.

    Attributes:
        next_type: Next event type.
        node: Number of node in track from source.
        nsx_nsf_nter: NSR or NSF or NTER.
        ntyn_mtp_angle_branch: NTYN/MTP or 13 or 15.
        ipt: Particle type.
        ncl: Problem numbers of the cells.
        mat: Material numbers of the cells.
        ncp: Count of collisions per track.
    """

    _REGEX = re.compile(r'\A(.{4})(.{4})(.{4})(.{4})(.{4})(.{4})(.{4})(.{4})\Z')

    def __init__(
        self,
        next_type: keyword_type.HistoryKeyword_Type,
        node: types.Integer,
        nsx_nsf_nter: types.Integer,
        ntyn_mtp_angle_branch: types.Integer,
        ipt: types.Integer,
        ncl: types.Integer,
        mat: types.Integer,
        ncp: types.Integer,
    ):
        """
        Initializes ``HistoryLine_J_7``.

        Parameters:
            next_type: Next event type.
            node: Number of node in track from source.
            nsx_nsf_nter: NSR or NSF or NTER.
            ntyn_mtp_angle_branch: NTYN/MTP or 13 or 15.
            ipt: Particle type.
            ncl: Problem numbers of the cells.
            mat: Material numbers of the cells.
            ncp: Count of collisions per track.

        Raises:
            McnpError: INVALID_HEADER_CODE.
        """

        if next_type is None:
            raise Exception

        if node is None:
            raise Exception

        if nsx_nsf_nter is None:
            raise Exception

        if ntyn_mtp_angle_branch is None:
            raise Exception

        if ipt is None:
            raise Exception

        if ncl is None:
            raise Exception

        if mat is None:
            raise Exception

        if ncp is None:
            raise Exception

        self.next_type: typing.Final[keyword_type.HistoryKeyword_Type] = next_type
        self.node: typing.Final[types.Integer] = node
        self.nsx_nsf_nter: typing.Final[types.Integer] = nsx_nsf_nter
        self.ntyn_mtp_angle_branch: typing.Final[types.Integer] = ntyn_mtp_angle_branch
        self.ipt: typing.Final[types.Integer] = ipt
        self.ncl: typing.Final[types.Integer] = ncl
        self.mat: typing.Final[types.Integer] = mat
        self.ncp: typing.Final[types.Integer] = ncp

    def from_mcnp(source: str):
        """
        Generates ``HistoryLine_J_7`` from PTRAC.

        Parameters:
            source: PTRAC for ``HistoryLine_J_7``.

        Returns:
            ``HistoryLine_J_7``.

        Raises:
            McnpError: TOOFEW_HISTORY.
        """

        source = _parser.preprocess_ptrac(source)
        tokens = HistoryLine_J_7._REGEX.match(source)

        if not tokens:
            raise Exception

        next_type = keyword_type.HistoryKeyword_Type.from_mcnp(tokens[1])
        node = types.Integer.from_mcnp(tokens[2])
        nsx_nsf_nter = types.Integer.from_mcnp(tokens[3])
        ntyn_mtp_angle_branch = types.Integer.from_mcnp(tokens[4])
        ipt = types.Integer.from_mcnp(tokens[5])
        ncl = types.Integer.from_mcnp(tokens[6])
        mat = types.Integer.from_mcnp(tokens[7])
        ncp = types.Integer.from_mcnp(tokens[8])

        return HistoryLine_J_7(
            next_type, node, nsx_nsf_nter, ntyn_mtp_angle_branch, ipt, ncl, mat, ncp
        )
