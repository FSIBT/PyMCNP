import typing
import dataclasses

from ..... import abc
from .... import literal
from ..Ksen import Ksen


class Legendre(Ksen):
    """
    Represents legendre ksen data options.

    Attributes:
        keyword: legendre ksen data option `LEGENDRE` symbol.
        equals: legendre ksen data option `=` symbol.
        value: legendre ksen data option `value` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'LEGENDRE'] | str = abc.Terminal[r'LEGENDRE']('LEGENDRE')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str
