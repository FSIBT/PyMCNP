import typing

from ..... import abc
from ..Ptrac import Ptrac


class Write(Ptrac):
    """
    Represents write ptrac data options.

    Attributes:
        keyword: write ptrac data option ``r'WRITE'`` symbol.
        equals: write ptrac data option ``r'='`` symbol.
        value: write ptrac data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'WRITE'] | str = abc.Terminal[r'WRITE']('WRITE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:POS|ALL)'] | str
