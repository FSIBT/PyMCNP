import typing
import dataclasses

from ..... import abc
from ..Ptrac import Ptrac


class Coinc(Ptrac):
    """
    Represents coinc ptrac data options.

    Attributes:
        keyword: coinc ptrac data option `COINC` symbol.
        equals: coinc ptrac data option `=` symbol.
        value: coinc ptrac data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'COINC'] | str = abc.Terminal[r'COINC']('COINC')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:COL|LIN)'] | str
