import typing

from .... import abc
from ..Cell import Cell
from ... import literal


class Rho(Cell):
    """
    Represents rho cell options.

    Attributes:
        keyword: rho cell option ``r'RHO'`` symbol.
        equals: rho cell option ``r'='`` symbol.
        d: rho cell option ``d`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'RHO'] = abc.Terminal[r'RHO']('RHO')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    d: literal.Real
