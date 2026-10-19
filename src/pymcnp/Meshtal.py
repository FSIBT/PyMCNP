import typing

from . import abc
from . import meshtal


class Meshtal(abc.File):
    """
    Represents meshtal files.

    Attributes:
        header: meshtal `header` parameter.
        title: meshtal `title` parameter.
        histories: meshtal `histories` parameter.
        number: meshtal `number` parameter.
        particle: meshtal `particle` parameter.
        bins: meshtal `bins` parameter.
        columns: meshtal `columns` parameter.
    """

    header: meshtal.line.Header
    title: typing.Annotated[abc.Terminal, r'\n.+?\n']
    histories: typing.Annotated[abc.Terminal, r' Number of histories used for normalizing tallies =.{17}\n\n']
    number: typing.Annotated[abc.Terminal, r' Mesh Tally Number.{10}\n']
    particle: typing.Annotated[abc.Terminal, r' .{8} mesh tally\.\n\n']
    bins: meshtal.block.Bin
    columns: typing.Annotated[abc.Terminal, r'[\s\S]*']
