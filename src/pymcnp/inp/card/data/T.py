import typing


from .... import abc
from ..Data import Data
from ... import literal
from ... import option


class T(Data):
    """
    Represents t data cards.
    """

    if typing.TYPE_CHECKING:
        keyword: typing.Annotated[abc.Terminal, r'T'] = abc.Terminal[r'T']('T')
        suffix: literal.Integer


class T_0(T):
    """
    Represents t data cards, form #0.

    Attributes:
        keyword: t data card ``r'T'`` symbol.
        suffix: t data card ``n`` parameter.
        t: t data card ``t`` parameter.
        nt: t data card ``r'NT'`` symbol.
        c: t data card ``r'C'`` symbol.
    """

    keyword: typing.Annotated[abc.Terminal, r'T'] = abc.Terminal[r'T']('T')
    suffix: literal.Integer
    t: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    nt: typing.Annotated[abc.Terminal, r'NT'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    c: typing.Annotated[abc.Terminal, r'C'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates t data cards, form #0.

        Raises:
            Error: Invalid value.
        """

        if not (0 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')


class T_1(T):
    """
    Represents t data cards, form #1.

    Attributes:
        keyword: t data card ``r'T'`` symbol.
        suffix: t data card ``n`` parameter.
        options: t data card ``options`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'T'] = abc.Terminal[r'T']('T')
    suffix: literal.Integer
    options: typing.Annotated[abc.Array, option.data.T, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates t data cards, form #1.

        Raises:
            Error: Invalid value.
        """

        if not (0 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
