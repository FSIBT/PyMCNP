import typing
import decimal
import dataclasses

from ..... import abc
from ..Act import Act
from .... import literal


class Thresh(Act):
    """
    Represents thresh act data options.

    Attributes:
        keyword: thresh act data option `THRESH` symbol.
        equals: thresh act data option `=` symbol.
        f: thresh act data option `f` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'THRESH'] | str = abc.Terminal[r'THRESH']('THRESH')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    f: literal.Real | int | float | decimal.Decimal | str
