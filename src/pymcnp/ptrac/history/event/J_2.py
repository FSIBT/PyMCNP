import re

from . import j
from . import _line
from .... import types
from .... import errors
from .... import _fields


class J_2(_fields.Fields, _line.EventLine):
    """
    Represents PTRAC history block j lines form #2a.

    Attributes:
        next_type: Next event type.
        node: Number of node in track from source.
        nsr: Source type.
        ipt: Particle type.
        ncl: Problem numbers of the cells.
        mat: Material numbers of the cells.
    """

    _REGEX = re.compile(r'\A\s(.{10})(.{10})(.{10})(.{10})(.{10})(.{10})\Z', re.IGNORECASE)

    _ERROR = errors.PtracError
    _CODE = errors.PtracCode.SEMANTICS_LINE

    next_type = _fields.Field(j.EventType, 'Next event type')
    node = _fields.Field(types.Integer, 'Number of node in track from source')
    nsr = _fields.Field(types.Real, 'Source type')
    ipt = _fields.Field(types.Integer, 'Particle type')
    ncl = _fields.Field(types.Integer, 'Problem numbers of the cells')
    mat = _fields.Field(types.Integer, 'Material numbers of the cells')

    def from_mcnp(source: str):
        """
        Generates `J_2` from PTRAC.

        Parameters:
            source: PTRAC for `J_2`.

        Returns:
            `J_2`.

        Raises:
            PtracError: SYNTAX_LINE.
        """

        tokens = J_2._REGEX.match(source)

        if not tokens:
            raise errors.PtracError(errors.PtracCode.SYNTAX_LINE, source)

        next_type = j.EventType.from_mcnp(tokens[1].strip())
        node = types.Integer.from_mcnp(tokens[2])
        nsr = types.Real.from_mcnp(tokens[3])
        ipt = types.Integer.from_mcnp(tokens[4])
        ncl = types.Integer.from_mcnp(tokens[5])
        mat = types.Integer.from_mcnp(tokens[6])

        return J_2(
            next_type,
            node,
            nsr,
            ipt,
            ncl,
            mat,
        )

    def to_mcnp(self):
        """
        Generates PTRAC from `J_2`.

        Returns:
            PTRAC for `J_2`.
        """

        return f' {str(self.next_type):>10}{str(self.node):>10}{str(self.nsr):>10}{str(self.ipt):>10}{str(self.ncl):>10}{str(self.mat):>10}'
