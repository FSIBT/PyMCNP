import re
import typing

from . import _subblock
from ...utils import types
from ...utils import errors


class SubtallyNps1(_subblock.Subblock):
    """
    Represents OUTP ``1tally 1 nps`` subtally.

    Attributes:
        surface: Surface number.
        angles: Angle bins.
        tallies: Tallies.
        total: Total line.
    """

    _REGEX = re.compile(
        r'\A surface  (.+)\n'
        r' angle  bin: (.+)\n'
        r'      energy   \n'
        r'((?:.+\n)+)'
        r'      total      (.+)\n\n\Z'
    )

    def __init__(
        self,
        surface: types.String,
        angles: types.String,
        tallies: types.String,
        total: types.String,
    ):
        """
        Initializes ``SubtallyNps1``.

        Parameters:
            surface: Surface number.
            angles: Angle bins.
            tallies: Tallies.
            total: Total line.

        Raises:
            OutpError: SEMANTICS_TABLE.
        """

        if surface is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, surface)
        if angles is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, angles)
        if tallies is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, tallies)
        if total is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, total)

        self.surface: typing.Final[types.String] = surface
        self.angles: typing.Final[types.String] = angles
        self.tallies: typing.Final[types.String] = tallies
        self.total: typing.Final[types.String] = total

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SubtallyNps1`` from OUTP.

        Parameters:
            source: OUTP for ``SubtallyNps1``.

        Returns:
            ``SubtallyNps1``.
        """

        tokens = SubtallyNps1._REGEX.match(source)

        if not tokens:
            raise errors.OutpError(errors.OutpCode.SYNTAX_TABLE, source)

        surface = types.String.from_mcnp(tokens[1])
        angles = types.String.from_mcnp(tokens[2])
        tallies = types.String.from_mcnp(tokens[3])
        total = types.String.from_mcnp(tokens[4])

        return SubtallyNps1(
            surface,
            angles,
            tallies,
            total,
        )

    def to_mcnp(self):
        """
        Generates OUTP from ``SubtallyNps1``.

        Returns:
            OUTP for ``SubtallyNps1``.
        """

        return f"""
 surface  {self.surface}
 angle  bin: {self.angles}
      energy   
{self.tallies}
      total      {self.total}\n
"""[1:-1]
