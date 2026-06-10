import typing
import dataclasses

from ..... import abc
from .... import literal
from ..T import T


class Csub(T):
    """
    Represents csub t data options.

    Attributes:
        keyword: csub t data option `CSUB` symbol.
        equals: csub t data option `=` symbol.
        value: csub t data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'CSUB'] | str = abc.Terminal[r'CSUB']('CSUB')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
