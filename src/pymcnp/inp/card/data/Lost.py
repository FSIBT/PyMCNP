import typing

from .... import abc
from ... import literal
from ..Data import Data


class Lost(Data):
    """
    Represents lost data cards.

    Attributes:
        keyword: lost data card ``r'LOST'`` symbol.
        lost1: lost data card ``lost1`` parameter.
        lost2: lost data card ``lost2`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'LOST'] | str = abc.Terminal[r'LOST']('LOST')
    lost1: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    lost2: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
