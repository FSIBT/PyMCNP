import typing
import dataclasses

import collections

from ..... import abc
from .... import literal
from ..Mesh import Mesh


class Jints(Mesh):
    """
    Represents jints mesh data options.

    Attributes:
        keyword: jints mesh data option `JINTS` symbol.
        equals: jints mesh data option `=` symbol.
        n: jints mesh data option `n` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'JINTS'] | str = abc.Terminal[r'JINTS']('JINTS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    n: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
