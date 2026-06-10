import typing
import dataclasses

import collections

from ..... import abc
from ..Fmesh import Fmesh
from .... import literal


class Tints(Fmesh):
    """
    Represents tints fmesh data options.

    Attributes:
        keyword: tints fmesh data option `TINTS` symbol.
        equals: tints fmesh data option `=` symbol.
        n: tints fmesh data option `n` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'TINTS'] | str = abc.Terminal[r'TINTS']('TINTS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    n: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
