import typing
import dataclasses

from ..... import abc
from ..Fmesh import Fmesh
from .... import literal


class Kclear(Fmesh):
    """
    Represents kclear fmesh data options.

    Attributes:
        keyword: kclear fmesh data option `KCLEAR` symbol.
        equals: kclear fmesh data option `=` symbol.
        n: kclear fmesh data option `n` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'KCLEAR'] | str = abc.Terminal[r'KCLEAR']('KCLEAR')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    n: literal.Integer | int | str
