import re
import typing

from . import j
from . import _line
from .... import types
from .... import errors


class J_1(_line.EventLine):
    """
    Represents PTRAC history block j lines form #1b.

    Attributes:
        next_type: Next event type.
        node: Number of node in track from source.
        nsx_nsf_nter: NSR or NSF or NTER.
        ntyn_mtp_angle_branch: NTYN/MTP or 13 or 15.
        ncl: Problem numbers of the cells.
        mat: Material numbers of the cells.
    """

    _REGEX = re.compile(r'\A\s(.{10})(.{10})(.{10})(.{10})(.{10})(.{10})\Z', re.IGNORECASE)

    def __init__(
        self,
        next_type: j.EventType,
        node: types.Integer,
        nsx_nsf_nter: types.Real,
        ntyn_mtp_angle_branch: types.Integer,
        ncl: types.Integer,
        mat: types.Integer,
    ):
        """
        Initializes `J_1`.

        Parameters:
            next_type: Next event type.
            node: Number of node in track from source.
            nsx_nsf_nter: NSR or NSF or NTER.
            ntyn_mtp_angle_branch: NTYN/MTP or 13 or 15.
            ncl: Problem numbers of the cells.
            mat: Material numbers of the cells.

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

        if ncl is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, ncl)

        if mat is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, mat)

        self.next_type: typing.Final[j.EventType] = next_type
        self.node: typing.Final[types.Integer] = node
        self.nsx_nsf_nter: typing.Final[types.Real] = nsx_nsf_nter
        self.ntyn_mtp_angle_branch: typing.Final[types.Integer] = ntyn_mtp_angle_branch
        self.ncl: typing.Final[types.Integer] = ncl
        self.mat: typing.Final[types.Integer] = mat

    def from_mcnp(source: str):
        """
        Generates `J_1` from PTRAC.

        Parameters:
            source: PTRAC for `J_1`.

        Returns:
            `J_1`.

        Raises:
            PtracError: SYNTAX_LINE.
        """

        tokens = J_1._REGEX.match(source)

        if not tokens:
            raise errors.PtracError(errors.PtracCode.SYNTAX_LINE, source)

        next_type = j.EventType.from_mcnp(tokens[1].strip())
        node = types.Integer.from_mcnp(tokens[2])
        nsx_nsf_nter = types.Real.from_mcnp(tokens[3])
        ntyn_mtp_angle_branch = types.Integer.from_mcnp(tokens[4])
        ncl = types.Integer.from_mcnp(tokens[5])
        mat = types.Integer.from_mcnp(tokens[6])

        return J_1(
            next_type,
            node,
            nsx_nsf_nter,
            ntyn_mtp_angle_branch,
            ncl,
            mat,
        )

    def to_mcnp(self):
        """
        Generates PTRAC from `J_1`.

        Returns:
            PTRAC for `J_1`.
        """

        return f' {str(self.next_type):>10}{str(self.node):>10}{str(self.nsx_nsf_nter):>10}{str(self.ntyn_mtp_angle_branch):>10}{str(self.ncl):>10}{str(self.mat):>10}'
