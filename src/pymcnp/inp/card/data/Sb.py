import typing
import decimal
import collections
import dataclasses


from .... import abc
from ..Data import Data
from ... import literal


class Sb(Data):
    """
    Represents sb data cards.
    """

    pass


class Sb_0(Sb):
    """
    Represents sb data cards, form #0.

    Attributes:
        keyword: sb data card `SB` symbol.
        suffix: sb data card `n` parameter.
        option: sb data card `option` parameter.
        b: sb data card `b` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'SB'] | str = abc.Terminal[r'SB']('SB')
    suffix: literal.Integer | int | str
    option: typing.Annotated[abc.Terminal, r'D|C|V|W'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    b: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )

    def __post_init__(self) -> None:
        """
        Validates sb data cards, form #0.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.suffix, literal.Integer)
        assert isinstance(self.b, (abc.Array, abc.Terminal[r'']))
        assert not isinstance(self.b, abc.Array) or all(isinstance(bi, literal.Real) for bi in self.b)

        if not (1 <= self.suffix <= 999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')

        if not isinstance(self.b, abc.Terminal) and not all(0 <= bi <= 1 for bi in self.b):
            raise abc.Error('Invalid value.', f'{self.b=}')


class Sb_1(Sb):
    """
    Represents sb data cards, form #1.

    Attributes:
        keyword: sb data card `SB` symbol.
        suffix: sb data card `n` parameter.
        f: sb data card `f` parameter.
        a: sb data card `a` parameter.
        b: sb data card `b` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'SB'] | str = abc.Terminal[r'SB']('SB')
    suffix: literal.Integer | int | str
    f: literal.Integer | int | str
    a: literal.Real | int | float | decimal.Decimal | str
    b: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates sb data cards, form #1.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (1 <= self.suffix <= 999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
