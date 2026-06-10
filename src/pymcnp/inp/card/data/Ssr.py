import typing
import dataclasses

import collections

from .... import abc
from ..Data import Data
from ... import option


class Ssr(Data):
    """
    Represents ssr data cards.

    Attributes:
        keyword: ssr data card `SSR` symbol.
        options: ssr data card `options` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'SSR'] | str = abc.Terminal[r'SSR']('SSR')
    options: typing.Annotated[abc.Array, option.data.Ssr, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[option.data.Ssr | str] | str = abc.Terminal[r'']('')
