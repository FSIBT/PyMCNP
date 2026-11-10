import re
import typing
import pathlib
import collections.abc

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
    def from_mcnp(cls, source: str) -> tuple[typing.Self, str]:
        """
        Compiles source strings into their corresponding meshtal files.

        Parameters:
            source: Source string to compile.

        Returns:
            Meshtal file corresponding to ``source``.
        """

        generator = cls.from_mcnp_iter(source)
        while True:
            try:
                next(generator)
            except StopIteration as stop:
                return stop.value

    @classmethod
    def from_mcnp_iter(cls, source: str) -> typing.Generator[meshtal.line.Row, None, tuple[typing.Self, str]]:
        """
        Compiles source strings into their corresponding meshtal files iteratively.

        Parameters:
            source: Source string to compile.

        Yields:
            Meshtal data rows, in order.

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

        # Rows are parsed one line at a time, on short strings, since the generic parser copies the rest of the source for every symbol.
        spaces: list[abc.Terminal] = []
        items: list[abc.Symbol] = []
        separator = None
        position = 0
        end_of_rows = 0
        while True:
            newline = source.find('\n', position)
            stop = len(source) if newline < 0 else newline
            try:
                item, rest = meshtal.line.Row.from_mcnp(source[position:stop])
            except abc.Error:
                break
            if rest.strip(' '):
                break

            if separator is not None:
                spaces.append(separator)
            items.append(item)
            yield item
            end_of_rows = stop - len(rest)

            if newline < 0:
                break
            separator = abc.Terminal[r' *\n'](rest + '\n')
            position = newline + 1

        source = source[end_of_rows:]
        rows = cls._fields['rows'][0](*items, spaces=spaces)
        end, source = abc.Terminal[r'(?: *\n)?'].from_mcnp(source)

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
    def from_file_iter(cls, path: pathlib.Path | str) -> typing.Generator[meshtal.line.Row, None, tuple[typing.Self, str]]:
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

    @staticmethod
    def iter_tallies(path: pathlib.Path | str) -> collections.abc.Iterator['Meshtal']:
        """
        Parses meshtal files with any number of mesh tallies, one tally at a time.

        Every tally is a ``Meshtal`` with the file's header, title and histories.
        ``from_file`` only reads the first tally of a file.

        Parameters:
            path: Path to meshtal file to read.

        Yields:
            One ``Meshtal`` per mesh tally, in file order.

        Raises:
            Error: File not found.
            Error: Expected mesh tally.
        """

        path = pathlib.Path(path)
        if not path.is_file():
            raise abc.Error('File not found.', f'{path=}')

        def parse(head: list[str], body: list[str]) -> Meshtal:
            while body and body[-1].strip() == '':
                body.pop()
            text = ''.join(head + body)
            if not text.endswith('\n'):
                text += '\n'
            tally, remainder = Meshtal.from_mcnp(text)
            if remainder != '':
                raise abc.Error('Expected mesh tally.', f'{remainder[:80]!r}')
            return tally

        head: list[str] = []
        body: list[str] = []
        found = False
        with path.open() as file:
            for line in file:
                if line.startswith(' Mesh Tally Number'):
                    if found:
                        yield parse(head, body)
                        body = []
                    found = True
                if found:
                    body.append(line)
                else:
                    head.append(line)

        if not found:
            raise abc.Error('Expected mesh tally.', f'{path=}')
        yield parse(head, body)

    @property
    def tally_number(self) -> int:
        """
        Mesh tally number, e.g., ``4``.
        """

        return int(re.search(r'\d+', self.number)[0])  # ty: ignore[not-subscriptable]

    @property
    def particle_name(self) -> str:
        """
        Particle of the mesh tally, e.g., ``'neutron'``.
        """

        return self.particle.split()[0]

    @property
    def names(self) -> list[str]:
        """
        Names of the data columns, e.g., ``['Time', 'X', 'Y', 'Z', 'Result', 'Rel Error']``.
        """

        return re.findall(r'Energy|Time|X|Y|Z|Result|Rel Error', self.labels)

    def to_dataframe_iter(self) -> typing.Iterator[pandas.DataFrame]:
        """
        Generates pandas dataframes from meshtal files; a meshtal file holds one mesh tally, so this yields one dataframe.

        Yields:
            Dataframe with one row per mesh bin. Energy and time columns hold floats, or ``'Total'`` where the row sums over all bins.
        """

        names = self.names
        frame = pandas.DataFrame([[str(value) for value in row.values] for row in self.rows], columns=names)
        for name in names:
            if name not in ('Energy', 'Time') or (frame[name].str.lower() != 'total').all():
                frame[name] = frame[name].astype(float)

        yield frame
