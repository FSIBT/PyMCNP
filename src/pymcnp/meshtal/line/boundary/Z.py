import typing
import dataclasses

from .... import abc
from ..Boundary import Boundary


class Z(Boundary):
    """
    Represents z boundary lines.

    Attributes:
        label: z boundary line `    Z direction:` symbol.
        partition: z boundary line `partition` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    label: typing.Annotated[abc.Terminal, r'    Z direction:'] = abc.Terminal[r'    Z direction:']('    Z direction:')
    partition: typing.Annotated[abc.Array, typing.Annotated[abc.Terminal, r'.{10}'], typing.Annotated[abc.Terminal, r'']] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
