import re

import pandas

from . import subtally
from . import _subblock
from ... import types
from ... import errors
from ... import _fields


class Subtally_1(_fields.Fields, _subblock.TallySubblock):
    """
    Represents OUTP `1tally 1 nps` subtally.

    Attributes:
        surface: Surface number.
        angle_from: Angle bin start.
        angle_to: Angle bin end.
        lines: Tally lines.
        total: Total line.
    """

    _REGEX = re.compile(r'\A surface {2}([^\n]+)\n angle {2}bin: {2}([^\n]{12}) to {2}([^\n]{11}) degrees {85}\n {6}energy {3}\n((?:[^\n]+\n)+?) {6}total {6}([^\n]+)\n ?\n\Z', re.IGNORECASE)

    _ERROR = errors.OutpError
    _CODE = errors.OutpCode.SEMANTICS_TABLE

    surface = _fields.Field(types.String, 'Surface number')
    angle_from = _fields.Field(types.String, 'Angle bin start')
    angle_to = _fields.Field(types.String, 'Angle bin end')
    lines = _fields.Field(types.Generator(types.String), 'Tally lines', many=True)
    total = _fields.Field(types.String, 'Total line')

    @staticmethod
    def from_mcnp(source: str):
        """
        Generates `Subtally_1` from OUTP.

        Parameters:
            source: OUTP for `Subtally_1`.

        Returns:
            `Subtally_1`.
        """

        tokens = Subtally_1._REGEX.match(source)

        if not tokens:
            raise errors.OutpError(errors.OutpCode.SYNTAX_TABLE, source)

        surface = types.String.from_mcnp(tokens[1])
        angle_from = types.String.from_mcnp(tokens[2])
        angle_to = types.String.from_mcnp(tokens[3])
        lines = types.Generator(subtally.Line).from_mcnp(tokens[4])
        total = types.String.from_mcnp(tokens[5])

        return Subtally_1(
            surface,
            angle_from,
            angle_to,
            lines,
            total,
        )

    def to_mcnp(self):
        """
        Generates OUTP from `Subtally_1`.

        Returns:
            OUTP for `Subtally_1`.
        """

        return f"""
 surface  {self.surface}
 angle  bin:  {self.angle_from} to  {self.angle_to} degrees                                                                                     
      energy   
{''.join(map(str, self.lines))}      total      {self.total}

"""[1:]

    def to_dataframe(self):
        """
        Generates `pandas.DataFrame` from `Subtally_1`.

        Returns:
            `pandas.DataFrame`.
        """

        df = pandas.concat((line.to_dataframe() for line in self.lines), ignore_index=True)
        df['surface'] = self.surface.value.strip()
        df['angle_from'] = self.angle_from.value.strip()
        df['angle_to'] = self.angle_to.value.strip()
        return df
