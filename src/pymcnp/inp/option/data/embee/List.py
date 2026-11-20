import typing

from ..... import abc
from ..Embee import Embee
from .... import literal


class List(Embee):
    """
    Represents list embee data options.

    Attributes:
        keyword: list embee data option ``r'LIST'`` symbol.
        equals: list embee data option ``r'='`` symbol.
        value: list embee data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'LIST'] = abc.Terminal[r'LIST']('LIST')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
