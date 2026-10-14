import re

import pandas

from . import subtally
from . import _subblock
from ... import types
from ... import errors
from ... import _fields


class Subtally_4(_fields.Fields, _subblock.TallySubblock):
    """
    Represents OUTP `1tally 4 nps` subtally.

    Attributes:
        cell: Cell number.
        lines: Tally lines.
        total: Total line.
    """

    _REGEX = re.compile(r'\A cell  (.+)\n' r'      energy   \n' r'((?:.+\n)+)' r'      total      (.+)\n\n\Z', re.IGNORECASE)

    _ERROR = errors.OutpError
    _CODE = errors.OutpCode.SEMANTICS_TABLE

    cell = _fields.Field(types.String, 'Cell number')
    lines = _fields.Field(types.Generator(types.String), 'Tally lines', many=True)
    total = _fields.Field(types.String, 'Total line')

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
