import typing
import dataclasses

import collections
from .... import abc
from ... import option
from ..Data import Data


class Stop(Data):
    """
    Represents stop data cards.

    Attributes:
        keyword: stop data card `STOP` symbol.
        options: stop data card `options` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'STOP'] | str = abc.Terminal[r'STOP']('STOP')
    options: typing.Annotated[abc.Array, option.data.Stop, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[option.data.Stop | str] | str = abc.Terminal[r'']('')
