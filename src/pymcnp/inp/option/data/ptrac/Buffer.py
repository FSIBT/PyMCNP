import typing

from ..... import abc
from ..Ptrac import Ptrac
from .... import literal


class Buffer(Ptrac):
    """
    Represents buffer ptrac data options.

    Attributes:
        keyword: buffer ptrac data option ``r'BUFFER'`` symbol.
        equals: buffer ptrac data option ``r'='`` symbol.
        value: buffer ptrac data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'BUFFER'] | str = abc.Terminal[r'BUFFER']('BUFFER')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
