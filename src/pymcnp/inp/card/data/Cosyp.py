import typing

from .... import abc
from ... import literal
from ..Data import Data


class Cosyp(Data):
    """
    Represents cosyp data cards.

    Attributes:
        keyword: cosyp data card ``r'COSYP'`` symbol.
        pre: cosyp data card ``prefix`` parameter.
        axsh: cosyp data card ``axsh`` parameter.
        axsv: cosyp data card ``axsv`` parameter.
        emap: cosyp data card ``emap`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'COSYP'] = abc.Terminal[r'COSYP']('COSYP')
    pre: literal.Integer
    axsh: literal.Integer
    axsv: literal.Integer
    emap: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates cosyp data cards.

        Raises:
            Error: Invalid value.
        """

        if self.axsh not in {1, 2, 3}:
            raise abc.Error('Invalid value.', f'{self.axsh=}')

        if self.axsv not in {1, 2, 3}:
            raise abc.Error('Invalid value.', f'{self.axsv=}')
