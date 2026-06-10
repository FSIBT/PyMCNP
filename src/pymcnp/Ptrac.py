import typing

from . import abc
from . import ptrac


class Ptrac(abc.File):
    """
    Represents ptrac files.

    Attributes:
        header: ptrac `header` parameter.
        histories: ptrac `histories` parameter.
    """

    header: ptrac.block.Header
    histories: typing.Annotated[abc.Array, ptrac.block.History, typing.Annotated[abc.Terminal, r'']]
    newline: typing.Annotated[abc.Terminal, r'\n?']
