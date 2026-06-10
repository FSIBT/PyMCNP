import typing
import dataclasses

from ..... import abc
from ..Read import Read


class Noecho(Read):
    """
    Represents noecho read data options.

    Attributes:
        keyword: noecho read data option `NOECHO` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'NOECHO'] | str = abc.Terminal[r'NOECHO']('NOECHO')
