import typing
import dataclasses

import collections

from ..... import abc
from ..Fmesh import Fmesh
from .... import literal


class Iints(Fmesh):
    """
    Represents iints fmesh data options.

    Attributes:
        keyword: iints fmesh data option `IINTS` symbol.
        equals: iints fmesh data option `=` symbol.
        n: iints fmesh data option `n` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'IINTS'] | str = abc.Terminal[r'IINTS']('IINTS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    n: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
