import typing

from ... import abc
from .. import line


class Event(abc.Nonterminal):
    """
    Represents event blocks.

    Attributes:
        j: event block `j` parameter.
        p: event block `p` parameter.
    """

    j: line.J
    newline: typing.Annotated[abc.Terminal, r'\n']
    p: line.P
