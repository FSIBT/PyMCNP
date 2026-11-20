import typing


from .... import abc
from ... import literal
from ..Data import Data


class Fq(Data):
    """
    Represents fq data cards.

    Attributes:
        keyword: fq data card ``r'FQ'`` symbol.
        suffix: fq data card ``n`` parameter.
        a: fq data card ``a`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'FQ'] = abc.Terminal[r'FQ']('FQ')
    suffix: literal.Integer
    a: typing.Annotated[abc.Array, typing.Annotated[abc.Terminal, r'F|D|U|S|M|C|E|T'], None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates fq data cards.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')

        if not isinstance(self.a, abc.Terminal) and not 1 <= len(self.a) <= 8:
            raise abc.Error('Invalid value.', f'{self.a=}')
