import typing
import dataclasses

import collections

from ..... import abc
from ..Ptrac import Ptrac
from .... import literal


class Surface(Ptrac):
    """
    Represents surface ptrac data options.

    Attributes:
        keyword: surface ptrac data option `SURFACE` symbol.
        equals: surface ptrac data option `=` symbol.
        s: surface ptrac data option `s` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'SURFACE'] | str = abc.Terminal[r'SURFACE']('SURFACE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    s: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | float | str] | str = abc.Terminal[r'']('')
