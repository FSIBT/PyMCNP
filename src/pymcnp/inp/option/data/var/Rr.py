import typing
import dataclasses

from ..... import abc
from ..Var import Var


class Rr(Var):
    """
    Represents rr var data options.

    Attributes:
        keyword: rr var data option `RR` symbol.
        equals: rr var data option `=` symbol.
        value: rr var data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'RR'] | str = abc.Terminal[r'RR']('RR')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: typing.Annotated[abc.Terminal, r'(?:ON|OFF)'] | str
