import typing

from .... import abc
from ... import option
from ..Data import Data


class Stop(Data):
    """
    Represents stop data cards.

    Attributes:
        keyword: stop data card ``r'STOP'`` symbol.
        options: stop data card ``options`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'STOP'] = abc.Terminal[r'STOP']('STOP')
    options: typing.Annotated[abc.Array, option.data.Stop, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
