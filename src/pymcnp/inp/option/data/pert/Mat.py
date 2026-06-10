import typing
import dataclasses

from ..... import abc
from ..Pert import Pert
from .... import literal


class Mat(Pert):
    """
    Represents mat pert data options.

    Attributes:
        keyword: mat pert data option `MAT` symbol.
        equals: mat pert data option `=` symbol.
        m: mat pert data option `m` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'MAT'] | str = abc.Terminal[r'MAT']('MAT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    m: literal.Integer | int | str
