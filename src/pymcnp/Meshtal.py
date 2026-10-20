import re
import typing

import pandas

from . import abc
from . import meshtal


class Meshtal(abc.File):
    """
    Represents meshtal files.

    Attributes:
        header: meshtal `header` parameter.
        title: meshtal `title` parameter.
        histories: meshtal `histories` parameter.
        number: meshtal `number` parameter.
        particle: meshtal `particle` parameter.
        bins: meshtal `bins` parameter.
        blank: meshtal blank line before the data.
        labels: meshtal data column labels.
        rows: meshtal data rows.
        end: meshtal final newline.
    """

    header: meshtal.line.Header
    title: typing.Annotated[abc.Terminal, r'\n.+?\n']
    histories: typing.Annotated[abc.Terminal, r' Number of histories used for normalizing tallies =.{17}\n\n']
    number: typing.Annotated[abc.Terminal, r' Mesh Tally Number.{10}\n']
    particle: typing.Annotated[abc.Terminal, r' .{8} mesh tally\.\n\n']
    bins: meshtal.block.Bin
    blank: typing.Annotated[abc.Terminal, r'\n\n']
    labels: typing.Annotated[abc.Terminal, r' *(?:Energy +)?(?:Time +)?X +Y +Z +Result +Rel Error\n']
    rows: typing.Annotated[abc.Array, meshtal.line.Row, typing.Annotated[abc.Terminal, r' *\n']]
    end: typing.Annotated[abc.Terminal, r'(?: *\n)?']

    def __post_init__(self) -> None:
        """
        Validates meshtal files.

        Raises:
            Error: Invalid value.
        """

        names = self.names
        if len(self.rows) == 0:
            raise abc.Error('Invalid value.', f'{self.rows=}')

        width = len(names)
        for row in self.rows:
            if len(row.values) != width:
                raise abc.Error('Invalid value.', f'{row=}\n{names=}')

            for name, value in zip(names, row.values):
                if name not in ('Energy', 'Time') and value.lower() == 'total':
                    raise abc.Error('Invalid value.', f'{row=}\n{name=}')

    @property
    def names(self) -> list[str]:
        """
        Names of the data columns, e.g., `['Time', 'X', 'Y', 'Z', 'Result', 'Rel Error']`.
        """

        return re.findall(r'Energy|Time|X|Y|Z|Result|Rel Error', self.labels)

    def to_dataframe(self) -> pandas.DataFrame:
        """
        Collects the data rows into a dataframe.

        Returns:
            Dataframe with one row per mesh bin. Energy and time columns hold floats, or `'Total'` where the row sums over all bins.
        """

        names = self.names
        frame = pandas.DataFrame([[str(value) for value in row.values] for row in self.rows], columns=names)
        for name in names:
            if name not in ('Energy', 'Time') or (frame[name].str.lower() != 'total').all():
                frame[name] = frame[name].astype(float)

        return frame
