import typing

import pandas

from .... import abc
from ... import line
from ..Tally import Tally


class Surface(Tally, abc.symbol.WithDataIter):
    """
    Represents surface subtally blocks.

    Attributes:
        surface_number_preamble: surface subtally block ``      surface.
        surface_number: surface subtally block surface number.
        table_heading: surface subtally block ``r'\\n        time   '`` symbol.
        table_body_preamble: surface subtally block ``r'\\n\\n'`` symbol.
        table_body: surface subtally block table body.
        table_total_preamble: surface subtally block ``r'\\n      total      '`` symbol.
        table_total: surface subtally block table total.
        table_footing: surface subtally block ``r'\\n ?\\n'`` symbol.
    """

    surface_number_preamble: typing.Annotated[abc.Terminal, r'      surface:']
    surface_number: typing.Annotated[abc.Terminal, r'.+(?=\n|\Z)']
    table_heading: typing.Annotated[abc.Terminal, r'\n        time   ']
    table_body_preamble: typing.Annotated[abc.Terminal, r'\n']
    table_body: typing.Annotated[abc.Array, line.Tally, typing.Annotated[abc.Terminal, r'\n']]
    table_total_preamble: typing.Annotated[abc.Terminal, r'\n      total      ']
    table_total: typing.Annotated[abc.Terminal, r'.+(?=\n|\Z)']
    table_footing: typing.Annotated[abc.Terminal, r'\n ?\n']

    def to_dataframe_iter(self, returning: bool = False) -> typing.Generator[pandas.DataFrame, None, pandas.DataFrame | None]:
        """
        Generates pandas dataframes for surface subtally blocks.

        Parameters:
            returning: Flag to/to not return.

        Yields:
            Pandas dataframes for surface subtally blocks.

        Returns:
            Pandas dataframe for all surface subtally blocks.
        """

        assert isinstance(self.table_body, (abc.Array, abc.Terminal[r'']))
        assert not isinstance(self.table_body, abc.Array) or all(isinstance(row, line.Tally) for row in self.table_body)

        if isinstance(self.table_body, abc.Array) and self.table_body:
            frame = pandas.concat((row.to_dataframe() for row in self.table_body), ignore_index=True)
            frame['surface_number'] = self.surface_number.strip()
        else:
            frame = pandas.DataFrame()

        yield frame

        if returning:
            return frame
