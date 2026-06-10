import typing
import decimal
import dataclasses

from ..... import abc
from ..Ssr import Ssr
from .... import literal


class Poa(Ssr):
    """
    Represents poa ssr data options.

    Attributes:
        keyword: poa ssr data option `POA` symbol.
        equals: poa ssr data option `=` symbol.
        c: poa ssr data option `c` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'POA'] | str = abc.Terminal[r'POA']('POA')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    c: literal.Real | int | float | decimal.Decimal | str
