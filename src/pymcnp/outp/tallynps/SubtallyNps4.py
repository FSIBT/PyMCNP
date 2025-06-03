import re
import typing

from . import _subblock
from ...utils import types
from ...utils import errors


class SubtallyNps4(_subblock.Subblock):
    """
    Represents OUTP ``1tally 4 nps`` subtally.

    Attributes:
        surface: Surface number.
        tallies: Tallies.
        total: Total line.
    """

    _REGEX = re.compile(
        r'\A cell  (.+)\n' r'      energy   \n' r'((?:.+\n)+)' r'      total      (.+)\n\n\Z'
    )

    def __init__(
        self,
        surface: types.String,
        tallies: types.String,
        total: types.String,
    ):
        """
        Initializes ``SubtallyNps4``.

        Parameters:
            surface: Surface number.
            tallies: Tallies.
            total: Total line.

        Raises:
            OutpError: SEMANTICS_TABLE.
        """

        if surface is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, surface)
        if tallies is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, tallies)
        if total is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, total)

        self.surface: typing.Final[types.String] = surface
        self.tallies: typing.Final[types.String] = tallies
        self.total: typing.Final[types.String] = total

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``SubtallyNps4`` from OUTP.

        Parameters:
            source: OUTP for ``SubtallyNps4``.

        Returns:
            ``SubtallyNps4``.
        """

        tokens = SubtallyNps4._REGEX.match(source)

        if not tokens:
            raise errors.OutpError(errors.OutpCode.SYNTAX_TABLE, source)

        surface = types.String.from_mcnp(tokens[1])
        tallies = types.String.from_mcnp(tokens[2])
        total = types.String.from_mcnp(tokens[3])

        return SubtallyNps4(
            surface,
            tallies,
            total,
        )

    def to_mcnp(self):
        """
        Generates OUTP from ``SubtallyNps4``.

        Returns:
            OUTP for ``SubtallyNps4``.
        """

        return f"""
 surface  {self.surface}
      time
{self.tallies}
      total      {self.total}\n
"""[1:-1]
