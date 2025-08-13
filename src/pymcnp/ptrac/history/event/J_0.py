import re
import typing

from . import j
from . import _line
from .... import types
from .... import errors


class J_0(_line.EventLine):
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

    def __init__(
        self,
        next_type: j.EventType,
        pbl: types.Integer,
        nsr: types.Integer,
        ncl: types.Integer,
        mat: types.Integer,
    ):
        """
        Initializes `J_0`.

        Parameters:
            next_type: Next J line event type.
            pbl: Number of nodes in track from source.
            nsr: Source type.
            ncl: Problem numbers of the cells.
            mat: Material numbers of the cells.

        Raises:
            PtracError: SEMANTICS_LINE.
        """

        if next_type is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, next_type)

        if pbl is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, pbl)

        if nsr is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, nsr)

        if ncl is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, ncl)

        if mat is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, mat)

        self.next_type: typing.Final[j.EventType] = next_type
        self.pbl: typing.Final[types.Integer] = pbl
        self.nsr: typing.Final[types.Integer] = nsr
        self.ncl: typing.Final[types.Integer] = ncl
        self.mat: typing.Final[types.Integer] = mat

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
