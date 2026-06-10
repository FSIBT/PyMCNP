import typing
import dataclasses

from .... import abc
from ..Boundary import Boundary


class Time(Boundary):
    """
    Represents time boundary lines.

    Attributes:
        label: time boundary line `    Time bin boundaries.
        partition: time boundary line `partition` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    label: typing.Annotated[abc.Terminal, r'    Time bin boundaries:  '] = abc.Terminal[r'    Time bin boundaries:  ']('    Time bin boundaries:  ')
    partition: typing.Annotated[abc.Array, typing.Annotated[abc.Terminal, r'.{9}'], typing.Annotated[abc.Terminal, r'']] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
