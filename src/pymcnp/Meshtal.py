import re
import typing
import pathlib
import collections.abc

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

    @staticmethod
    def iter_tallies(path: pathlib.Path | str) -> collections.abc.Iterator['Meshtal']:
        """
        Parses meshtal files with any number of mesh tallies, one tally at a time.

        Every tally is a `Meshtal` with the file's header, title and histories.
        `from_file` only reads the first tally of a file.

        Parameters:
            path: Path to meshtal file to read.

        Yields:
            One `Meshtal` per mesh tally, in file order.

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
        Mesh tally number, e.g., `4`.
        """

        return int(re.search(r'\d+', self.number)[0])  # ty: ignore[not-subscriptable]

    @property
    def particle_name(self) -> str:
        """
        Particle of the mesh tally, e.g., `'neutron'`.
        """

        return self.particle.split()[0]

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
