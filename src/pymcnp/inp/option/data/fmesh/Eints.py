import typing
import dataclasses

import collections

from ..... import abc
from ..Fmesh import Fmesh
from .... import literal


class Eints(Fmesh):
    """
    Represents eints fmesh data options.

    Attributes:
        keyword: eints fmesh data option `EINTS` symbol.
        equals: eints fmesh data option `=` symbol.
        n: eints fmesh data option `n` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'EINTS'] | str = abc.Terminal[r'EINTS']('EINTS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    n: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
