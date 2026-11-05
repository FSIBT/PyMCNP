import typing

import collections

from .... import abc
from ..Data import Data
from ... import option


class Act(Data):
    """
    Represents act data cards.

    Attributes:
        keyword: act data card ``r'ACT'`` symbol.
        options: act data card ``options`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'ACT'] | str = abc.Terminal[r'ACT']('ACT')
    options: typing.Annotated[abc.Array, option.data.Act, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[option.data.Act | str] | str = abc.Terminal[r'']('')
