import typing
import dataclasses

import collections

from ..... import abc
from ..Fmesh import Fmesh
from .... import literal


class Kints(Fmesh):
    """
    Represents kints fmesh data options.

    Attributes:
        keyword: kints fmesh data option `KINTS` symbol.
        equals: kints fmesh data option `=` symbol.
        n: kints fmesh data option `n` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'KINTS'] | str = abc.Terminal[r'KINTS']('KINTS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    n: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
