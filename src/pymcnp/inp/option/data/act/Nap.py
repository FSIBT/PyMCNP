import typing
import dataclasses

from ..... import abc
from ..Act import Act
from .... import literal


class Nap(Act):
    """
    Represents nap act data options.

    Attributes:
        keyword: nap act data option `NAP` symbol.
        equals: nap act data option `=` symbol.
        valuem: nap act data option `valuem` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'NAP'] | str = abc.Terminal[r'NAP']('NAP')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    valuem: literal.Integer | int | str
