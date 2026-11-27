import re
import sys
import typing
import difflib
import pathlib

import docopt as _docopt

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


def docopt(doc: str, argv: list[str] | None = None, options_first: bool = False, **kwargs) -> dict:
    """
    Parses the command line as ``docopt.docopt`` does, but says what is wrong with it if it does not fit the usage.

    docopt itself only says "found unmatched (duplicate?) arguments" with its internal patterns, or nothing.

    Raises:
        docopt.DocoptExit: The message names the problem, e.g., "Unknown option --partquet; did you mean --parquet?", followed by the usage.
    """

    argv = sys.argv[1:] if argv is None else argv
    try:
        return _docopt.docopt(doc, argv, options_first=options_first, **kwargs)
    except _docopt.DocoptExit:
        pass
    raise _docopt.DocoptExit(f'Error: {_usage_problem(doc, argv, options_first)}\n') from None


def _or(words: list[str], conjunction: str = 'or') -> str:
    return words[0] if len(words) == 1 else f'{", ".join(words[:-1])} {conjunction} {words[-1]}'


def _suggest(word: str, words: typing.Iterable[str]) -> str:
    close = difflib.get_close_matches(word, list(words), n=1, cutoff=0.6)
    return f'; did you mean {close[0]}?' if close else '.'


def _usage_problem(doc: str, argv: list[str], options_first: bool) -> str:
    """
    Finds the first way ``argv`` does not fit the usage of ``doc``.
    """

    usage = doc.partition('Usage:')[2].strip().partition('\n\n')[0]
    lines = [re.findall(r'\.\.\.|[\[\]()|]|[^\s\[\]()|]+', line)[1:] for line in usage.splitlines()]

    # Options: the names of each, the long ones, and those taking a value, e.g., -o --output=<file>.
    aliases: dict[str, str] = {}
    valued: set[str] = set()
    for line in doc.splitlines():
        if (line := line.strip()).startswith('-'):
            names = re.findall(r'--?[A-Za-z][\w-]*', line.partition('  ')[0])
            for name in names:
                aliases[name] = names[-1]
            if '<' in line.partition('  ')[0]:
                valued.update(names)
    for name in re.findall(r'(?<![\w-])--?[A-Za-z][\w-]*', usage):
        aliases.setdefault(name, name)
    longs = [name for name in aliases if name.startswith('--')]

    # Splitting the arguments into options and positional arguments, as docopt does.
    given: list[str] = []
    positionals: list[str] = []
    tokens = iter(argv)
    for token in tokens:
        if token == '--' or (options_first and positionals):
            positionals += [token] if token != '--' else []
            positionals += list(tokens)
        elif token.startswith('--') and len(token) > 2:
            name, equals, _ = token.partition('=')
            matches = [name] if name in aliases else [option for option in longs if option.startswith(name)]
            if len(matches) != 1:
                return f'Unknown option {name}{_suggest(name, longs)}'
            given.append(aliases[matches[0]])
            if matches[0] in valued and not equals:
                next(tokens, None)
        elif re.match(r'-[A-Za-z]', token):
            for i, letter in enumerate(token[1:], 1):
                if (name := f'-{letter}') not in aliases:
                    return f'Unknown option {name}.'
                given.append(aliases[name])
                if name in valued:
                    if i == len(token) - 1:
                        next(tokens, None)
                    break
        else:
            positionals.append(token)

    # Commands, e.g., "convert outp": the words of the usage lines that fit the arguments so far.
    def words(line: list[str]) -> list[str]:
        return [token for token in line if re.fullmatch(r'[a-z][\w-]*', token) and token != 'options']

    candidates = lines
    depth = 0
    while choices := list(dict.fromkeys(words(line)[depth] for line in candidates if len(words(line)) > depth)):
        program = ' '.join(['pymcnp', *positionals[:depth]])
        if depth >= len(positionals):
            return f'{program} needs {_or(choices)}.'
        if positionals[depth] not in choices:
            word = positionals[depth]
            # A path, e.g., outp.txt, is a file given too early, not a misspelled command.
            return f'{program} needs {_or(choices)}, not {word}' + ('.' if re.search(r'[./\\]', word) else _suggest(word, choices))
        candidates = [line for line in candidates if len(words(line)) > depth and words(line)[depth] == positionals[depth]]
        depth += 1
    if not candidates:
        return 'The arguments do not fit the usage.'
    line = candidates[0]
    program = ' '.join(['pymcnp', *positionals[:depth]])

    # Required alternatives, e.g., (--csv | --parquet).
    for group in re.findall(r'\(([^()]*\|[^()]*)\)', ' '.join(line)):
        options = [aliases.get(option, option) for option in group.replace('|', ' ').split()]
        chosen = [option for option in options if option in given]
        if not chosen:
            return f'Give {_or(options)}.'
        if len(chosen) > 1:
            return f'Give only one of {_or(chosen, "and")}.'

    # Positional arguments, e.g., <inp>, [<command>] or <inp>...
    required, repeated, optional, bracket = [], False, 0, 0
    for i, token in enumerate(line):
        bracket += (token == '[') - (token == ']')
        if token.startswith('<'):
            if bracket:
                optional += 1
            else:
                required.append(token)
            repeated |= line[i + 1 : i + 2] == ['...']
    values = positionals[depth:]
    if len(values) < len(required):
        return f'{program} needs {_or(required[len(values) :], "and")}.'
    if not repeated and len(values) > len(required) + optional:
        return f'Unexpected argument {values[len(required) + optional]}.'

    return 'The arguments do not fit the usage.'


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
