import pathlib
import datetime

import rich
import rich.panel


def get_outfile(path: str | pathlib.Path, new: str, old: str) -> str:
    path = str(path)

    if path.rsplit('.', maxsplit=1)[0] == old:
        path = path.rsplit('.', maxsplit=1)[1]

    return pathlib.Path(path + '.' + new)


def get_timestamp() -> str:
    """
    Gets current timestamp.

    Returns:
        Current timestamp "YYYY-MM-DD--HH-MM-SS".
    """

    return datetime.datetime.today().strftime('%Y-%m-%d--%H-%M-%S')


def print(msg: str):
    """
    Wraps ``rich.print``.
    """

    rich.print(msg)


def info(msg: str):
    """
    Prints error panel.
    """

    rich.print(rich.panel.Panel(f'[bold][deep_sky_blue1]Info:[/][/] {msg}'))


def error(msg: str):
    """
    Prints error panel.
    """

    rich.print(rich.panel.Panel(f'[bold][red]Error:[/][/] {msg}'))


def warning(msg: str):
    """
    Prints error panel.
    """

    rich.print(rich.panel.Panel(f'[bold][gold3]Warning:[/][/] {msg}'))


def done():
    """
    Prints done message.
    """

    info('Done!')


def disclaimer():
    """
    Prints disclaimer message.
    """

    warning('PyMCNP is in active development! ' 'Please, double check eveything works. ' 'Reports error on [underline][link=https://github.com/FSIBT/PyMCNP/issues]GitHub[/][/].')
