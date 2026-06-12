import typing
import decimal
import collections
import dataclasses


from .... import abc
from ..Data import Data
from ... import literal
from ... import option


class T(Data):
    """
    Represents t data cards.
    """

    pass


class T_0(T):
    """
    Represents t data cards, form #0.

    Attributes:
        keyword: t data card `T` symbol.
        suffix: t data card `n` parameter.
        t: t data card `t` parameter.
        nt: t data card `NT` symbol.
        c: t data card `C` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'T'] | str = abc.Terminal[r'T']('T')
    suffix: literal.Integer | int | str
    t: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )
    nt: typing.Annotated[abc.Terminal, r'NT'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    c: typing.Annotated[abc.Terminal, r'C'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates t data cards, form #0.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')


class T_1(T):
    """
    Represents t data cards, form #1.

    Attributes:
        keyword: t data card `T` symbol.
        suffix: t data card `n` parameter.
        options: t data card `options` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'T'] | str = abc.Terminal[r'T']('T')
    suffix: literal.Integer | int | str
    options: typing.Annotated[abc.Array, option.data.T, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[option.data.T | str] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates t data cards, form #1.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
