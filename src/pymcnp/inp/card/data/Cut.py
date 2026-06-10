import typing
import decimal
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Cut(Data):
    """
    Represents cut data cards.

    Attributes:
        keyword: cut data card `CUT` symbol.
        colon: cut data card `:` symbol.
        particle: cut data card `particle` parameter.
        t: cut data card `t` parameter.
        e: cut data card `e` parameter.
        wc1: cut data card `wc1` parameter.
        wc2: cut data card `wc2` parameter.
        swtm: cut data card `swtm` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'CUT'] | str = abc.Terminal[r'CUT']('CUT')
    colon: typing.Annotated[abc.Terminal, r':'] | str = abc.Terminal[r':'](':')
    particle: literal.Particle | str
    t: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    e: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    wc1: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    wc2: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    swtm: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
