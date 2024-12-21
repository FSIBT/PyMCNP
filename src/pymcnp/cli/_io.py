"""
'_utils'
"""

import datetime

import rich
import rich.panel


def get_timestamp() -> str:
    return datetime.datetime.today().strftime('%Y-%m-%d--%H-%M-%S')


def error(msg):
    rich.print(rich.panel.Panel(msg))
    exit(1)


def print(msg):
    rich.print(rich.panel.Panel(msg))


def done():
    rich.print(rich.panel.Panel('[deep_sky_blue1][bold]Info:[/][/] Done!'))


def warning():
    rich.print(
        rich.panel.Panel(
            '[bold][gold3]Warning:[/][/] PyMCNP is just getting started! '
            'Please, double check the output to make sure everything works. '
            'If you find errors, please, report them on [link=https://github.com/FSIBT/PyMCNP/issues]GitHub[/link].'
        )
    )
