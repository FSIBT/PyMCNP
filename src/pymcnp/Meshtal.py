import typing

import pandas

from . import abc
from . import meshtal


class Meshtal(abc.file.WithMcnpIter, abc.file.WithDataIter, abc.File):
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
    number_preamble: typing.Annotated[abc.Terminal, r'\n\n Mesh Tally Number *']
    number: typing.Annotated[abc.Terminal, r'\d+']
    particles_preamble: typing.Annotated[abc.Terminal, '\n ']
    particle: typing.Annotated[abc.Terminal, r'\S+']
    particle_postable: typing.Annotated[abc.Terminal, r' +mesh tally\.\n\n']
    bins: meshtal.block.Bin
    blank: typing.Annotated[abc.Terminal, r'\n\n *']
    labels: typing.Annotated[abc.Array, meshtal.literal.Label, typing.Annotated[abc.Terminal, r' +']]
    labels_postable: typing.Annotated[abc.Terminal, r'\n']
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

        for row in self.rows:
            if len(row.values) != len(self.labels):
                raise abc.Error('Invalid value.', f'\n{row=}\n{self.labels=}')

            for label, value in zip(self.labels, row.values):
                if label not in ('Energy', 'Time') and value.lower() == 'total':
                    raise abc.Error('Invalid value.', f'\n{row=}\n{self.labels=}')

    @classmethod
    def from_mcnp_iter(cls, source: str, returning: bool = False) -> typing.Generator[tuple[meshtal.line.Row, str], None, tuple[typing.Self, str] | None]:
        """
        Compiles source strings into their corresponding meshtal files iteratively.

        Parameters:
            source: Source string to compile.
            returning: Flag to/to not return.

        Yields:
            Meshtal data rows, in order.

        Returns:
            Meshtal file corresponding to `source` if `returning`.
        """

        header, source = meshtal.line.Header.from_mcnp(source)
        title_preamble, source = abc.Terminal[r'\n'].from_mcnp(source)
        title, source = abc.Terminal[r'.+'].from_mcnp(source)
        histories_preamble, source = abc.Terminal[r'\n Number of histories used for normalizing tallies ='].from_mcnp(source)
        histories, source = abc.Terminal[r'.{17}'].from_mcnp(source)
        number_preamble, source = abc.Terminal[r'\n\n Mesh Tally Number *'].from_mcnp(source)
        number, source = abc.Terminal[r'\d+'].from_mcnp(source)
        particles_preamble, source = abc.Terminal['\n '].from_mcnp(source)
        particle, source = abc.Terminal[r'\S+'].from_mcnp(source)
        particle_postable, source = abc.Terminal[r' +mesh tally\.\n\n'].from_mcnp(source)
        bins, source = meshtal.block.Bin.from_mcnp(source)
        blank, source = abc.Terminal[r'\n\n *'].from_mcnp(source)
        labels, source = abc.Array[meshtal.literal.Label, abc.Terminal[r' +']].from_mcnp(source)
        labels_postable, source = abc.Terminal[r'\n'].from_mcnp(source)

        spaces: list[abc.Terminal] = []
        if returning:
            items: list[abc.Symbol] = []

        while True:
            try:
                item, source = meshtal.line.Row.from_mcnp(source)
                yield item, source

                if returning:
                    items.append(item)
            except abc.Error:
                if spaces:
                    source = spaces.pop(-1).to_mcnp() + source
                break

            try:
                space, source = abc.Terminal[r' *\n'].from_mcnp(source)

                if returning:
                    spaces.append(space)
                else:
                    spaces = [space]
            except abc.Error:
                break

        if returning:
            rows = abc.Array[meshtal.line.Row, abc.Terminal[r' *\n']](*items, spaces=spaces)

        end, source = abc.Terminal[r'(?: *\n)?'].from_mcnp(source)

        if returning:
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
                labels_postable=labels_postable,
                rows=rows,
                end=end,
            ), source

    def to_dataframe_iter(self, returning: bool = False) -> typing.Generator[pandas.DataFrame, None, pandas.DataFrame | None]:
        """
        Generates pandas dataframes for rows.

        Parameters:
            returning: Flag to/to not return.

        Yields:
            Pandas dataframes for rows.

        Returns:
            Pandas dataframe for all rows.
        """

        if returning:
            frames = []

        for row in self.rows:
            frame = row.to_dataframe()
            frame.columns = self.labels
            yield frame

            if returning:
                frames.append(frame)

        if returning:
            return pandas.concat(frames, ignore_index=True)
