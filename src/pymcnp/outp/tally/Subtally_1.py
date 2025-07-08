import re
import typing

import pandas

from . import subtally
from . import _subblock
from ...utils import types
from ...utils import errors


class Subtally_1(_subblock.Subblock):
    """
    Represents OUTP ``1tally 1 nps`` subtally.

    Attributes:
        surface: Surface number.
        angles: Angle bins.
        lines: Tally lines.
        total: Total line.
    """

    _REGEX = re.compile(r'\A surface {2}([^\n]+)\n angle {2}bin: ([^\n]+)\n {6}energy {3}\n((?:[^\n]+\n)+?) {6}total {6}([^\n]+)\n ?\n\Z')

    def __init__(
        self,
        surface: types.String,
        angles: types.String,
        lines: types.Tuple[types.String],
        total: types.String,
    ):
        """
        Initializes ``Subtally_1``.

        Parameters:
            surface: Surface number.
            angles: Angle bins.
            lines: Tally lines.
            total: Total line.

        Raises:
            OutpError: SEMANTICS_TABLE.
        """

        if surface is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, surface)
        if angles is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, angles)
        if lines is None or None in lines:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, lines)
        if total is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, total)

        self.surface: typing.Final[types.String] = surface
        self.angles: typing.Final[types.String] = angles
        self.lines: typing.Final[types.String] = lines
        self.total: typing.Final[types.String] = total

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates ``Subtally_1`` from OUTP.

        Parameters:
            source: OUTP for ``Subtally_1``.

        Returns:
            ``Subtally_1``.
        """

        tokens = Subtally_1._REGEX.match(source)

        if not tokens:
            raise errors.OutpError(errors.OutpCode.SYNTAX_TABLE, source)

        surface = types.String.from_mcnp(tokens[1])
        angles = types.String.from_mcnp(tokens[2])
        lines = types.Tuple.from_mcnp(tokens[3], subtally.Line)
        total = types.String.from_mcnp(tokens[4])

        return Subtally_1(
            surface,
            angles,
            lines,
            total,
        )

    def to_mcnp(self):
        """
        Generates OUTP from ``Subtally_1``.

        Returns:
            OUTP for ``Subtally_1``.
        """

        return f"""
 surface  {self.surface}
 angle  bin: {self.angles}
      energy   
{''.join(map(str, self.lines))}      total      {self.total}

"""[1:]

    def to_dataframe(self):
        """
        Generates ``pandas.DataFrame`` from ``Subtally_1``.

        Returns:
            ``pandas.DataFrame``.
        """

        df = pandas.concat((line.to_dataframe() for line in self.lines), ignore_index=True)
        df['surface'] = self.surface.strip()
        df['angle'] = self.angles.strip()
        return df
