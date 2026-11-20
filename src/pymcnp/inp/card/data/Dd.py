import typing


from .... import abc
from ... import literal
from ... import group
from ..Data import Data


class Dd(Data):
    """
    Represents dd data cards.

    Attributes:
        keyword: dd data card ``r'DD'`` symbol.
        suffix: dd data card ``n`` parameter.
        k_m: dd data card ``k_m`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'DD'] = abc.Terminal[r'DD']('DD')
    suffix: literal.Integer
    k_m: typing.Annotated[abc.Array, group.Criterion, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates dd data cards.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
