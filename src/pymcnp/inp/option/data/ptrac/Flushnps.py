import typing
import dataclasses

from ..... import abc
from ..Ptrac import Ptrac
from .... import literal


class Flushnps(Ptrac):
    """
    Represents flushnps ptrac data options.

    Attributes:
        keyword: flushnps ptrac data option `FLUSHNPS` symbol.
        equals: flushnps ptrac data option `=` symbol.
        value: flushnps ptrac data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'FLUSHNPS'] | str = abc.Terminal[r'FLUSHNPS']('FLUSHNPS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
