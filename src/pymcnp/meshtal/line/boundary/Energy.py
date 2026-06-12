import typing
import dataclasses

from .... import abc
from ..Boundary import Boundary


class Energy(Boundary):
    """
    Represents energy boundary lines.

    Attributes:
        label: energy boundary line `    Energy bin boundaries:` symbol.
        bins: energy boundary line bins.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    label: typing.Annotated[abc.Terminal, r'    Energy bin boundaries:'] = abc.Terminal[r'    Energy bin boundaries:']('    Energy bin boundaries:')
    bins: typing.Annotated[abc.Array, typing.Annotated[abc.Terminal, r'.{9}'], typing.Annotated[abc.Terminal, r'']] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
