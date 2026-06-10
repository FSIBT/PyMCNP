import typing
import decimal
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Lcb(Data):
    """
    Represents lcb data cards.

    Attributes:
        keyword: lcb data card `LCB` symbol.
        flenb1: lcb data card `flenb1` parameter.
        flenb2: lcb data card `flenb2` parameter.
        flenb3: lcb data card `flenb3` parameter.
        flenb4: lcb data card `flenb4` parameter.
        flenb5: lcb data card `flenb5` parameter.
        flenb6: lcb data card `flenb6` parameter.
        cotfe: lcb data card `cotfe` parameter.
        film0: lcb data card `film0` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'LCB'] | str = abc.Terminal[r'LCB']('LCB')
    flenb1: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    flenb2: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    flenb3: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    flenb4: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    flenb5: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    flenb6: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    cotfe: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    film0: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
