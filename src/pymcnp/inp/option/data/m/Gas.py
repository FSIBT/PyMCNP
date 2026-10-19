import typing
import dataclasses

from ..... import abc
from .... import literal
from ..M import M


class Gas(M):
    """
    Represents gas m data options.

    Attributes:
        keyword: gas m data option `GAS` symbol.
        equals: gas m data option `=` symbol.
        value: gas m data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    keyword: typing.Annotated[abc.Terminal, r'GAS'] | str = abc.Terminal[r'GAS']('GAS')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str = dataclasses.field(kw_only=True)
