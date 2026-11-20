import typing


from .... import abc
from ... import literal
from ..Data import Data


class Si(Data):
    """
    Represents si data cards.

    Attributes:
        keyword: si data card ``r'SI'`` symbol.
        suffix: si data card ``n`` parameter.
        option: si data card ``option`` parameter.
        i: si data card ``i`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'SI'] = abc.Terminal[r'SI']('SI')
    suffix: literal.Integer
    option: typing.Annotated[abc.Terminal, r'H|L|A|S'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    i: typing.Annotated[abc.Array, literal.Distribution, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates si data cards.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
