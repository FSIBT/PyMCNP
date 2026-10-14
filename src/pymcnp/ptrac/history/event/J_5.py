import re

from . import j
from . import _line
from .... import types
from .... import errors
from .... import _fields


class J_5(_fields.Fields, _line.EventLine):
    """
    Represents PTRAC history block j lines form #3b.

    Attributes:
        next_type: Next event type.
        node: Number of node in track from source.
        nsx_nsf_nter: NSR or NSF or NTER.
        ntyn_mtp_angle_branch: NTYN/MTP or 13 or 15.
        ncl: Problem numbers of the cells.
        mat: Material numbers of the cells.
        ncp: Count of collisions per track.
    """

    _REGEX = re.compile(r'\A\s(.{10})(.{10})(.{10})(.{10})(.{10})(.{10})(.{10})\Z', re.IGNORECASE)

    _ERROR = errors.PtracError
    _CODE = errors.PtracCode.SEMANTICS_LINE

    next_type = _fields.Field(j.EventType, 'Next event type')
    node = _fields.Field(types.Integer, 'Number of node in track from source')
    nsx_nsf_nter = _fields.Field(types.Integer, 'NSR or NSF or NTER')
    ntyn_mtp_angle_branch = _fields.Field(types.Integer, 'NTYN/MTP or 13 or 15')
    ncl = _fields.Field(types.Integer, 'Problem numbers of the cells')
    mat = _fields.Field(types.Integer, 'Material numbers of the cells')
    ncp = _fields.Field(types.Integer, 'Count of collisions per track')

    def from_mcnp(source: str):
        """
        Generates `J_5` from PTRAC.

        Parameters:
            source: PTRAC for `J_5`.

        Returns:
            `J_5`.

        Raises:
            PtracError: SYNTAX_LINE.
        """

        tokens = J_5._REGEX.match(source)

        if not tokens:
            raise errors.PtracError(errors.PtracCode.SYNTAX_LINE, source)

        next_type = j.EventType.from_mcnp(tokens[1].strip())
        node = types.Integer.from_mcnp(tokens[2])
        nsx_nsf_nter = types.Integer.from_mcnp(tokens[3])
        ntyn_mtp_angle_branch = types.Integer.from_mcnp(tokens[4])
        ncl = types.Integer.from_mcnp(tokens[5])
        mat = types.Integer.from_mcnp(tokens[6])
        ncp = types.Integer.from_mcnp(tokens[7])

        return J_5(
            next_type,
            node,
            nsx_nsf_nter,
            ntyn_mtp_angle_branch,
            ncl,
            mat,
            ncp,
        )

    def to_mcnp(self):
        """
        Generates PTRAC from `J_5`.

        Returns:
            PTRAC for `J_5`.
        """

        return f' {str(self.next_type):>10}{str(self.node):>10}{str(self.nsx_nsf_nter):>10}{str(self.ntyn_mtp_angle_branch):>10}{str(self.ncl):>10}{str(self.mat):>10}{str(self.ncp):>10}'
