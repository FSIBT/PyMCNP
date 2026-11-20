import typing
import dataclasses


from .... import abc
from ... import literal
from ..Data import Data


class Fill(Data):
    """
    Represents fill data cards.

    Attributes:
        keyword: fill data card ``r'FILL'`` symbol.
        n: fill data card ``n`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'FILL'] = abc.Terminal[r'FILL']('FILL')
    n: typing.Annotated[abc.Array, literal.Integer | literal.Jump, None] | typing.Annotated[abc.Terminal, r''] = dataclasses.field(kw_only=True)

    def __post_init__(self) -> None:
        """
        Validates fill data cards.

        Raises:
            Error: Invalid value.
        """

        if isinstance(self.n, abc.Array) and not all(0 <= nj <= 99_999_999 for nj in self.n):
            raise abc.Error('Invalid value.', f'{self.n=}')
