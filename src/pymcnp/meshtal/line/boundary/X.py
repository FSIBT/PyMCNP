import typing
import dataclasses

from .... import abc
from ..Boundary import Boundary


class X(Boundary):
    """
    Represents x boundary lines.

    Attributes:
        label: x boundary line `    X direction:` symbol.
        partition: x boundary line `partition` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    label: typing.Annotated[abc.Terminal, r'    X direction:'] = abc.Terminal[r'    X direction:']('    X direction:')
    partition: typing.Annotated[abc.Array, typing.Annotated[abc.Terminal, r'.{10}'], typing.Annotated[abc.Terminal, r'']] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
