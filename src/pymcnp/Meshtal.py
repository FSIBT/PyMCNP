import re
import typing
import pathlib

import pandas

from . import abc
from . import meshtal


class Meshtal(abc.DataFile):
    """
    Represents meshtal files.

    Attributes:
        header: meshtal `header` item.
        title_preamble: meshtal `r'\\n'` symbol.
        title: meshtal `title` item.
        histories_preamble: meshtal `r'\\n Number of histories used for normalizing tallies ='` symbol.
        histories: meshtal `histories` item.
        number_preamble: meshtal `r'\\n\\n Mesh Tally Number'` symbol.
        number: meshtal `number` item.
        particles_preamble: meshtal `r'\\n\\n '` symbol.
        particle: meshtal `particle` item.
        particle_postable: meshtal `r' mesh tally\\.\\n\\n'` symbol.
        bins: meshtal `bins` item.
        blank: meshtal blank line before the data.
        labels: meshtal data column labels.
        rows: meshtal data rows.
        end: meshtal final newline.
    """

    header: meshtal.line.Header
    title_preamble: typing.Annotated[abc.Terminal, r'\n']
    title: typing.Annotated[abc.Terminal, r'.+']
    histories_preamble: typing.Annotated[abc.Terminal, r'\n Number of histories used for normalizing tallies =']
    histories: typing.Annotated[abc.Terminal, r'.{17}']
    number_preamble: typing.Annotated[abc.Terminal, r'\n\n Mesh Tally Number']
    number: typing.Annotated[abc.Terminal, r'.{10}']
    particles_preamble: typing.Annotated[abc.Terminal, '\n ']
    particle: typing.Annotated[abc.Terminal, r'.{8}']
    particle_postable: typing.Annotated[abc.Terminal, r' mesh tally\.\n\n']
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

        if len(self.rows) == 0:
            raise abc.Error('Invalid value.', f'{self.rows=}')

        labels = re.findall(r'Energy|Time|X|Y|Z|Result|Rel Error', self.labels)
        for row in self.rows:
            if len(row.values) != len(labels):
                raise abc.Error('Invalid value.', f'\n{row=}\n{self.labels=}')

            for label, value in zip(labels, row.values):
                if label not in ('Energy', 'Time') and value.lower() == 'total':
                    raise abc.Error('Invalid value.', f'\n{row=}\n{self.labels=}')

    @classmethod
    def from_mcnp_iter(cls, source: str) -> typing.Generator[tuple[meshtal.line.Row, str], None, tuple[typing.Self, str]]:
        """
        Compiles source strings into their corresponding meshtal files iteratively.

        Parameters:
            source: Source string to compile.

        Yields:
            Meshtal data row corresponding to `source`.

        Returns:
            Meshtal file corresponding to `source`.
        """

        header, source = meshtal.line.Header.from_mcnp(source)
        title_preamble, source = abc.Terminal[r'\n'].from_mcnp(source)
        title, source = abc.Terminal[r'.+'].from_mcnp(source)
        histories_preamble, source = abc.Terminal[r'\n Number of histories used for normalizing tallies ='].from_mcnp(source)
        histories, source = abc.Terminal[r'.{17}'].from_mcnp(source)
        number_preamble, source = abc.Terminal[r'\n\n Mesh Tally Number'].from_mcnp(source)
        number, source = abc.Terminal[r'.{10}'].from_mcnp(source)
        particles_preamble, source = abc.Terminal['\n '].from_mcnp(source)
        particle, source = abc.Terminal[r'.{8}'].from_mcnp(source)
        particle_postable, source = abc.Terminal[r' mesh tally\.\n\n'].from_mcnp(source)
        bins, source = meshtal.block.Bin.from_mcnp(source)
        blank, source = abc.Terminal[r'\n\n'].from_mcnp(source)
        labels, source = abc.Terminal[r' *(?:Energy +)?(?:Time +)?X +Y +Z +Result +Rel Error\n'].from_mcnp(source)

        spaces: list[abc.Terminal] = []
        items: list[abc.Symbol] = []
        while True:
            try:
                item, source = meshtal.line.Row.from_mcnp(source)
                yield item, source
                items.append(item)
            except abc.Error:
                if spaces:
                    source = spaces.pop(-1).to_mcnp() + source
                break

            try:
                space, source = abc.Terminal[r' *\n'].from_mcnp(source)
                spaces.append(space)
            except abc.Error:
                break

        rows = cls._fields['rows'][0](*items, spaces=spaces)
        end, source = abc.Terminal.from_mcnp(r'(?: *\n)?')

        return cls(
            header=header,
            title_preamble=title_preamble,
            title=title,
            histories_preamble=histories_preamble,
            histories=histories,
            number_preamble=number_preamble,
            number=number,
            particles_preamble=particles_preamble,
            particle=particle,
            particle_postable=particle_postable,
            bins=bins,
            blank=blank,
            labels=labels,
            rows=rows,
            end=end,
        ), source

    @classmethod
    def from_file_iter(cls, path: pathlib.Path | str) -> typing.Generator[tuple[meshtal.line.Row, str], None, tuple[typing.Self, str]]:
        """
        Compiles files into their corresponding meshtal files iteratively.

        Parameters:
            path: Path to file to compile.

        Yields:
            Meshtal data row corresponding to file at `path`.

        Returns:
            Meshtal file corresponding to file at `path`.

        Raises:
            Error: File not found.
        """

        path = pathlib.Path(path)

        if not path.is_file():
            raise abc.Error('File not found.', f'{path=}')

        source = path.read_text()

        return cls.from_mcnp_iter(source)

    def to_dataframe(self) -> pandas.DataFrame:
        """
        Generates pandas dataframes from meshtal files.

        Yields:
            Pandas dataframes concatenated into the returned dataframe.

        Returns:
            Pandas dataframe corresponding to ``self``.
        """

        names = re.findall(r'Energy|Time|X|Y|Z|Result|Rel Error', self.labels)

        if not self.rows:
            return pandas.DataFrame()
        else:
            frame = pandas.concat((row.to_dataframe() for row in self.rows), ignore_index=True)
            frame.columns = names
            return frame

    def to_dataframe_iter(self) -> typing.Generator[pandas.DataFrame, None, pandas.DataFrame]:
        """
        Generates pandas dataframes from meshtal files iteratively.

        Returns:
            Pandas dataframe corresponding to ``self``.
        """

        names = re.findall(r'Energy|Time|X|Y|Z|Result|Rel Error', self.labels)

        if not self.rows:
            return pandas.DataFrame()

        frames = []
        for row in self.rows:
            frame = row.to_dataframe()
            frame.columns = names
            yield frame
            frames.append(frame)

        return pandas.concat(frames, ignore_index=True)
