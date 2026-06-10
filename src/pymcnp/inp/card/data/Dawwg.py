import typing
import dataclasses

import collections

from .... import abc
from ..Data import Data
from ... import option


class Dawwg(Data):
    """
    Represents dawwg data cards.

    Attributes:
        keyword: dawwg data card `DAWWG` symbol.
        options: dawwg data card `options` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'DAWWG'] | str = abc.Terminal[r'DAWWG']('DAWWG')
    options: typing.Annotated[abc.Array, option.data.Dawwg, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[option.data.Dawwg | str] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates dawwg data cards.
        """

        if not isinstance(self.options, abc.Terminal) and not any(isinstance(keyvalue, option.data.dawwg.Points) for keyvalue in self.options):
            raise abc.Error('Invalid value.', f'{self.options=}')

        if not isinstance(self.options, abc.Terminal) and not any(isinstance(keyvalue, option.data.dawwg.Xsec) for keyvalue in self.options):
            raise abc.Error('Invalid value.', f'{self.options=}')
