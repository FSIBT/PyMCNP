import typing

import pandas

from .... import abc
from ... import line
from ..Tally import Tally


class SurfaceAngle(Tally, abc.symbol.WithDataIter):
    """
    Represents surface angle subtally blocks.

    Attributes:
        surface_number_preamble: surface angle subtally block surface number preamble.
        surface_number: surface angle subtally block surface number.
        angle_from_preamble: surface angle subtally block angle bin preamble.
        angle_from: surface angle subtally block angle from.
        angle_to_preamble: surface angle subtally block ``r' to  '`` symbol.
        angle_to: surface angle subtally block angle to.
        angle_to_postamble: surface angle subtally block angle to postamble.
        table_heading: surface angle subtally block ``r'\\n {6}energy {3}'`` symbol.
        table_body_preamble: surface angle subtally block ``r'\\n\\n'`` symbol.
        table_body: surface angle subtally block table body.
        table_total_preamble: surface angle subtally block ``r'\\n {6}total {6}'`` symbol.
        table_total: surface angle subtally block table total.
        table_footing: surface angle subtally block ``r'\\n ?\\n'`` symbol.
    """

    surface_number_preamble: typing.Annotated[abc.Terminal, r' surface ']
    surface_number: typing.Annotated[abc.Terminal, r'.+(?=\n|\Z)']
    angle_from_preamble: typing.Annotated[abc.Terminal, r'\n angle  bin:  ']
    angle_from: typing.Annotated[abc.Terminal, r'.{12}']
    angle_to_preamble: typing.Annotated[abc.Terminal, r' to  ']
    angle_to: typing.Annotated[abc.Terminal, r'.{11}']
    angle_to_postamble: typing.Annotated[abc.Terminal, r' degrees {85}']
    table_heading: typing.Annotated[abc.Terminal, r'\n {6}energy {3}']
    table_body_preamble: typing.Annotated[abc.Terminal, r'\n']
    table_body: typing.Annotated[abc.Array, line.Tally, typing.Annotated[abc.Terminal, r'\n']]
    table_total_preamble: typing.Annotated[abc.Terminal, r'\n {6}total {6}']
    table_total: typing.Annotated[abc.Terminal, r'.+(?=\n|\Z)']
    table_footing: typing.Annotated[abc.Terminal, r'\n ?\n']

    def to_dataframe_iter(self, returning: bool = False) -> typing.Generator[pandas.DataFrame, None, pandas.DataFrame | None]:
        """
        Generates pandas dataframes for surface angle subtally blocks.

        Parameters:
            returning: Flag to/to not return.

        Yields:
            Pandas dataframes for surface angle subtally blocks.

        Returns:
            Pandas dataframe for all surface angle subtally blocks.
        """

        assert isinstance(self.table_body, (abc.Array, abc.Terminal[r'']))
        assert not isinstance(self.table_body, abc.Array) or all(isinstance(row, line.Tally) for row in self.table_body)

        if isinstance(self.table_body, abc.Array) and self.table_body:
            frame = pandas.concat((row.to_dataframe() for row in self.table_body), ignore_index=True)
            frame['surface_number'] = self.surface_number.strip()
            frame['angle_from'] = self.angle_from.strip()
            frame['angle_to'] = self.angle_to.strip()
        else:
            frame = pandas.DataFrame()

        yield frame

        if returning:
            return frame
