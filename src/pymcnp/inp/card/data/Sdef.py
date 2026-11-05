import typing

import collections

from .... import abc
from ..Data import Data
from ... import option


class Sdef(Data):
    """
    Represents sdef data cards.

    Attributes:
        keyword: sdef data card ``r'SDEF'`` symbol.
        options: sdef data card ``options`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'SDEF'] | str = abc.Terminal[r'SDEF']('SDEF')
    options: typing.Annotated[abc.Array, option.data.Sdef, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[option.data.Sdef | str] | str = abc.Terminal[r'']('')
