import pathlib

import rich
import rich.panel


def get_outfile(path: str | pathlib.Path, ext: str, i: int = None) -> str:
    path = str(path)
    path, _ = path.rsplit('.', maxsplit=1)

    return pathlib.Path(path + f'{f"-{i:05}" if i else ""}.' + ext)


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

    warning('PyMCNP is in active development! Please, double-check everything works. Reports error on [underline][link=https://github.com/FSIBT/PyMCNP/issues]GitHub[/][/].')
