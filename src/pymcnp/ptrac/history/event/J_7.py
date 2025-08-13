import re
import typing

from . import j
from . import _line
from .... import types
from .... import errors


class J_7(_line.EventLine):
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

    _REGEX = re.compile(r'\A\s(.{10})(.{10})(.{10})(.{10})(.{10})(.{10})(.{10})(.{10})\Z', re.IGNORECASE)

    def __init__(
        self,
        next_type: j.EventType,
        node: types.Integer,
        nsx_nsf_nter: types.Integer,
        ntyn_mtp_angle_branch: types.Integer,
        ipt: types.Integer,
        ncl: types.Integer,
        mat: types.Integer,
        ncp: types.Integer,
    ):
        """
        Initializes `J_7`.

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
            PtracError: SEMANTICS_LINE.
        """

        if next_type is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, next_type)

        if node is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, node)

        if nsx_nsf_nter is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, nsx_nsf_nter)

        if ntyn_mtp_angle_branch is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, ntyn_mtp_angle_branch)

        if ipt is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, ipt)

        if ncl is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, ncl)

        if mat is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, mat)

        if ncp is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, ncp)

        self.next_type: typing.Final[j.EventType] = next_type
        self.node: typing.Final[types.Integer] = node
        self.nsx_nsf_nter: typing.Final[types.Integer] = nsx_nsf_nter
        self.ntyn_mtp_angle_branch: typing.Final[types.Integer] = ntyn_mtp_angle_branch
        self.ipt: typing.Final[types.Integer] = ipt
        self.ncl: typing.Final[types.Integer] = ncl
        self.mat: typing.Final[types.Integer] = mat
        self.ncp: typing.Final[types.Integer] = ncp

    def from_mcnp(source: str):
        """
        Generates `J_7` from PTRAC.

        Parameters:
            source: PTRAC for `J_7`.

        Returns:
            `J_7`.

        Raises:
            PtracError: SYNTAX_LINE.
        """

        tokens = J_7._REGEX.match(source)

        if not tokens:
            raise errors.PtracError(errors.PtracCode.SYNTAX_LINE, source)

        next_type = j.EventType.from_mcnp(tokens[1].strip())
        node = types.Integer.from_mcnp(tokens[2])
        nsx_nsf_nter = types.Integer.from_mcnp(tokens[3])
        ntyn_mtp_angle_branch = types.Integer.from_mcnp(tokens[4])
        ipt = types.Integer.from_mcnp(tokens[5])
        ncl = types.Integer.from_mcnp(tokens[6])
        mat = types.Integer.from_mcnp(tokens[7])
        ncp = types.Integer.from_mcnp(tokens[8])

        return J_7(next_type, node, nsx_nsf_nter, ntyn_mtp_angle_branch, ipt, ncl, mat, ncp)

    def to_mcnp(self):
        """
        Generates PTRAC from `J_7`.

        Returns:
            PTRAC for `J_7`.
        """

        return f' {str(self.next_type):>10}{str(self.node):>10}{str(self.nsx_nsf_nter):>10}{str(self.ntyn_mtp_angle_branch):>10}{str(self.ipt):>10}{str(self.ncl):>10}{str(self.mat):>10}{str(self.ncp):>10}'
