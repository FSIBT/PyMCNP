import typing
import dataclasses

from ..... import abc
from ..Ptrac import Ptrac


class Event(Ptrac):
    """
    Represents event ptrac data options.

    Attributes:
        keyword: event ptrac data option `EVENT` symbol.
        equals: event ptrac data option `=` symbol.
        value: event ptrac data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'EVENT'] | str = abc.Terminal[r'EVENT']('EVENT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:SRC|BNK|SUR|COL|TER|CAP)'] | str
