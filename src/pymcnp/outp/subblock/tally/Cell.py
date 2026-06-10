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


class Cell(Tally):
    """
    Represents cell subtally blocks.

    Attributes:
        cell_number_preamble: cell subtally block ` cell  ` symbol.
        cell_number: cell subtally block `cell_number` parameter.
        table_heading: cell subtally block `\n      energy   ` symbol.
        table_body_preamble: cell subtally block `\n\n` symbol.
        table_body: cell subtally block `table_body` parameter.
        table_total_preamble: cell subtally block `\n      total      ` symbol.
        table_total: cell subtally block `table_total` parameter.
        table_footing: cell subtally block `\n ?\n` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    cell_number_preamble: typing.Annotated[abc.Terminal, r' cell  '] = abc.Terminal[r' cell  '](' cell  ')
    cell_number: typing.Annotated[abc.Terminal, r'.+(?=\n|\Z)']
    table_heading: typing.Annotated[abc.Terminal, r'\n      energy   \n'] = abc.Terminal[r'\n      energy   \n']('\n      energy   \n')
    table_body: typing.Annotated[abc.Array, line.Tally, Space] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    table_total_preamble: typing.Annotated[abc.Terminal, r'\n      total      '] = abc.Terminal[r'\n      total      ']('\n      total      ')
    table_total: typing.Annotated[abc.Terminal, r'.+(?=\n|\Z)']
    table_footing: typing.Annotated[abc.Terminal, r'\n ?\n'] = abc.Terminal[r'\n\n']('\n\n')

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
            df['cell_number'] = self.cell_number.strip()
            return df

        return pandas.DataFrame()
