import typing

from ..... import abc
from ..Pert import Pert
from .... import literal


class Method(Pert):
    """
    Represents method pert data options.

    Attributes:
        keyword: method pert data option ``r'METHOD'`` symbol.
        equals: method pert data option ``r'='`` symbol.
        j: method pert data option ``j`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'METHOD'] = abc.Terminal[r'METHOD']('METHOD')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    j: literal.Real
