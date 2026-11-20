import typing

from .... import abc
from ... import literal
from ..Data import Data
from ... import option


class Kpert(Data):
    """
    Represents kpert data cards.

    Attributes:
        keyword: kpert data card ``r'KPERT'`` symbol.
        suffix: kpert data card ``n`` parameter.
        options: kpert data card ``options`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'KPERT'] = abc.Terminal[r'KPERT']('KPERT')
    suffix: literal.Integer
    options: typing.Annotated[abc.Array, option.data.Kpert, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates kpert data cards.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')

        if not isinstance(self.options, abc.Terminal) and not any(isinstance(keyvalue, option.data.kpert.Cell) for keyvalue in self.options):
            raise abc.Error('Invalid value.', f'{self.options=}')
