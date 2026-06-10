import typing
import dataclasses

import collections

from ..... import abc
from ..Ptrac import Ptrac
from .... import literal


class Nps(Ptrac):
    """
    Represents nps ptrac data options.

    Attributes:
        keyword: nps ptrac data option `NPS` symbol.
        equals: nps ptrac data option `=` symbol.
        n: nps ptrac data option `n` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'NPS'] | str = abc.Terminal[r'NPS']('NPS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    n: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
