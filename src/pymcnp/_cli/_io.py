import sys
import typing
import pathlib

import rich
import rich.markup
import rich.panel

from .. import abc
from ..Inp import _unparseable_card

T = typing.TypeVar('T')

# Exit codes of every command.
OK = 0
PROBLEMS = 1
USAGE = 2
PARTLY_PARSED = 3


def get_outfile(path: pathlib.Path | str, ext: str, i: str | None = None) -> pathlib.Path:
    """
    Names an output file next to ``path``, with its extension replaced by ``ext``.

    A file name without an extension, e.g., MCNP's default ``outp``, gets
    ``ext`` appended: ``outp.csv``. ``i``, if given, is added to the name:
    ``example_00-cells.pdf``.
    """

    path = pathlib.Path(path)
    name = path.stem + (f'-{i}' if i is not None else '') + '.' + ext

    return path.with_name(name)


def info(msg: str):
    """
    Prints info panel; ``msg`` is plain text, not rich markup.
    """

    rich.print(rich.panel.Panel(f'[bold][deep_sky_blue1]Info:[/][/] {rich.markup.escape(msg)}'))


def error(msg: str):
    """
    Prints error panel; ``msg`` is plain text, not rich markup.
    """

    rich.print(rich.panel.Panel(f'[bold][red]Error:[/][/] {rich.markup.escape(msg)}'))


def warning(msg: str):
    """
    Prints warning panel; ``msg`` is plain text, not rich markup.
    """

    rich.print(rich.panel.Panel(f'[bold][gold3]Warning:[/][/] {rich.markup.escape(msg)}'))


def partly_parsed(path: pathlib.Path | str, remainder: str, unit: str = 'card') -> bool:
    """
    Prints a warning panel if PyMCNP could not parse all of a file.

    Parsing stops at the first card PyMCNP cannot parse, so that card and
    every card after it are missing from the result. The warning names the
    line where parsing stopped if it can find it: for INP files (``unit`` is
    ``card``), the first card that does not parse, as ``pymcnp check`` finds
    it; for other files, the first line of ``remainder`` that is not blank, if
    ``remainder`` is the end of the file.

    Parameters:
        path: Path of the file.
        remainder: Text PyMCNP did not parse.
        unit: What the file is made of, ``card`` for INP files or ``line``.

    Returns:
        True if ``remainder`` is not empty.
    """

    if not remainder.strip():
        return False

    skip, first = next((index, line.strip()) for index, line in enumerate(remainder.split('\n')) if line.strip())
    number = None
    text = abc._text.read_text(path, warn=False)
    if unit == 'card':
        lines = text.split('\n')
        found = _unparseable_card(lines)
        if found is not None:
            number = found[0]
            first = lines[number - 1].strip()
    elif text.endswith(remainder):
        # The remainder starts where parsing stopped: count the lines before it.
        number = text.count('\n', 0, len(text) - len(remainder)) + skip + 1

    where = f', line {number}' if number is not None else ''

    warning(f'{path}{where}: PyMCNP cannot parse the {unit} "{first}", so it and every {unit} after it are missing.')
    return True


def fail(msg: str, code: int) -> typing.NoReturn:
    """
    Prints an error panel and exits with ``code``.
    """

    error(msg)
    sys.exit(code)


def read(path: pathlib.Path, parse: typing.Callable[[pathlib.Path], T], unit: str = 'line', hint: str = '') -> T:
    """
    Reads a file for a command, exiting with a message instead of a traceback.

    Exits with ``USAGE`` if the file does not exist or cannot be read as
    text, and with ``PARTLY_PARSED`` if PyMCNP cannot parse it, as ``pymcnp
    check`` does for every command. For INP files (``unit`` is ``card``), a
    card PyMCNP cannot parse is named with its line, as ``pymcnp check``
    does; other errors, e.g., two cells with one number, are given as they
    are.

    Parameters:
        path: Path of the file.
        parse: Function that parses the file at a path.
        unit: What the file is made of, ``card`` for INP files or ``line``.
        hint: Sentence added to the message for a file that is not text.

    Returns:
        What ``parse`` returns.
    """

    if not path.exists():
        fail(f'{path}: no such file.', USAGE)
    if not path.is_file():
        fail(f'{path}: not a file.', USAGE)

    try:
        return parse(path)
    except UnicodeDecodeError as err:
        if 'UTF-16' in err.reason:
            fail(f'{path}: UTF-16 text, which PyMCNP does not read; save the file as UTF-8.', USAGE)
        # Text that is not UTF-8 is read as Latin-1, so this is a file with a NUL byte, e.g., a binary PTRAC file.
        fail(f'{path}: not a text file (a NUL byte at byte offset {err.start}), so PyMCNP cannot read it.{" " + hint if hint else ""}', USAGE)
    except OSError as err:
        fail(f'{path}: cannot read the file: {err.strerror}.', USAGE)
    except abc.Error as err:
        # Errors of the grammar have a stack; others, e.g., two cells with one number, are not about one card.
        if unit == 'card' and err.stack and (found := _unparseable_card(abc._text.read_text(path, warn=False).split('\n'))) is not None:
            number, card_err = found
            fail(f'{path}, line {number}: PyMCNP cannot parse this card: {str(card_err).splitlines()[0]} Nothing is read; fix the card and check the file with "pymcnp check".', PARTLY_PARSED)
        fail(f'{path}: PyMCNP cannot parse this file: {" ".join(str(err).split())}', PARTLY_PARSED)


def done():
    """
    Prints done message.
    """

    info('Done!')
