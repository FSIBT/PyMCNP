import typing
import dataclasses

import collections

from .... import abc
from ..Data import Data
from ... import option
from ... import literal


class Bfld(Data):
    """
    Represents bfld data cards.

    Attributes:
        keyword: bfld data card `BFLD` symbol.
        suffix: bfld data card `n` parameter.
        type: bfld data card `type` parameter.
        options: bfld data card `options` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'BFLD'] | str = abc.Terminal[r'BFLD']('BFLD')
    suffix: literal.Integer | int | str
    type: typing.Annotated[abc.Terminal, r'CONST|QUAD|QUADFF'] | str
    options: typing.Annotated[abc.Array, option.data.Bfld, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[option.data.Bfld | str] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates bfld data cards.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')

        if self.options != '' and not any(isinstance(keyvalue, option.data.bfld.Field) for keyvalue in self.options):
            raise abc.Error('Invalid value.', f'{self.options=}')
