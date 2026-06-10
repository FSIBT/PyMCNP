import typing
import dataclasses

import collections

from ..... import abc
from ..Ptrac import Ptrac
from .... import literal


class Type(Ptrac):
    """
    Represents type ptrac data options.

    Attributes:
        keyword: type ptrac data option `TYPE` symbol.
        equals: type ptrac data option `=` symbol.
        value: type ptrac data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'TYPE'] | str = abc.Terminal[r'TYPE']('TYPE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Array, literal.Particle, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Particle | str] | str = abc.Terminal[r'']('')
