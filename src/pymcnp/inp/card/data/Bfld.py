import typing


from .... import abc
from ..Data import Data
from ... import option
from ... import literal


class Bfld(Data):
    """
    Represents bfld data cards.

    Attributes:
        keyword: bfld data card ``r'BFLD'`` symbol.
        suffix: bfld data card ``n`` parameter.
        type: bfld data card ``type`` parameter.
        options: bfld data card ``options`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'BFLD'] = abc.Terminal[r'BFLD']('BFLD')
    suffix: literal.Integer
    type: typing.Annotated[abc.Terminal, r'CONST|QUAD|QUADFF']
    options: typing.Annotated[abc.Array, option.data.Bfld, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates bfld data cards.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')

        if self.options != '' and not any(isinstance(keyvalue, option.data.bfld.Field) for keyvalue in self.options):
            raise abc.Error('Invalid value.', f'{self.options=}')
