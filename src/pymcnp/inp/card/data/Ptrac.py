import typing

import collections

from .... import abc
from ..Data import Data
from ... import option


class Ptrac(Data):
    """
    Represents ptrac data cards.

    Attributes:
        keyword: ptrac data card ``r'PTRAC'`` symbol.
        options: ptrac data card ``options`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'PTRAC'] | str = abc.Terminal[r'PTRAC']('PTRAC')
    options: typing.Annotated[abc.Array, option.data.Ptrac, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[option.data.Ptrac | str] | str = abc.Terminal[r'']('')
