import typing

from ..... import abc
from ..Kpert import Kpert
from .... import literal


class Rho(Kpert):
    """
    Represents rho kpert data options.

    Attributes:
        keyword: rho kpert data option ``r'RHO'`` symbol.
        equals: rho kpert data option ``r'='`` symbol.
        r: rho kpert data option ``r`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'RHO'] = abc.Terminal[r'RHO']('RHO')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    r: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
