import typing

from ..... import abc
from ..Ptrac import Ptrac
from ..Ptrac import PtracSpace


class Event(Ptrac):
    """
    Represents event ptrac data options.

    Attributes:
        keyword: event ptrac data option ``r'EVENT'`` symbol.
        equals: event ptrac data option ``r'='`` symbol.
        value: event ptrac data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'EVENT'] = abc.Terminal[r'EVENT']('EVENT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Array, typing.Annotated[abc.Terminal, r'(?:SRC|BNK|SUR|COL|TER|CAP)(?![A-Za-z])'], PtracSpace]
