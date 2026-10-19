import pathlib

import rich
import rich.panel


def get_outfile(path: pathlib.Path | str, ext: str, i: str | int | None = None) -> pathlib.Path:
    if isinstance(i, int):
        i = f'{i:05}'

    path = str(path)
    path, _ = path.rsplit('.', maxsplit=1)

    return pathlib.Path(path + (f'-{i}' if i else '') + '.' + ext)


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


def done():
    """
    Prints done message.
    """

    info('Done!')
