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


class SurfaceAngle(Tally):
    """
    Represents surface angle subtally blocks.

    Attributes:
        surface_number_preamble: surface angle subtally block `surface_number_preamble` parameter.
        surface_number: surface angle subtally block `surface_number` parameter.
        angle_from_preamble: surface angle subtally block `\n angle bin.
        angle_from: surface angle subtally block `angle_from` parameter.
        angle_to_preamble: surface angle subtally block ` to  ` symbol.
        angle_to: surface angle subtally block `angle_to` parameter.
        angle_to_postamble: surface angle subtally block `angle_to_postamble` parameter.
        table_heading: surface angle subtally block `\n {6}energy {3}` symbol.
        table_body_preamble: surface angle subtally block `\n\n` symbol.
        table_body: surface angle subtally block `table_body` parameter.
        table_total_preamble: surface angle subtally block `\n {6}total {6}` symbol.
        table_total: surface angle subtally block `table_total` parameter.
        table_footing: surface angle subtally block `\n ?\n` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    surface_number_preamble: typing.Annotated[abc.Terminal, r' surface '] = abc.Terminal[r' surface '](' surface ')
    surface_number: typing.Annotated[abc.Terminal, r'.+(?=\n|\Z)']
    angle_from_preamble: typing.Annotated[abc.Terminal, r'\n angle  bin:  '] = abc.Terminal[r'\n angle  bin:  ']('\n angle  bin:  ')
    angle_from: typing.Annotated[abc.Terminal, r'.{12}']
    angle_to_preamble: typing.Annotated[abc.Terminal, r' to  '] = abc.Terminal[r' to  '](' to  ')
    angle_to: typing.Annotated[abc.Terminal, r'.{11}']
    angle_to_postamble: typing.Annotated[abc.Terminal, r' degrees {85}']
    table_heading: typing.Annotated[abc.Terminal, r'\n {6}energy {3}'] = abc.Terminal[r'\n {6}energy {3}']('\n      energy   ')
    table_body_preamble: typing.Annotated[abc.Terminal, r'\n'] = abc.Terminal[r'\n']('\n')
    table_body: typing.Annotated[abc.Array, line.Tally, Space] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    table_total_preamble: typing.Annotated[abc.Terminal, r'\n {6}total {6}'] = abc.Terminal[r'\n {6}total {6}']('\n      total      ')
    table_total: typing.Annotated[abc.Terminal, r'.+(?=\n|\Z)']
    table_footing: typing.Annotated[abc.Terminal, r'\n ?\n'] = abc.Terminal[r'\n ?\n']('\n \n')

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
            df['angle_from'] = self.angle_from.strip()
            df['angle_to'] = self.angle_to.strip()
            return df

        return pandas.DataFrame()
