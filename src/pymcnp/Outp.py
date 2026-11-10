import re
import typing

import pandas

from . import abc
from . import outp


class Outp(abc.DataFile):
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
        outp version.
        """

        return self.header.version

    @property
    def nps(self) -> str | None:
        """
        outp nps, ``None`` without footer.
        """

        return self.footer.nps if isinstance(self.footer, outp.Footer) else None

    @property
    def run_time(self) -> str | None:
        """
        outp run_time, ``None`` without footer.
        """

        return self.footer.run_time if isinstance(self.footer, outp.Footer) else None

    @property
    def terminated(self) -> str | None:
        """
        outp terminated, ``None`` without footer.
        """

        return self.footer.terminated if isinstance(self.footer, outp.Footer) else None

    @property
    def warnings(self) -> str | None:
        """
        outp warnings, ``None`` without footer.
        """

        return self.footer.warnings if isinstance(self.footer, outp.Footer) else None

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
            return block.to_dataframe()

        raise abc.Error('Missing table.', f'no {particle} activity table (print table 126) in this output')

    def tallies(self) -> pandas.DataFrame:
        """
        Lists the tallies of the output.

        Returns:
            Dataframe with one row per tally: ``number`` (int), ``quantity`` (MCNP's description, e.g., ``'number of particles crossing a surface.'``), ``particles``, ``nps``, ``bins`` (number of result rows), and ``checks_passed`` (``None`` if the output has no statistical checks for it).
        """

        checks = self.summary.checks
        rows = []
        for frame in self.to_dataframe_iter():
            if frame.empty:
                continue
            first = frame.iloc[0]
            number = int(first['number'])
            rows.append(
                {
                    'number': number,
                    'quantity': _quantity(first['type']),
                    'particles': first['particles'],
                    'nps': int(first['nps']),
                    'bins': len(frame),
                    'checks_passed': checks[number].passed if number in checks else None,
                }
            )

        frame = pandas.DataFrame(rows, columns=['number', 'quantity', 'particles', 'nps', 'bins', 'checks_passed'])

        return frame.astype({'number': 'Int64', 'nps': 'Int64', 'bins': 'Int64', 'checks_passed': 'boolean'})

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

    def to_dataframe_iter(self) -> typing.Iterator[pandas.DataFrame]:
        """
        Generates pandas dataframes from output files, one tally at a time.

        Yields:
            Pandas dataframe for each tally, with the tally ``number``, ``type``, ``particles`` and ``nps`` as columns.
        """

        for tally in self.blocks.filter(outp.block.Tally):
            yield tally.to_dataframe()


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
