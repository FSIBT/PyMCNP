import typing
import dataclasses

import collections

from .... import abc
from ..Data import Data
from ... import option


class Dbrc(Data):
    """
    Represents dbrc data cards.

    Attributes:
        keyword: dbrc data card `DBRC` symbol.
        options: dbrc data card `options` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'DBRC'] | str = abc.Terminal[r'DBRC']('DBRC')
    options: typing.Annotated[abc.Array, option.data.Dbrc, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[option.data.Dbrc | str] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates dbrc data cards.
        """

        if (
            not isinstance(self.options, abc.Terminal)
            and any(isinstance(keyvalue, option.data.dbrc.Isos) for keyvalue in self.options)
            and not any(isinstance(keyvalue, option.data.dbrc.Endf) for keyvalue in self.options)
        ):
            raise abc.Error('Invalid value.', f'{self.options=}')
