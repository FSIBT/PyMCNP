import typing

from .... import abc
from ... import literal
from ..Data import Data


class Wwg(Data):
    """
    Represents wwg data cards.

    Attributes:
        keyword: wwg data card ``r'WWG'`` symbol.
        it: wwg data card ``it`` parameter.
        ic: wwg data card ``ic`` parameter.
        wg: wwg data card ``wg`` parameter.
        ie: wwg data card ``ie`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'WWG'] = abc.Terminal[r'WWG']('WWG')
    it: literal.Integer
    ic: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] = literal.Jump('J')
    wg: literal.Real | literal.Jump | typing.Annotated[abc.Terminal, r''] = literal.Jump('J')
    ie: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] = literal.Jump('J')
