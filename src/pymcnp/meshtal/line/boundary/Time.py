import typing

from .... import abc
from ..Boundary import Boundary


class Time(Boundary):
    """
    Represents time boundary lines.

    Attributes:
        label: time boundary line ``r'    Time bin boundaries:  '`` symbol.
        bins: time boundary line bins.
    """

    label: typing.Annotated[abc.Terminal, r'    Time bin boundaries:  '] = abc.Terminal[r'    Time bin boundaries:  ']('    Time bin boundaries:  ')
    bins: typing.Annotated[abc.Array, typing.Annotated[abc.Terminal, r'.{9}'], typing.Annotated[abc.Terminal, r'']] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
