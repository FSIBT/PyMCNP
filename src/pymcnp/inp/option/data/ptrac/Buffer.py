import typing
import dataclasses

from ..... import abc
from ..Ptrac import Ptrac
from .... import literal


class Buffer(Ptrac):
    """
    Represents buffer ptrac data options.

    Attributes:
        keyword: buffer ptrac data option `BUFFER` symbol.
        equals: buffer ptrac data option `=` symbol.
        value: buffer ptrac data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'BUFFER'] | str = abc.Terminal[r'BUFFER']('BUFFER')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
