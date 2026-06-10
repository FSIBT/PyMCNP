import typing
import dataclasses

from ..... import abc
from ..Ptrac import Ptrac
from .... import literal


class Meph(Ptrac):
    """
    Represents meph ptrac data options.

    Attributes:
        keyword: meph ptrac data option `MEPH` symbol.
        equals: meph ptrac data option `=` symbol.
        value: meph ptrac data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'MEPH'] | str = abc.Terminal[r'MEPH']('MEPH')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
