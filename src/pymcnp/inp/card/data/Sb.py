import typing


from .... import abc
from ..Data import Data
from ... import literal


class Sb(Data):
    """
    Represents sb data cards.
    """

    if typing.TYPE_CHECKING:
        keyword: typing.Annotated[abc.Terminal, r'SB']
        option: typing.Annotated[abc.Terminal, r'D|C|V|W'] | typing.Annotated[abc.Terminal, r'']


class Sb_0(Sb):
    """
    Represents sb data cards, form #0.

    Attributes:
        keyword: sb data card ``r'SB'`` symbol.
        suffix: sb data card ``n`` parameter.
        option: sb data card ``option`` parameter.
        b: sb data card ``b`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'SB'] = abc.Terminal[r'SB']('SB')
    suffix: literal.Integer
    option: typing.Annotated[abc.Terminal, r'D|C|V|W'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    b: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates sb data cards, form #0.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')

        # Probabilities are relative, as MCNP normalizes them, so they may exceed 1.
        if not isinstance(self.b, abc.Terminal) and not all(0 <= bi for bi in self.b):
            raise abc.Error('Invalid value.', f'{self.b=}')


class Sb_1(Sb):
    """
    Represents sb data cards, form #1.

    Attributes:
        keyword: sb data card ``r'SB'`` symbol.
        suffix: sb data card ``n`` parameter.
        f: sb data card ``f`` parameter, the number of a built-in function, e.g., ``-21``.
        a: sb data card ``a`` parameter, empty for the function's default.
        b: sb data card ``b`` parameter, empty for the function's default.
    """

    keyword: typing.Annotated[abc.Terminal, r'SB'] = abc.Terminal[r'SB']('SB')
    suffix: literal.Integer
    f: literal.Integer
    a: literal.Real | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    b: literal.Real | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates sb data cards, form #1.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')

        if self.f >= 0:
            raise abc.Error('Invalid value.', f'{self.f=}')
