"""
'_utils'
"""

import datetime

import rich


def get_timestamp() -> str:
    return datetime.datetime.today().strftime('%Y-%m-%d--%H-%M-%S')


def error(msg):
    rich.print(msg)
    exit(1)


def warning(msg):
    rich.print(rich.panel.Panel(msg))
    return
