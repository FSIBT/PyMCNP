import typing

from ..... import abc
from ..Pert import Pert
from .... import literal


class Mat(Pert):
    """
    Represents mat pert data options.

    Attributes:
        keyword: mat pert data option ``r'MAT'`` symbol.
        equals: mat pert data option ``r'='`` symbol.
        m: mat pert data option ``m`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'MAT'] = abc.Terminal[r'MAT']('MAT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    m: literal.Integer
