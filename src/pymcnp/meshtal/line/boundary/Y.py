import typing
import dataclasses

from .... import abc
from ..Boundary import Boundary


class Y(Boundary):
    """
    Represents y boundary lines.

    Attributes:
        label: y boundary line `    Y direction:` symbol.
        bins: y boundary line bins.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    label: typing.Annotated[abc.Terminal, r'    Y direction:'] = abc.Terminal[r'    Y direction:']('    Y direction:')
    bins: typing.Annotated[abc.Array, typing.Annotated[abc.Terminal, r'.{10}'], typing.Annotated[abc.Terminal, r'']] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
