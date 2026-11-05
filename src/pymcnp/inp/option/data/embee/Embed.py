import typing

from ..... import abc
from ..Embee import Embee
from .... import literal


class Embed(Embee):
    """
    Represents embed embee data options.

    Attributes:
        keyword: embed embee data option ``r'EMBED'`` symbol.
        equals: embed embee data option ``r'='`` symbol.
        value: embed embee data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'EMBED'] | str = abc.Terminal[r'EMBED']('EMBED')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
