import typing
import decimal
import collections
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Cosyp(Data):
    """
    Represents cosyp data cards.

    Attributes:
        keyword: cosyp data card `COSYP` symbol.
        pre: cosyp data card `prefix` parameter.
        axsh: cosyp data card `axsh` parameter.
        axsv: cosyp data card `axsv` parameter.
        emap: cosyp data card `emap` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'COSYP'] | str = abc.Terminal[r'COSYP']('COSYP')
    pre: literal.Integer | int | str
    axsh: literal.Integer | int | str
    axsv: literal.Integer | int | str
    emap: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[
        r''
    ]('')

    def __post_init__(self) -> None:
        """
        Validates cosyp data cards.
        """

        if self.axsh not in {1, 2, 3}:
            raise abc.Error('Invalid value.', f'{self.axsh=}')

        if self.axsv not in {1, 2, 3}:
            raise abc.Error('Invalid value.', f'{self.axsv=}')
