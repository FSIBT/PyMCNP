import re
import typing

import pandas

from . import subtally
from . import _subblock
from ... import types
from ... import errors


class Subtally_4(_subblock.TallySubblock):
    """
    Represents OUTP `1tally 4 nps` subtally.

    Attributes:
        cell: Cell number.
        lines: Tally lines.
        total: Total line.
    """

    _REGEX = re.compile(r'\A cell  (.+)\n' r'      energy   \n' r'((?:.+\n)+)' r'      total      (.+)\n\n\Z', re.IGNORECASE)

    def __init__(
        self,
        cell: types.String,
        lines: types.Generator(types.String),
        total: types.String,
    ):
        """
        Initializes `Subtally_4`.

        Parameters:
            cell: Cell number.
            lines: Tally lines.
            total: Total line.

        Raises:
            OutpError: SEMANTICS_TABLE.
        """

        if cell is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, cell)
        if lines is None or None in lines:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, lines)
        if total is None:
            raise errors.OutpError(errors.OutpCode.SEMANTICS_TABLE, total)

        self.cell: typing.Final[types.String] = cell
        self.lines: typing.Final[types.String] = lines
        self.total: typing.Final[types.String] = total

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Subtally_4` from OUTP.

        Parameters:
            source: OUTP for `Subtally_4`.

        Returns:
            `Subtally_4`.
        """

        tokens = Subtally_4._REGEX.match(source)

        if not tokens:
            raise errors.OutpError(errors.OutpCode.SYNTAX_TABLE, source)

        cell = types.String.from_mcnp(tokens[1])
        lines = types.Generator(subtally.Line).from_mcnp(tokens[2])
        total = types.String.from_mcnp(tokens[3])

        return Subtally_4(
            cell,
            lines,
            total,
        )

    def to_mcnp(self):
        """
        Generates OUTP from `Subtally_4`.

        Returns:
            OUTP for `Subtally_4`.
        """

        return f"""
 cell  {self.cell}
      energy   
{''.join(map(str, self.lines))}      total      {self.total}

"""[1:]

    def to_dataframe(self):
        """
        Generates `pandas.DataFrame` from `Subtally_4`.

        Returns:
            `pandas.DataFrame`.
        """

        df = pandas.concat((line.to_dataframe() for line in self.lines), ignore_index=True)
        df['cell'] = self.cell.value.strip()
        return df
