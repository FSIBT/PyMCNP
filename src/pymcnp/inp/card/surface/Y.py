import typing

from .... import abc
from ..Surface import Surface
from ... import literal


class Y(Surface):
    """
    Represents y surface cards.
    """

    if typing.TYPE_CHECKING:
        prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r'']
        j: literal.Integer
        n: literal.Integer | typing.Annotated[abc.Terminal, r'']
        keyword: typing.Annotated[abc.Terminal, r'Y']
        y0: literal.Real
        r0: literal.Real


class Y_0(Y):
    """
    Represents y surface cards, form #0.

    Attributes:
        prefix: y surface card ``prefix`` parameter.
        j: y surface card ``j`` parameter.
        n: y surface card ``n`` parameter.
        keyword: y surface card ``r'Y'`` symbol.
        y0: y surface card ``y0`` parameter.
        r0: y surface card ``r0`` parameter.
    """

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    j: literal.Integer
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'Y'] = abc.Terminal[r'Y']('Y')
    y0: literal.Real
    r0: literal.Real

    def __post_init__(self) -> None:
        """
        Validates y surface cards, form #0.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')


class Y_1(Y):
    """
    Represents y surface cards, form #1.

    Attributes:
        prefix: y surface card ``prefix`` parameter.
        j: y surface card ``j`` parameter.
        n: y surface card ``n`` parameter.
        keyword: y surface card ``r'Y'`` symbol.
        y0: y surface card ``y0`` parameter.
        r0: y surface card ``r0`` parameter.
        y1: y surface card ``y1`` parameter.
        r1: y surface card ``r1`` parameter.
    """

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    j: literal.Integer
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'Y'] = abc.Terminal[r'Y']('Y')
    y0: literal.Real
    r0: literal.Real
    y1: literal.Real
    r1: literal.Real

    def __post_init__(self) -> None:
        """
        Validates y surface cards, form #1.
        """

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')


class Y_2(Y):
    """
    Represents y surface cards, form #0.

    Attributes:
        prefix: y surface card ``prefix`` parameter.
        j: y surface card ``j`` parameter.
        n: y surface card ``n`` parameter.
        keyword: y surface card ``r'Y'`` symbol.
        y0: y surface card ``y0`` parameter.
        r0: y surface card ``r0`` parameter.
        y1: y surface card ``y1`` parameter.
        r1: y surface card ``r1`` parameter.
        y2: y surface card ``y2`` parameter.
        r2: y surface card ``r2`` parameter.
    """

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    j: literal.Integer
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'Y'] = abc.Terminal[r'Y']('Y')
    y0: literal.Real
    r0: literal.Real
    y1: literal.Real
    r1: literal.Real
    y2: literal.Real
    r2: literal.Real

    def __post_init__(self) -> None:
        """
        Validates y surface cards, form #0.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')
