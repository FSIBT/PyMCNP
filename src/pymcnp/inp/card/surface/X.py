import typing
import decimal
import dataclasses

from .... import abc
from ..Surface import Surface
from ... import literal


class X(Surface):
    """
    Represents x surface cards.
    """

    pass


class X_0(X):
    """
    Represents x surface cards, form #0.

    Attributes:
        prefix: x surface card `prefix` parameter.
        j: x surface card `j` parameter.
        n: x surface card `n` parameter.
        keyword: x surface card `X` symbol.
        x0: x surface card `x0` parameter.
        r0: x surface card `r0` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    j: literal.Integer | int | str
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] | int | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'X'] | str = abc.Terminal[r'X']('X')
    x0: literal.Real | int | float | decimal.Decimal | str
    r0: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates x surface cards, form #2.
        """

        assert isinstance(self.j, literal.Integer)
        assert isinstance(self.n, (literal.Integer, abc.Terminal[r'']))

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')


class X_1(X):
    """
    Represents x surface cards, form #1.

    Attributes:
        j: x surface card `j` parameter.
        n: x surface card `n` parameter.
        keyword: x surface card `X` symbol.
        x0: x surface card `x0` parameter.
        r0: x surface card `r0` parameter.
        x1: x surface card `x1` parameter.
        r1: x surface card `r1` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    j: literal.Integer | int | str
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] | int | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'X'] | str = abc.Terminal[r'X']('X')
    x0: literal.Real | int | float | decimal.Decimal | str
    r0: literal.Real | int | float | decimal.Decimal | str
    x1: literal.Real | int | float | decimal.Decimal | str
    r1: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates x surface cards, form #1.
        """

        assert isinstance(self.j, literal.Integer)
        assert isinstance(self.n, (literal.Integer, abc.Terminal[r'']))

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')


class X_2(X):
    """
    Represents x surface cards, form #2.

    Attributes:
        j: x surface card `j` parameter.
        n: x surface card `n` parameter.
        keyword: x surface card `X` symbol.
        x0: x surface card `x0` parameter.
        r0: x surface card `r0` parameter.
        x1: x surface card `x1` parameter.
        r1: x surface card `r1` parameter.
        x2: x surface card `x2` parameter.
        r2: x surface card `r2` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    j: literal.Integer | int | str
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] | int | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'X'] | str = abc.Terminal[r'X']('X')
    x0: literal.Real | int | float | decimal.Decimal | str
    r0: literal.Real | int | float | decimal.Decimal | str
    x1: literal.Real | int | float | decimal.Decimal | str
    r1: literal.Real | int | float | decimal.Decimal | str
    x2: literal.Real | int | float | decimal.Decimal | str
    r2: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates x surface cards, form #0.
        """

        assert isinstance(self.j, literal.Integer)
        assert isinstance(self.n, (literal.Integer, abc.Terminal[r'']))

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')
