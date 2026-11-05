import typing

from ..... import abc
from ..Ptrac import Ptrac
from .... import literal


class Flushnps(Ptrac):
    """
    Represents flushnps ptrac data options.

    Attributes:
        keyword: flushnps ptrac data option ``r'FLUSHNPS'`` symbol.
        equals: flushnps ptrac data option ``r'='`` symbol.
        value: flushnps ptrac data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'FLUSHNPS'] | str = abc.Terminal[r'FLUSHNPS']('FLUSHNPS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
