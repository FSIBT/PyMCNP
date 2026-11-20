import typing

from ..... import abc
from ..Stop import Stop
from .... import literal


class F(Stop):
    """
    Represents f stop data options.

    Attributes:
        keyword: f stop data option ``r'F'`` symbol.
        suffix: f stop data option ``k`` parameter.
        equals: f stop data option ``r'='`` symbol.
        e: f stop data option ``e`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'F'] = abc.Terminal[r'F']('F')
    suffix: literal.Integer
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    e: literal.Real
