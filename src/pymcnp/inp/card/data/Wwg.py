import typing
import decimal
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Wwg(Data):
    """
    Represents wwg data cards.

    Attributes:
        keyword: wwg data card `WWG` symbol.
        it: wwg data card `it` parameter.
        ic: wwg data card `ic` parameter.
        wg: wwg data card `wg` parameter.
        ie: wwg data card `ie` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'WWG'] | str = abc.Terminal[r'WWG']('WWG')
    it: literal.Integer | int | str
    ic: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    wg: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | float | decimal.Decimal | str = literal.Jump('J')
    ie: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
