import typing
import dataclasses

from ..... import abc
from .... import literal
from ..M import M


class Hstep(M):
    """
    Represents hstep m data options.

    Attributes:
        keyword: hstep m data option `HSTEP` symbol.
        equals: hstep m data option `=` symbol.
        n: hstep m data option `n` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'HSTEP'] | str = abc.Terminal[r'HSTEP']('HSTEP')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    n: literal.Integer | int | str
