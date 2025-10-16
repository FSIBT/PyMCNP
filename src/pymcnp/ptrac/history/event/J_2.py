import re
import typing

from . import j
from . import _line
from .... import types
from .... import errors


class J_2(_line.EventLine):
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

    def __init__(
        self,
        next_type: j.EventType,
        node: types.Integer,
        nsr: types.Real,
        ipt: types.Integer,
        ncl: types.Integer,
        mat: types.Integer,
    ):
        """
        Initializes `J_2`.

        Parameters:
            next_type: Next event type.
            node: Number of node in track from source.
            nsr: Source type.
            ipt: Particle type.
            ncl: Problem numbers of the cells.
            mat: Material numbers of the cells.

        Raises:
            PtracError: SEMANTICS_LINE.
        """

        if next_type is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, next_type)

        if node is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, node)

        if nsr is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, nsr)

        if ipt is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, ipt)

        if ncl is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, ncl)

        if mat is None:
            raise errors.PtracError(errors.PtracCode.SEMANTICS_LINE, mat)

        self.next_type: typing.Final[j.EventType] = next_type
        self.node: typing.Final[types.Integer] = node
        self.nsr: typing.Final[types.Real] = nsr
        self.ipt: typing.Final[types.Integer] = ipt
        self.ncl: typing.Final[types.Integer] = ncl
        self.mat: typing.Final[types.Integer] = mat

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
