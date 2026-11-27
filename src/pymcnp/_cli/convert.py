"""
Usage:
    pymcnp convert outp (--csv | --parquet) <file>
    pymcnp convert ptrac (--csv | --parquet) <file>
    pymcnp convert meshtal (--csv | --parquet) <file>

Options:
    -c --csv        Write CSV.
    -p --parquet    Write PARQUET.

Writes the data of OUTP (all tallies), PTRAC (one row per event), or
MESHTAL (all mesh tallies, with a "number" column) files next to them, with
.csv or .parquet appended to the file name, e.g., run.outp to run.outp.csv and
run.ptrac to run.ptrac.csv, or outp to outp.csv. Nothing is written if there
is nothing to convert.

Exit codes:
    0    Converted.
    1    There is nothing to convert, e.g., a PTRAC file without events, or
         an OUTP file of a run MCNP stopped with a fatal error; the error
         is named.
    2    Usage error, or the file does not exist or cannot be read as text,
         e.g., a binary PTRAC file.
    3    PyMCNP cannot parse all of the file, e.g., a file of another kind;
         the part before is converted. Also if there is nothing to convert
         because PyMCNP cannot parse the tallies of an OUTP file.
"""

import pathlib
import sys

import pandas
from docopt import docopt

from . import _io
from ..abc.file.WithDataIter import _write_parquet
from ..Outp import Outp
from ..Ptrac import Ptrac
from ..Meshtal import Meshtal


def main() -> None:
    """
    Executes the ``pymcnp convert`` command.
    """

    # Processing CLI arguments.
    args = docopt(__doc__)

    if args['outp']:
        Nonterminal = Outp
    elif args['ptrac']:
        Nonterminal = Ptrac
    else:
        Nonterminal = Meshtal

    file = pathlib.Path(args['<file>'])

    # Reading output file; meshtal files may hold several mesh tallies.
    if Nonterminal is Meshtal:
        frame, remainder, unparsed, fatal = _io.read(file, _meshtal), '', False, []
    else:
        hint = 'PyMCNP reads text PTRAC files only: have MCNP write one with the PTRAC option FILE=ASC.' if Nonterminal is Ptrac else ''
        nonterminal, remainder = _io.read(file, Nonterminal.from_file, hint=hint)
        frame = nonterminal.to_dataframe()
        fatal = nonterminal.fatal_errors if isinstance(nonterminal, Outp) else []
        # Tallies PyMCNP cannot parse were warned about; if they are all there is, the file is not converted in full.
        unparsed = isinstance(nonterminal, Outp) and bool(nonterminal._unparsed_tallies())

    partly = _io.partly_parsed(file, remainder, 'line')

    if frame.empty:
        _io.fail(f'{file}: nothing to convert; no file written.{_stopped(fatal)}', _io.PARTLY_PARSED if partly or unparsed else _io.PROBLEMS)

    # Converting! The output keeps the whole file name, so run.outp and run.ptrac of one run do not write the same file.
    if args['--csv']:
        out = file.with_name(file.name + '.csv')
        frame.to_csv(out, index=False)
    else:
        out = file.with_name(file.name + '.parquet')
        _write_parquet(frame, out)

    _io.info(f'Wrote {out}')

    if partly:
        sys.exit(_io.PARTLY_PARSED)

    _io.done()


def _stopped(fatal: list[str]) -> str:
    """
    Says which fatal errors stopped MCNP, the reason an OUTP file has no tallies.
    """

    # MCNP pads its messages, e.g., "illegal entry:  xdmf", and repeats one for every card it applies to.
    errors = list(dict.fromkeys(' '.join(error.split()) for error in fatal))
    if not fatal:
        return ''
    if len(fatal) == 1:
        return f' MCNP stopped with a fatal error: {errors[0]}'
    return f' MCNP stopped with {len(fatal)} fatal errors, e.g.:' + ''.join(f'\n    {error}' for error in errors[:3])


def _meshtal(path: pathlib.Path) -> pandas.DataFrame:
    """
    Reads every mesh tally of a MESHTAL file into one frame, with a ``number`` column first.
    """

    frame = pandas.concat([tally.to_dataframe().assign(number=tally.tally_number) for tally in Meshtal.iter_tallies(path)], ignore_index=True)
    frame.insert(0, 'number', frame.pop('number'))
    return frame
