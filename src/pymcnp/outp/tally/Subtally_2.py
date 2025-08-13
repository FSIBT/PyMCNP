import re
import typing

import pandas

from . import subtally
from . import _subblock
from ... import types
from ... import errors


class Subtally_2(_subblock.TallySubblock):
    """
    Represents OUTP `1tally 2 nps` subtally.

    Attributes:
        surface: Surface number.
        lines: Tally lines.
        total: Total line.
    """

    _REGEX = re.compile(r'\A      surface:  (.+)\n' r'        time   \n' r'((?:.+\n)+)' r'      total      (.+)\n\n\Z', re.IGNORECASE)

    def __init__(
        self,
        surface: types.String,
        lines: types.Generator(types.String),
        total: types.String,
    ):
        """
        Initializes `Subtally_2`.

        Parameters:
            surface: Surface number.
            lines: Tally lines.
            total: Total line.

        Raises:
            OutpError: SEMANTICS_TABLE.
        """

        if surface is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, surface)
        if lines is None or None in lines:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, lines)
        if total is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, total)

        self.surface: typing.Final[types.String] = surface
        self.lines: typing.Final[types.String] = lines
        self.total: typing.Final[types.String] = total

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Subtally_2` from OUTP.

        Parameters:
            source: OUTP for `Subtally_2`.

        Returns:
            `Subtally_2`.
        """

        tokens = Subtally_2._REGEX.match(source)

        if not tokens:
            raise errors.OutpError(errors.OutpCode.SYNTAX_TABLE, source)

        surface = types.String.from_mcnp(tokens[1])
        lines = types.Generator(subtally.Line).from_mcnp(tokens[2])
        total = types.String.from_mcnp(tokens[3])

        return Subtally_2(
            surface,
            lines,
            total,
        )

    def to_mcnp(self):
        """
        Generates OUTP from `Subtally_2`.

        Returns:
            OUTP for `Subtally_2`.
        """

        return f"""
      surface:  {self.surface}
        time   
{''.join(map(str, self.lines))}      total      {self.total}

"""[1:]

    def to_dataframe(self):
        """
        Generates `pandas.DataFrame` from `Subtally_2`.

        Returns:
            `pandas.DataFrame`.
        """

        df = pandas.concat((line.to_dataframe() for line in self.lines), ignore_index=True)
        df['surface'] = self.surface.value.strip()
        return df
