import pathlib

import rich
import rich.markup
import rich.panel


def get_outfile(path: pathlib.Path | str, ext: str, i: str | None = None) -> pathlib.Path:
    path = str(path)
    path, _ = path.rsplit('.', maxsplit=1)

    return pathlib.Path(path + (f'-{i}' if i is not None else '') + '.' + ext)


def info(msg: str):
    """
    Prints info panel.
    """

    rich.print(rich.panel.Panel(f'[bold][deep_sky_blue1]Info:[/][/] {msg}'))


def error(msg: str):
    """
    Prints error panel.
    """

    rich.print(rich.panel.Panel(f'[bold][red]Error:[/][/] {msg}'))


def warning(msg: str):
    """
    Prints warning panel.
    """

    rich.print(rich.panel.Panel(f'[bold][gold3]Warning:[/][/] {msg}'))


def partly_parsed(path: pathlib.Path | str, remainder: str) -> bool:
    """
    Prints a warning panel if PyMCNP could not parse all of a file.

    Parsing stops at the first card PyMCNP cannot parse, so that card and
    every card after it are missing from the result.

    Returns:
        True if ``remainder`` is not empty.
    """

    if not remainder.strip():
        return False

    first = next(line for line in remainder.split('\n') if line.strip()).strip()
    warning(rich.markup.escape(f'{path}: PyMCNP cannot parse the card "{first}", so it and every card after it are missing.'))
    return True


def done():
    """
    Prints done message.
    """

    info('Done!')
