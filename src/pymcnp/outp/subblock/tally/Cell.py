import typing

import pandas

from .... import abc
from ... import line
from ..Tally import Tally


class Cell(Tally, abc.symbol.WithDataIter):
    """
    Represents cell subtally blocks.

    Attributes:
        cell_number_preamble: cell subtally block ``r' cell  '`` symbol.
        cell_number: cell subtally block cell number.
        table_heading: cell subtally block ``r'\\n      energy   '`` symbol.
        table_body_preamble: cell subtally block ``r'\\n\\n'`` symbol.
        table_body: cell subtally block table body.
        table_total_preamble: cell subtally block ``r'\\n      total      '`` symbol.
        table_total: cell subtally block table total.
        table_footing: cell subtally block ``r'\\n ?\\n'`` symbol.
    """

    cell_number_preamble: typing.Annotated[abc.Terminal, r' cell  ']
    cell_number: typing.Annotated[abc.Terminal, r'.+(?=\n|\Z)']
    table_heading: typing.Annotated[abc.Terminal, r'\n      energy   \n']
    table_body: typing.Annotated[abc.Array, line.Tally, typing.Annotated[abc.Terminal, r'\n']]
    table_total_preamble: typing.Annotated[abc.Terminal, r'\n      total      ']
    table_total: typing.Annotated[abc.Terminal, r'.+(?=\n|\Z)']
    table_footing: typing.Annotated[abc.Terminal, r'\n ?\n']

    def to_dataframe_iter(self, returning: bool = False) -> typing.Generator[pandas.DataFrame, None, pandas.DataFrame | None]:
        """
        Generates pandas dataframes for cell subtally blocks.

        Parameters:
            returning: Flag to/to not return.

        Yields:
            Pandas dataframes for cell subtally blocks.

        Returns:
            Pandas dataframe for all cell subtally blocks.
        """

        assert isinstance(self.table_body, (abc.Array, abc.Terminal[r'']))
        assert not isinstance(self.table_body, abc.Array) or all(isinstance(row, line.Tally) for row in self.table_body)

        if isinstance(self.table_body, abc.Array) and self.table_body:
            frame = pandas.concat((row.to_dataframe() for row in self.table_body), ignore_index=True)
            frame['cell_number'] = self.cell_number.strip()
        else:
            frame = pandas.DataFrame()

        yield frame

        if returning:
            return frame
