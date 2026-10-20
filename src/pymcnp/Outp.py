import re
import typing

import pandas

from . import abc
from . import outp

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


class Outp(abc.File):
    """
    Represents output files.

    Attributes:
        header: outp `header` parameter.
        blocks: outp `blocks` parameter.
    """

    header: typing.Annotated[
        abc.Terminal,
        r'(?:          Code Name & Version = MCNP6, 1\.0\n  \n     _/      _/        _/_/_/       _/      _/       _/_/_/         _/_/_/\n    _/_/  _/_/      _/             _/_/    _/       _/    _/     _/       \n   _/  _/  _/      _/             _/  _/  _/       _/_/_/       _/_/_/    \n  _/      _/      _/             _/    _/_/       _/           _/    _/   \n _/      _/        _/_/_/       _/      _/       _/             _/_/      \n  \n  \+---------------------------------------------------------------------\+\n  \| Copyright 2008\. Los Alamos National Security, LLC\.  All rights      \|\n  \| reserved\.                                                           \|\n  \|   This material was produced under U\.S\. Government contract         \|\n  \| DE-AC52-06NA25396 for Los Alamos National Laboratory, which is      \|\n  \| operated by Los Alamos National Security, LLC, for the U\.S\.         \|\n  \| Department of Energy\. The Government is granted for itself and      \|\n  \| others acting on its behalf a paid-up, nonexclusive, irrevocable    \|\n  \| worldwide license in this material to reproduce, prepare derivative \|\n  \| works, and perform publicly and display publicly\. Beginning five    \|\n  \| \(5\) years after 2008, subject to additional five-year worldwide     \|\n  \| renewals, the Government is granted for itself and others acting on \|\n  \| its behalf a paid-up, nonexclusive, irrevocable worldwide license   \|\n  \| in this material to reproduce, prepare derivative works, distribute \|\n  \| copies to the public, perform publicly and display publicly, and to \|\n  \| permit others to do so\. NEITHER THE UNITED STATES NOR THE UNITED    \|\n  \| STATES DEPARTMENT OF ENERGY, NOR LOS ALAMOS NATIONAL SECURITY, LLC, \|\n  \| NOR ANY OF THEIR EMPLOYEES, MAKES ANY WARRANTY, EXPRESS OR IMPLIED, \|\n  \| OR ASSUMES ANY LEGAL LIABILITY OR RESPONSIBILITY FOR THE ACCURACY,  \|\n  \| COMPLETENESS, OR USEFULNESS OF ANY INFORMATION, APPARATUS, PRODUCT, \|\n  \| OR PROCESS DISCLOSED, OR REPRESENTS THAT ITS USE WOULD NOT INFRINGE \|\n  \| PRIVATELY OWNED RIGHTS\.                                             \|\n  \+---------------------------------------------------------------------\+\n  \n)|(?:          Code Name & Version = MCNP_6\.20, 6\.2\.0\n  \n     _/      _/        _/_/_/       _/      _/       _/_/_/         _/_/_/ \n    _/_/  _/_/      _/             _/_/    _/       _/    _/     _/        \n   _/  _/  _/      _/             _/  _/  _/       _/_/_/       _/_/_/     \n  _/      _/      _/             _/    _/_/       _/           _/    _/    \n _/      _/        _/_/_/       _/      _/       _/             _/_/       \n  \n  \+-----------------------------------------------------------------------\+\n  \| Copyright \(2018\)\.  Los Alamos National Security, LLC\.  All rights     !\n  \| reserved\.                                                             !\n  \|  This material was produced under U\.S\. Government contract            !\n  \| DE-AC52-06NA25396 for Los Alamos National Laboratory, which is        !\n  \| operated by Los Alamos National Security, LLC for the U.S\.            !\n  \| Department of Energy\. The Government is granted for itself and        !\n  \| others acting on its behalf a paid-up, nonexclusive, irrevocable      !\n  \| worldwide license in this material to reproduce, prepare derivative   !\n  \| works, and perform publicly and display publicly\. Beginning five \(5\)  !\n  \| years after February 14, 2018, subject to additional five-year        !\n  \| worldwide renewals, the Government is granted for itself and others   !\n  \| acting on its behalf a paid-up, nonexclusive, irrevocable worldwide   !\n  \| license in this material to reproduce, prepare derivative works,      !\n  \| distribute copies to the public, perform publicly and display         !\n  \| publicly, and to permit others to do so\. NEITHER THE UNITED STATES    !\n  \| NOR THE UNITED STATES DEPARTMENT OF ENERGY, NOR LOS ALAMOS NATIONAL   !\n  \| SECURITY, LLC, NOR ANY OF THEIR EMPLOYEES, MAKES ANY WARRANTY,        !\n  \| EXPRESS OR IMPLIED, OR ASSUMES ANY LEGAL LIABILITY OR RESPONSIBILITY  !\n  \| FOR THE ACCURACY, COMPLETENESS, OR USEFULNESS OF ANY INFORMATION,     !\n  \| APPARATUS, PRODUCT, OR PROCESS DISCLOSED, OR REPRESENTS THAT ITS USE  !\n  \| WOULD NOT INFRINGE PRIVATELY OWNED RIGHTS\.                            !\n  \+-----------------------------------------------------------------------\+\n  \n)',
    ]
    blocks: typing.Annotated[abc.Array, outp.Block, abc.Terminal[r'']] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    @property
    def fatal_errors(self) -> list[str]:
        """
        Fatal errors MCNP reported, e.g., `surface -7 not found for cell 2 card.`.

        Returns:
            Messages of fatal errors, empty if the run did not fail.
        """

        return _fatal_errors(self.to_mcnp())

    @property
    def summary(self) -> outp.Summary:
        """
        Headline results: version, histories, run time, termination, `keff`, fatal errors, warnings and the statistical checks of each tally.

        Returns:
            Summary of the output file, with `None` for values the output does not contain.
        """

        text = self.to_mcnp()
        return outp.Summary.from_text(text, _fatal_errors(text))

    def activity(self, particle: str) -> pandas.DataFrame:
        """
        Generates a dataframe from the activity table of a particle (print table 126).

        Parameters:
            particle: `'neutron'` or `'photon'`.

        Returns:
            Dataframe with one row per cell (columns `cell`, `tracks` entering, `population`, `collisions`, ...) and a final row for the totals.

        Raises:
            Error: Unknown particle or the output has no such table.
        """

        kinds = {'neutron': outp.block.NeutronActivity, 'photon': outp.block.PhotonActivity}
        if particle not in kinds:
            raise abc.Error('Invalid value.', f'{particle=}, expected one of {sorted(kinds)}')

        for block in self.blocks:
            if isinstance(block, kinds[particle]):
                return block.to_dataframe()

        raise abc.Error('Missing table.', f'no {particle} activity table (print table 126) in this output')

    def tallies(self) -> pandas.DataFrame:
        """
        Lists the tallies of the output.

        Returns:
            Dataframe with one row per tally: `number` (int), `quantity` (MCNP's description, e.g., `'number of particles crossing a surface.'`), `particles`, `nps`, `bins` (number of result rows), and `checks_passed` (`None` if the output has no statistical checks for it).
        """

        checks = self.summary.checks
        rows = []
        for number, frame in self.to_dataframe().items():
            if frame.empty:
                continue
            first = frame.iloc[0]
            rows.append(
                {
                    'number': int(number),
                    'quantity': _quantity(first['type']),
                    'particles': first['particles'],
                    'nps': int(first['nps']),
                    'bins': len(frame),
                    'checks_passed': checks[int(number)].passed if int(number) in checks else None,
                }
            )

        frame = pandas.DataFrame(rows, columns=['number', 'quantity', 'particles', 'nps', 'bins', 'checks_passed'])
        return frame.astype({'number': 'Int64', 'nps': 'Int64', 'bins': 'Int64', 'checks_passed': 'boolean'})

    def tally(self, number: int | str) -> pandas.DataFrame:
        """
        Generates a dataframe with typed columns for one tally.

        Columns: `bins`, `counts`, `errors` (floats, `counts` is the result and `errors` its relative error), the cell, surface and angle columns the tally has
        (`cell`, `surface` and `facet` are integers, `angle_from` and `angle_to` floats), then `number`, `quantity`, `particles` and `nps`.

        Parameters:
            number: Tally number, e.g., `4` or `'4'`.

        Returns:
            Dataframe with one row per tally bin.

        Raises:
            Error: Tally not found.
        """

        frames = self.to_dataframe()
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

    def to_dataframe(self) -> dict[str, pandas.DataFrame]:
        """
        Generates pandas dataframes from output files.

        Returns:
            Tuple of corresponding pandas dataframes.
        """

        tallies = {}

        for block in self.blocks:
            if isinstance(block, outp.block.Tally):
                assert hasattr(block, 'number')
                assert isinstance(block.number, str)
                tallies[block.number.strip()] = block.to_dataframe()

        return tallies
