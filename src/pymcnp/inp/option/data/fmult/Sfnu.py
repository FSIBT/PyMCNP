import typing

from ..... import abc
from ..Fmult import Fmult
from .... import literal


class Sfnu(Fmult):
    """
    Represents sfnu fmult data options.

    Attributes:
        keyword: sfnu fmult data option ``r'SFNU'`` symbol.
        equals: sfnu fmult data option ``r'='`` symbol.
        x: sfnu fmult data option ``x`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'SFNU'] = abc.Terminal[r'SFNU']('SFNU')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    x: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
