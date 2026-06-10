import typing
import dataclasses

import collections

from ..... import abc
from .... import literal
from ..Mesh import Mesh


class Iints(Mesh):
    """
    Represents iints mesh data options.

    Attributes:
        keyword: iints mesh data option `IINTS` symbol.
        equals: iints mesh data option `=` symbol.
        n: iints mesh data option `n` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'IINTS'] | str = abc.Terminal[r'IINTS']('IINTS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    n: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
