import typing
import dataclasses


from .... import abc
from ... import literal
from ..Data import Data


class Lat(Data):
    """
    Represents lat data cards.

    Attributes:
        keyword: lat data card ``r'LAT'`` symbol.
        n: lat data card ``n`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'LAT'] = abc.Terminal[r'LAT']('LAT')
    n: typing.Annotated[abc.Array, literal.Integer | literal.Jump, None] | typing.Annotated[abc.Terminal, r''] = dataclasses.field(kw_only=True)

    def __post_init__(self) -> None:
        """
        Validates lat data cards.

        Raises:
            Error: Invalid value.
        """

        if not isinstance(self.n, abc.Terminal) and not all(nj in {1, 2} for nj in self.n):
            raise abc.Error('Invalid value.', f'{self.n=}')
