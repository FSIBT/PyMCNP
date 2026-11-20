import typing


from .... import abc
from ..Data import Data
from ... import literal
from ... import option


class Df(Data):
    """
    Represents df data cards.
    """

    if typing.TYPE_CHECKING:
        keyword: typing.Annotated[abc.Terminal, r'DF'] = abc.Terminal[r'DF']('DF')
        suffix: literal.Integer


class Df_0(Df):
    """
    Represents df data cards, form #0.

    Attributes:
        keyword: df data card ``r'DF'`` symbol.
        suffix: df data card ``n`` parameter.
        b: df data card ``b`` parameter.
        f: df data card ``f`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'DF'] = abc.Terminal[r'DF']('DF')
    suffix: literal.Integer
    b: typing.Annotated[abc.Terminal, r'LOG|LIN'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    f: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates df data cards, form #0.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')


class Df_1(Df):
    """
    Represents df data cards, form #1.

    Attributes:
        keyword: df data card ``r'DF'`` symbol.
        suffix: df data card ``n`` parameter.
        options: df data card ``options`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'DF'] = abc.Terminal[r'DF']('DF')
    suffix: literal.Integer
    options: typing.Annotated[abc.Array, option.data.Df, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates df data cards, form #1.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
