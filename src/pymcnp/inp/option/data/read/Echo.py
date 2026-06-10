import typing
import dataclasses

from ..... import abc
from ..Read import Read


class Echo(Read):
    """
    Represents echo read data options.

    Attributes:
        keyword: echo read data option `ECHO` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'ECHO'] | str = abc.Terminal[r'ECHO']('ECHO')
