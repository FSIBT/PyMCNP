import re
import typing

import pandas

from . import abc
from . import outp


class Outp(abc.file.WithDataIter, abc.File):
    """
    Represents output files.

    Attributes:
        header: outp header.
        blocks: outp blocks.
        footer: outp footer, empty if MCNP stopped early, e.g., with ``bad trouble``.
    """

    header: outp.Header
    blocks: typing.Annotated[abc.Array, outp.Block, abc.Terminal[r'']]
    footer: outp.Footer | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    @property
    def version(self) -> str:
        """
        Outp file version.
        """

        return self.header.version

    @property
    def nps(self) -> str | None:
        """
        Output file nps, ``None`` without footer.
        """

        return self.footer.nps if isinstance(self.footer, outp.Footer) else None

    @property
    def run_time(self) -> str | None:
        """
        Output file run time, ``None`` without footer.
        """

        return self.footer.run_time if isinstance(self.footer, outp.Footer) else None

    @property
    def terminated(self) -> str | None:
        """
        Output file terminated, ``None`` without footer.
        """

        return self.footer.terminated if isinstance(self.footer, outp.Footer) else None

    @property
    def warnings(self) -> str | None:
        """
        Output file warnings, ``None`` without footer.
        """

        return self.footer.warnings if isinstance(self.footer, outp.Footer) else None

    def activities(self, kind: type[outp.block.Activity] = outp.block.Activity) -> tuple[outp.block.Activity, ...]:
        """
        Gets output file activity blocks.

        Parameters:
            kind: Activity block type to get.

        Returns:
            Activity blocks of kind ``kind``.
        """

        every = self.blocks.filter(kind)

        return tuple(every)

    def tallies(self, number: abc.Terminal | str | None = None, kind: type[outp.block.Tally] = outp.block.Tally) -> tuple[outp.block.Tally, ...]:
        """
        Gets output file tally blocks.

        Parameters:
            number: Tally block number to get.
            kind: Tally block type to get.

        Returns:
            Tally blocks of number ``number``, if specificed, and kind ``kind``.
        """

        every = self.blocks.filter(kind)

        number_matches = every

        if number is not None:
            number = abc.Terminal[r'.{8}'](str(number).rjust(8))
            number_matches = self.blocks.filter(kind, number=number)

        return tuple(number_matches)

    @property
    def fatal_errors(self) -> list[str]:
        """
        Fatal errors MCNP reported, e.g., ``surface -7 not found for cell 2 card.``.

        Returns:
            Messages of fatal errors, empty if the run did not fail.
        """

        return _fatal_errors(self.to_mcnp())

    @property
    def summary(self) -> outp.Summary:
        """
        Headline results: version, histories, run time, termination, ``keff``, fatal errors, warnings and the statistical checks of each tally.

        Returns:
            Summary of the output file, with ``None`` for values the output does not contain.
        """

        text = self.to_mcnp()

        return outp.Summary.from_text(text, _fatal_errors(text))

    def activity(self, particle: str) -> pandas.DataFrame:
        """
        Generates a dataframe from the activity table of a particle (print table 126).

        Parameters:
            particle: ``'neutron'`` or ``'photon'``.

        Returns:
            Dataframe with one row per cell (columns ``cell``, ``tracks`` entering, ``population``, ``collisions``, ...) and a final row for the totals.

        Raises:
            Error: Unknown particle or the output has no such table.
        """

        kinds = {'neutron': outp.block.NeutronActivity, 'photon': outp.block.PhotonActivity}
        if particle not in kinds:
            raise abc.Error('Invalid value.', f'{particle=}, expected one of {sorted(kinds)}')

        for block in self.blocks.filter(kinds[particle]):
            rows = []
            for row in block.table_body:
                fields = row.to_mcnp().split()
                rows.append([int(fields[1]), int(fields[2]), int(fields[3]), int(fields[4]), *map(float, fields[5:])])

            frame = pandas.DataFrame(rows, columns=list(_ACTIVITY_COLUMNS))
            total = pandas.DataFrame(
                [
                    {
                        'cell': None,
                        'tracks': int(block.table_total_tracks),
                        'population': int(block.table_total_population),
                        'collisions': int(block.table_total_collisions),
                        'collisions_weighted': float(block.table_total_weighted_collisions),
                    }
                ],
                columns=list(_ACTIVITY_COLUMNS),
            )
            frame = pandas.concat([frame, total], ignore_index=True) if rows else total
            frame['cell'] = frame['cell'].astype('Int64')

            return frame

        raise abc.Error('Missing table.', f'no {particle} activity table (print table 126) in this output')

    def tally(self, number: int | str) -> pandas.DataFrame:
        """
        Generates a dataframe with typed columns for one tally.

        Columns: ``bins``, ``counts``, ``errors`` (floats, ``counts`` is the result and ``errors`` its relative error), the cell, surface and angle columns the tally has
        (``cell``, ``surface`` and ``facet`` are integers, ``angle_from`` and ``angle_to`` floats), then ``number``, ``quantity``, ``particles`` and ``nps``.

        Parameters:
            number: Tally number, e.g., ``4`` or ``'4'``.

        Returns:
            Dataframe with one row per tally bin.

        Raises:
            Error: Tally not found.
        """

        frames = {str(frame['number'].iloc[0]).strip(): frame for frame in self.to_dataframe_iter() if not frame.empty}
        key = str(number).strip()
        if key not in frames:
            raise abc.Error('Tally not found.', f'{number=}, expected one of {sorted(frames, key=int)}')

        frame = frames[key].copy()
        frame['number'] = int(key)
        frame['quantity'] = frame.pop('type').map(_quantity)
        frame['nps'] = frame['nps'].astype(int)
        if 'cell_number' in frame:
            frame['cell'] = _integers(frame.pop('cell_number'))
        if 'surface_number' in frame:
            surface = frame.pop('surface_number').map(_surface)
            frame['surface'] = pandas.array([value[0] for value in surface], dtype='Int64')
            frame['facet'] = pandas.array([value[1] for value in surface], dtype='Int64')
        for column in ('angle_from', 'angle_to'):
            if column in frame:
                frame[column] = frame[column].astype(float)

        leading = [column for column in frame.columns if column not in ('bins', 'counts', 'errors', 'number', 'quantity', 'particles', 'nps')]

        return frame[['bins', 'counts', 'errors', *leading, 'number', 'quantity', 'particles', 'nps']]

    def to_dataframe_iter(self, returning: bool = False) -> typing.Generator[pandas.DataFrame, None, pandas.DataFrame | None]:
        """
        Generates pandas dataframes for tallies.

        Parameters:
            returning: Flag to/to not return.

        Yields:
            Pandas dataframes for tallies.

        Returns:
            Pandas dataframe for all tallies.
        """

        if tallies := self.blocks.filter(outp.block.Tally):
            if returning:
                frames = []

            for tally in tallies:
                yield (frame := tally.to_dataframe())

                if returning:
                    frames.append(frame)

            if returning:
                return pandas.concat(frames, ignore_index=True)
        else:
            if returning:
                return pandas.DataFrame()


_ACTIVITY_COLUMNS = (
    'cell',
    'tracks',
    'population',
    'collisions',
    'collisions_weighted',
    'number_weighted_energy',
    'flux_weighted_energy',
    'average_track_weight',
    'average_track_mfp',
)

_REGEX_FATAL = re.compile(r'^ *(?:fatal error|bad trouble)\.? +(.*\S)', re.IGNORECASE | re.MULTILINE)


def _fatal_errors(text: str) -> list[str]:
    return [match[1] for match in _REGEX_FATAL.finditer(text)]


def _quantity(text: str) -> str:
    text = re.sub(r'^\s*\d+\s+', '', text.strip())
    return re.split(r'\s+units\s', text, maxsplit=1)[0].strip()


def _integers(column: pandas.Series) -> pandas.Series:
    return pandas.to_numeric(column.str.strip(), errors='coerce').astype('Int64')


def _surface(text: str) -> tuple[int | None, int | None]:
    whole, _, facet = text.strip().partition('.')
    try:
        return int(whole), int(facet) if facet else 0
    except ValueError:
        return None, None
