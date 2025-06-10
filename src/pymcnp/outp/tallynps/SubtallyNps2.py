import re
import typing

from . import _subblock
from ...utils import types
from ...utils import errors


class SubtallyNps2(_subblock.Subblock):
    """
    Represents OUTP ``1tally 2 nps`` subtally.

    Attributes:
        surface: Surface number.
        tallies: Tallies.
        total: Total line.
    """

    _REGEX = re.compile(r'\A      surface:  (.+)\n' r'        time   \n' r'((?:.+\n)+)' r'      total      (.+)\n\n\Z')

    def __init__(
        self,
        surface: types.String,
        tallies: types.String,
        total: types.String,
    ):
        """
        Initializes ``SubtallyNps2``.

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
        Generates ``SubtallyNps2`` from OUTP.

        Parameters:
            source: OUTP for ``SubtallyNps2``.

        Returns:
            ``SubtallyNps2``.
        """

        tokens = SubtallyNps2._REGEX.match(source)

        if not tokens:
            raise errors.OutpError(errors.OutpCode.SYNTAX_TABLE, source)

        surface = types.String.from_mcnp(tokens[1])
        tallies = types.String.from_mcnp(tokens[2])
        total = types.String.from_mcnp(tokens[3])

        return SubtallyNps2(
            surface,
            tallies,
            total,
        )

    def to_mcnp(self):
        """
        Generates OUTP from ``SubtallyNps2``.

        Returns:
            OUTP for ``SubtallyNps2``.
        """

        return f"""
 surface  {self.surface}
      time
{self.tallies}
      total      {self.total}\n
"""[1:-1]
