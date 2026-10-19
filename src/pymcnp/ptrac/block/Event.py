import typing
import dataclasses

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

    j: line.J = dataclasses.field(kw_only=True)
    newline: typing.Annotated[abc.Terminal, r'\n'] = dataclasses.field(kw_only=True)
    p: line.P = dataclasses.field(kw_only=True)
