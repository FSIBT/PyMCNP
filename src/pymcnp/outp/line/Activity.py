import typing

import pandas

from ... import abc
from ..Line import Line


class Activity(Line):
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

    def to_dataframe(self) -> pandas.DataFrame:
        """
        Generates pandas dataframes for activity lines.

        Returns:
            Pandas dataframe corresponding to ``self``.
        """

        return pandas.DataFrame(
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
