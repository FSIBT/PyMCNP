import typing
import decimal
import dataclasses

from .... import abc
from ..Surface import Surface
from ... import literal


class Y(Surface):
    """
    Represents y surface cards.
    """

    pass


class Y_0(Y):
    """
    Represents y surface cards, form #0.

    Attributes:
        prefix: y surface card `prefix` parameter.
        j: y surface card `j` parameter.
        n: y surface card `n` parameter.
        keyword: y surface card `Y` symbol.
        y0: y surface card `y0` parameter.
        r0: y surface card `r0` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    j: literal.Integer | int | str
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] | int | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'Y'] | str = abc.Terminal[r'Y']('Y')
    y0: literal.Real | int | float | decimal.Decimal | str
    r0: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates y surface cards, form #2.
        """

        assert isinstance(self.j, literal.Integer)
        assert isinstance(self.n, (literal.Integer, abc.Terminal[r'']))

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')


class Y_1(Y):
    """
    Represents y surface cards, form #1.

    Attributes:
        j: y surface card `j` parameter.
        n: y surface card `n` parameter.
        keyword: y surface card `Y` symbol.
        y0: y surface card `y0` parameter.
        r0: y surface card `r0` parameter.
        y1: y surface card `y1` parameter.
        r1: y surface card `r1` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    j: literal.Integer | int | str
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] | int | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'Y'] | str = abc.Terminal[r'Y']('Y')
    y0: literal.Real | int | float | decimal.Decimal | str
    r0: literal.Real | int | float | decimal.Decimal | str
    y1: literal.Real | int | float | decimal.Decimal | str
    r1: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates y surface cards, form #1.
        """

        assert isinstance(self.j, literal.Integer)
        assert isinstance(self.n, (literal.Integer, abc.Terminal[r'']))

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')


class Y_2(Y):
    """
    Represents y surface cards, form #2.

    Attributes:
        j: y surface card `j` parameter.
        n: y surface card `n` parameter.
        keyword: y surface card `Y` symbol.
        y0: y surface card `y0` parameter.
        r0: y surface card `r0` parameter.
        y1: y surface card `y1` parameter.
        r1: y surface card `r1` parameter.
        y2: y surface card `y2` parameter.
        r2: y surface card `r2` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    j: literal.Integer | int | str
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] | int | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'Y'] | str = abc.Terminal[r'Y']('Y')
    y0: literal.Real | int | float | decimal.Decimal | str
    r0: literal.Real | int | float | decimal.Decimal | str
    y1: literal.Real | int | float | decimal.Decimal | str
    r1: literal.Real | int | float | decimal.Decimal | str
    y2: literal.Real | int | float | decimal.Decimal | str
    r2: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates y surface cards, form #0.
        """

        assert isinstance(self.j, literal.Integer)
        assert isinstance(self.n, (literal.Integer, abc.Terminal[r'']))

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')
