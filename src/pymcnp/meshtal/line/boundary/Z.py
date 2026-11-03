import typing

from .... import abc
from ..Boundary import Boundary


class Z(Boundary):
    """
    Represents z boundary lines.

    Attributes:
        label: z boundary line `    Z direction:` symbol.
        bins: z boundary line bins.
    """

    label: typing.Annotated[abc.Terminal, r'    Z direction:'] = abc.Terminal[r'    Z direction:']('    Z direction:')
    bins: typing.Annotated[abc.Array, typing.Annotated[abc.Terminal, r'.{10}'], typing.Annotated[abc.Terminal, r'']] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
