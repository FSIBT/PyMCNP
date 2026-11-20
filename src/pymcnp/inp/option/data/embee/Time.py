import typing

from ..... import abc
from ..Embee import Embee
from .... import literal


class Time(Embee):
    """
    Represents time embee data options.

    Attributes:
        keyword: time embee data option ``r'TIME'`` symbol.
        equals: time embee data option ``r'='`` symbol.
        value: time embee data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'TIME'] = abc.Terminal[r'TIME']('TIME')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    value: literal.Real
