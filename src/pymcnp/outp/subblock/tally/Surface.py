import re
import typing
import dataclasses

import pandas

from .... import abc
from ... import line
from ..Tally import Tally


class Space(abc.Terminal):
    """
    Represents spaces for lines.
    """

    _pattern = re.compile(r'(\n)([\s\S]*)', re.IGNORECASE)
    _default = '\n'


class Surface(Tally):
    """
    Represents surface subtally blocks.

    Attributes:
        surface_number_preamble: surface subtally block `      surface.
        surface_number: surface subtally block surface number.
        table_heading: surface subtally block `\n        time   ` symbol.
        table_body_preamble: surface subtally block `\n\n` symbol.
        table_body: surface subtally block table body.
        table_total_preamble: surface subtally block `\n      total      ` symbol.
        table_total: surface subtally block table total.
        table_footing: surface subtally block `\n ?\n` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    surface_number_preamble: typing.Annotated[abc.Terminal, r'      surface:'] = abc.Terminal[r'      surface:']('      surface:')
    surface_number: typing.Annotated[abc.Terminal, r'.+(?=\n|\Z)']
    table_heading: typing.Annotated[abc.Terminal, r'\n        time   '] = abc.Terminal[r'\n        time   ']('\n        time   ')
    table_body_preamble: typing.Annotated[abc.Terminal, r'\n'] = abc.Terminal[r'\n']('\n')
    table_body: typing.Annotated[abc.Array, line.Tally, Space] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    table_total_preamble: typing.Annotated[abc.Terminal, r'\n      total      '] = abc.Terminal[r'\n      total      ']('\n      total      ')
    table_total: typing.Annotated[abc.Terminal, r'.+(?=\n|\Z)']
    table_footing: typing.Annotated[abc.Terminal, r'\n ?\n'] = abc.Terminal[r'\n ?\n']('\n\n')

    def to_dataframe(self) -> pandas.DataFrame:
        """
        Generates pandas dataframes for surface angle subtally blocks.

        Returns:
            Corresponding pandas dataframe for `self`.
        """

        assert isinstance(self.table_body, (abc.Array, abc.Terminal[r'']))
        assert not isinstance(self.table_body, abc.Array) or all(isinstance(row, line.Tally) for row in self.table_body)

        if isinstance(self.table_body, abc.Array) and self.table_body:
            df = pandas.concat((row.to_dataframe() for row in self.table_body), ignore_index=True)
            df['surface_number'] = self.surface_number.strip()
            return df

        return pandas.DataFrame()
