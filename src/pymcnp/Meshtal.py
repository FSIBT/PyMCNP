import collections.abc
import pathlib
import typing

import pandas

from . import abc
from . import meshtal


class Meshtal(abc.file.WithMcnpIter, abc.file.WithDataIter, abc.File):
    """
    Represents meshtal files.

    Attributes:
        header: meshtal ``header`` item.
        title_preamble: meshtal ``r'\\n'`` symbol.
        title: meshtal ``title`` item.
        histories_preamble: meshtal ``r'\\n Number of histories used for normalizing tallies ='`` symbol.
        histories: meshtal ``histories`` item.
        number_preamble: meshtal ``r'\\n\\n Mesh Tally Number'`` symbol.
        number: meshtal ``number`` item.
        particles_preamble: meshtal ``r'\\n\\n '`` symbol.
        particle: meshtal ``particle`` item.
        particle_postamble: meshtal ``r' mesh tally\\.\\n\\n'`` symbol.
        bins: meshtal ``bins`` item.
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
    particle_postamble: typing.Annotated[abc.Terminal, r' +mesh tally\.\n\n']
    bins: meshtal.block.Bin
    blank: typing.Annotated[abc.Terminal, r'\n\n *']
    labels: typing.Annotated[abc.Array, meshtal.literal.Label, typing.Annotated[abc.Terminal, r' +']]
    labels_postamble: typing.Annotated[abc.Terminal, r'\n']
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
    def _from_mcnp_iter_at(cls, source: str, pos: int, returning: bool = False) -> typing.Generator[meshtal.line.Row, None, tuple[typing.Self | None, int]]:
        """
        Compiles source strings at positions into their corresponding meshtal files iteratively.

        Parameters:
            source: Source string to compile.
            pos: Position in ``source`` to compile at.
            returning: Flag to/to not build the meshtal file.

        Yields:
            Meshtal data rows, in order.

        Returns:
            Meshtal file corresponding to ``source`` at ``pos`` if ``returning`` (else ``None``), and the position where it ends.
        """

        header, pos = meshtal.line.Header._from_mcnp_at(source, pos)
        title_preamble, pos = _TITLE_PREAMBLE._from_mcnp_at(source, pos)
        title, pos = _TITLE._from_mcnp_at(source, pos)
        histories_preamble, pos = _HISTORIES_PREAMBLE._from_mcnp_at(source, pos)
        histories, pos = _HISTORIES._from_mcnp_at(source, pos)
        number_preamble, pos = _NUMBER_PREAMBLE._from_mcnp_at(source, pos)
        number, pos = _NUMBER._from_mcnp_at(source, pos)
        particles_preamble, pos = _PARTICLES_PREAMBLE._from_mcnp_at(source, pos)
        particle, pos = _PARTICLE._from_mcnp_at(source, pos)
        particle_postamble, pos = _PARTICLE_POSTAMBLE._from_mcnp_at(source, pos)
        bins, pos = meshtal.block.Bin._from_mcnp_at(source, pos)
        blank, pos = _BLANK._from_mcnp_at(source, pos)
        labels, pos = _LABELS._from_mcnp_at(source, pos)
        labels_postamble, pos = _LABELS_POSTAMBLE._from_mcnp_at(source, pos)

        spaces: list[abc.Terminal] = []
        if returning:
            items: list[abc.Symbol] = []

        while True:
            try:
                item, pos = meshtal.line.Row._from_mcnp_at(source, pos)
                yield item

                if returning:
                    items.append(item)
            except abc.Error:
                if spaces:
                    pos -= len(spaces.pop(-1))
                break

            try:
                space, pos = _ROW_SPACE._from_mcnp_at(source, pos)

                if returning:
                    spaces.append(space)
                else:
                    spaces = [space]
            except abc.Error:
                break

        if returning:
            rows = _ROWS(*items, spaces=spaces)

        end, pos = _END._from_mcnp_at(source, pos)

        if not returning:
            return None, pos

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
            particle_postamble=particle_postamble,
            bins=bins,
            blank=blank,
            labels=labels,
            labels_postamble=labels_postamble,
            rows=rows,
            end=end,
        ), pos

    if typing.TYPE_CHECKING:

        @classmethod
        def from_mcnp_iter(cls, source: str, returning: bool = False) -> typing.Generator[meshtal.line.Row, None, tuple[typing.Self, str] | None]: ...

        @classmethod
        def from_file_iter(cls, path: pathlib.Path | str, returning: bool = False) -> typing.Generator[meshtal.line.Row, None, tuple[typing.Self, str] | None]: ...

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
            UnicodeDecodeError: The file is not text, i.e., it holds a NUL byte, e.g., binary PTRAC, or is UTF-16.
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
        with abc._text.open_text(path) as file:
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

        return int(self.number)

    @property
    def nps(self) -> int:
        """
        Number of histories the mesh tally is normalized to, e.g., ``2000``; ``histories`` is the padded text of the file.
        """

        return int(float(self.histories))

    @property
    def particle_name(self) -> str:
        """
        Particle of the mesh tally, e.g., ``'neutron'``.
        """

        return str(str.__str__(self.particle))

    @property
    def names(self) -> list[str]:
        """
        Names of the data columns, e.g., ``['Time', 'X', 'Y', 'Z', 'Result', 'Rel Error']``.
        """

        return [str(str.__str__(label)) for label in self.labels]

    def to_dataframe_iter(self, returning: bool = False) -> typing.Generator[pandas.DataFrame, None, pandas.DataFrame | None]:
        """
        Generates pandas dataframes for meshtal files; a meshtal file holds one mesh tally, so this yields one dataframe.

        Parameters:
            returning: Flag to/to not return.

        Yields:
            Dataframe with one row per mesh bin. Energy and time columns hold floats, or strings (``'Total'`` included) if some row sums over all bins.

        Returns:
            The same dataframe if ``returning``.
        """

        names = self.names
        frame = pandas.DataFrame([[str(value) for value in row.values] for row in self.rows], columns=names)
        for name in names:
            if name not in ('Energy', 'Time') or (frame[name].str.lower() != 'total').all():
                frame[name] = frame[name].astype(float)

        yield frame

        if returning:
            return frame


_TITLE_PREAMBLE = abc.Terminal[r'\n']
_TITLE = abc.Terminal[r'.+']
_HISTORIES_PREAMBLE = abc.Terminal[r'\n Number of histories used for normalizing tallies =']
_HISTORIES = abc.Terminal[r'.{17}']
_NUMBER_PREAMBLE = abc.Terminal[r'\n\n Mesh Tally Number *']
_NUMBER = abc.Terminal[r'\d+']
_PARTICLES_PREAMBLE = abc.Terminal['\n ']
_PARTICLE = abc.Terminal[r'\S+']
_PARTICLE_POSTAMBLE = abc.Terminal[r' +mesh tally\.\n\n']
_BLANK = abc.Terminal[r'\n\n *']
_LABELS = abc.Array[meshtal.literal.Label, abc.Terminal[r' +']]
_LABELS_POSTAMBLE = abc.Terminal[r'\n']
_ROW_SPACE = abc.Terminal[r' *\n']
_ROWS = abc.Array[meshtal.line.Row, _ROW_SPACE]
_END = abc.Terminal[r'(?: *\n)?']
