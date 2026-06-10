import typing
import dataclasses

import collections

from ..... import abc
from .... import literal
from ..Mesh import Mesh


class Kints(Mesh):
    """
    Represents kints mesh data options.

    Attributes:
        keyword: kints mesh data option `KINTS` symbol.
        equals: kints mesh data option `=` symbol.
        n: kints mesh data option `n` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'KINTS'] | str = abc.Terminal[r'KINTS']('KINTS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    n: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Integer | int | str] | str = abc.Terminal[r'']('')
