import re

from . import j
from . import _line
from .... import types
from .... import errors
from .... import _fields


class J_3(_fields.Fields, _line.EventLine):
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

    _REGEX = re.compile(r'\A\s(.{10})(.{10})(.{10})(.{10})(.{10})(.{10})(.{10})\Z', re.IGNORECASE)

    _ERROR = errors.PtracError
    _CODE = errors.PtracCode.SEMANTICS_LINE

    next_type = _fields.Field(j.EventType, 'Next event type')
    node = _fields.Field(types.Integer, 'Number of node in track from source')
    nsx_nsf_nter = _fields.Field(types.Integer, 'NSR or NSF or NTER')
    ntyn_mtp_angle_branch = _fields.Field(types.Integer, 'NTYN/MTP or 13 or 15')
    ipt = _fields.Field(types.Integer, 'Particle type')
    ncl = _fields.Field(types.Integer, 'Problem numbers of the cells')
    mat = _fields.Field(types.Integer, 'Material numbers of the cells')

    def from_mcnp(source: str):
        """
        Generates `J_3` from PTRAC.

        Parameters:
            source: PTRAC for `J_3`.

        Returns:
            `J_3`.

        Raises:
            PtracError: SYNTAX_LINE.
        """

        tokens = J_3._REGEX.match(source)

        if not tokens:
            raise errors.PtracError(errors.PtracCode.SYNTAX_LINE, source)

        next_type = j.EventType.from_mcnp(tokens[1].strip())
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

    def to_mcnp(self):
        """
        Generates PTRAC from `J_3`.

        Returns:
            PTRAC for `J_3`.
        """

        return f' {str(self.next_type):>10}{str(self.node):>10}{str(self.nsx_nsf_nter):>10}{str(self.ntyn_mtp_angle_branch):>10}{str(self.ipt):>10}{str(self.ncl):>10}{str(self.mat):>10}'
