import typing

from ... import abc
from .. import line


class Event(abc.Nonterminal):
    """
    Represents event blocks.

    Attributes:
        j: event block j line.
        newline: event block `\\n` symbol.
        p: event block p line.
    """

    j: line.J
    newline: typing.Annotated[abc.Terminal, r'\n']
    p: line.P
