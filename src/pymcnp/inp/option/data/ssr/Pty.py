import typing
import dataclasses

import collections

from ..... import abc
from ..Ssr import Ssr
from .... import literal


class Pty(Ssr):
    """
    Represents pty ssr data options.

    Attributes:
        keyword: pty ssr data option `PTY` symbol.
        equals: pty ssr data option `=` symbol.
        p: pty ssr data option `p` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'PTY'] | str = abc.Terminal[r'PTY']('PTY')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    p: typing.Annotated[abc.Array, literal.Particle, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Particle | str] | str = abc.Terminal[r'']('')
