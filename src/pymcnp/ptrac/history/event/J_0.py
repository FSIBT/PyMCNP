import re

from . import j
from . import _line
from .... import types
from .... import errors
from .... import _fields


class J_0(_fields.Fields, _line.EventLine):
    """
    Represents PTRAC history block j lines form #1a.

    Attributes:
        next_type: Next J line event type.
        node: Number of node in track from source.
        nsr: Source type.
        ncl: Problem numbers of the cells.
        mat: Material numbers of the cells.
    """

    _REGEX = re.compile(r'\A\s(.{10})(.{10})(.{10})(.{10})(.{10})\Z', re.IGNORECASE)

    _ERROR = errors.PtracError
    _CODE = errors.PtracCode.SEMANTICS_LINE

    next_type = _fields.Field(j.EventType, 'Next J line event type')
    pbl = _fields.Field(types.Integer, 'Number of nodes in track from source')
    nsr = _fields.Field(types.Integer, 'Source type')
    ncl = _fields.Field(types.Integer, 'Problem numbers of the cells')
    mat = _fields.Field(types.Integer, 'Material numbers of the cells')

    def from_mcnp(source: str):
        """
        Generates `J_0` from PTRAC.

        Parameters:
            source: PTRAC for `J_0`.

        Returns:
            `J_0`.

        Raises:
            PtracError: SYNTAX_LINE.
        """

        tokens = J_0._REGEX.match(source)

        if not tokens:
            raise errors.PtracError(errors.PtracCode.SYNTAX_LINE, source)

        next_type = j.EventType.from_mcnp(tokens[1].strip())
        pbl = types.Integer.from_mcnp(tokens[2])
        nsr = types.Integer.from_mcnp(tokens[3])
        ncl = types.Integer.from_mcnp(tokens[4])
        mat = types.Integer.from_mcnp(tokens[5])

        return J_0(
            next_type,
            pbl,
            nsr,
            ncl,
            mat,
        )

    def to_mcnp(self):
        """
        Generates PTRAC from `J_0`.

        Returns:
            PTRAC for `J_0`.
        """

        return f' {str(self.next_type):>10}{str(self.pbl):>10}{str(self.nsr):>10}{str(self.ncl):>10}{str(self.mat):>10}'
