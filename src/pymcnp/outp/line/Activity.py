import typing

import pandas

from ... import abc
from ..Line import Line


class Activity(Line, abc.symbol.WithDataIter):
    """
    Represents activity lines.

    Attributes:
        bin: line bin.
        count: line count.
        error: line error.
    """

    index: typing.Annotated[abc.Terminal, r'.{9}']
    cell: typing.Annotated[abc.Terminal, r'.{9}']
    tracks: typing.Annotated[abc.Terminal, r'.{12}']
    population: typing.Annotated[abc.Terminal, r'.{13}']
    collisions: typing.Annotated[abc.Terminal, r'.{13}']
    collisions_weight: typing.Annotated[abc.Terminal, r'.{14}']
    number: typing.Annotated[abc.Terminal, r'.{13}']
    flux: typing.Annotated[abc.Terminal, r'.{13}']
    average_weight: typing.Annotated[abc.Terminal, r'.{13}']
    average_mfp: typing.Annotated[abc.Terminal, r'.{13}']

    def to_dataframe_iter(self, returning: bool = False) -> typing.Generator[pandas.DataFrame, None, pandas.DataFrame | None]:
        """
        Generates pandas dataframes for values.

        Parameters:
            returning: Flag to/to not return.

        Yields:
            Pandas dataframes for values.

        Returns:
            Pandas dataframe for all values.
        """

        yield (
            frame := pandas.DataFrame(
                {
                    'index': [float(self.index)],
                    'cell': [float(self.cell)],
                    'tracks': [float(self.tracks)],
                    'population': [float(self.population)],
                    'collisions': [float(self.collisions)],
                    'collisions_weight': [float(self.collisions_weight)],
                    'number': [float(self.number)],
                    'flux': [float(self.flux)],
                    'average_weight': [float(self.average_weight)],
                    'average_mfp': [float(self.average_mfp)],
                }
            )
        )

        if returning:
            return frame
