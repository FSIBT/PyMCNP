import typing

from .... import abc
from ..Surface import Surface
from ... import literal


class X(Surface):
    """
    Represents x surface cards.
    """

    if typing.TYPE_CHECKING:
        prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r'']
        j: literal.Integer
        n: literal.Integer | typing.Annotated[abc.Terminal, r'']
        keyword: typing.Annotated[abc.Terminal, r'X']
        x0: literal.Real
        r0: literal.Real


class X_0(X):
    """
    Represents x surface cards, form #0.

    Attributes:
        prefix: x surface card ``prefix`` parameter.
        j: x surface card ``j`` parameter.
        n: x surface card ``n`` parameter.
        keyword: x surface card ``r'X'`` symbol.
        x0: x surface card ``x0`` parameter.
        r0: x surface card ``r0`` parameter.
    """

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    j: literal.Integer
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'X'] = abc.Terminal[r'X']('X')
    x0: literal.Real
    r0: literal.Real

    def __post_init__(self) -> None:
        """
        Validates x surface cards, form #0.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')


class X_1(X):
    """
    Represents x surface cards, form #1.

    Attributes:
        prefix: x surface card ``prefix`` parameter.
        j: x surface card ``j`` parameter.
        n: x surface card ``n`` parameter.
        keyword: x surface card ``r'X'`` symbol.
        x0: x surface card ``x0`` parameter.
        r0: x surface card ``r0`` parameter.
        x1: x surface card ``x1`` parameter.
        r1: x surface card ``r1`` parameter.
    """

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    j: literal.Integer
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'X'] = abc.Terminal[r'X']('X')
    x0: literal.Real
    r0: literal.Real
    x1: literal.Real
    r1: literal.Real

    def __post_init__(self) -> None:
        """
        Validates x surface cards, form #1.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')


class X_2(X):
    """
    Represents x surface cards, form #2.

    Attributes:
        prefix: x surface card ``prefix`` parameter.
        j: x surface card ``j`` parameter.
        n: x surface card ``n`` parameter.
        keyword: x surface card ``r'X'`` symbol.
        x0: x surface card ``x0`` parameter.
        r0: x surface card ``r0`` parameter.
        x1: x surface card ``x1`` parameter.
        r1: x surface card ``r1`` parameter.
        x2: x surface card ``x2`` parameter.
        r2: x surface card ``r2`` parameter.
    """

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    j: literal.Integer
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'X'] = abc.Terminal[r'X']('X')
    x0: literal.Real
    r0: literal.Real
    x1: literal.Real
    r1: literal.Real
    x2: literal.Real
    r2: literal.Real

    def __post_init__(self) -> None:
        """
        Validates x surface cards, form #2.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')
