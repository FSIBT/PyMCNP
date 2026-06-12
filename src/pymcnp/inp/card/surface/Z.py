import typing
import decimal
import dataclasses

from .... import abc
from ..Surface import Surface
from ... import literal


class Z(Surface):
    """
    Represents z surface cards.
    """

    pass


class Z_0(Z):
    """
    Represents z surface cards, form #0.

    Attributes:
        prefix: z surface card `prefix` parameter.
        j: z surface card `j` parameter.
        n: z surface card `n` parameter.
        keyword: z surface card `Z` symbol.
        z0: z surface card `z0` parameter.
        r0: z surface card `r0` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    j: literal.Integer | int | str
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] | int | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'Z'] | str = abc.Terminal[r'Z']('Z')
    z0: literal.Real | int | float | decimal.Decimal | str
    r0: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates z surface cards, form #0.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.j, literal.Integer)
        assert isinstance(self.n, (literal.Integer, abc.Terminal[r'']))

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')


class Z_1(Z):
    """
    Represents z surface cards, form #1.

    Attributes:
        j: z surface card `j` parameter.
        n: z surface card `n` parameter.
        keyword: z surface card `Z` symbol.
        z0: z surface card `z0` parameter.
        r0: z surface card `r0` parameter.
        z1: z surface card `z1` parameter.
        r1: z surface card `r1` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    j: literal.Integer | int | str
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] | int | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'Z'] | str = abc.Terminal[r'Z']('Z')
    z0: literal.Real | int | float | decimal.Decimal | str
    r0: literal.Real | int | float | decimal.Decimal | str
    z1: literal.Real | int | float | decimal.Decimal | str
    r1: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates z surface cards, form #1.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.j, literal.Integer)
        assert isinstance(self.n, (literal.Integer, abc.Terminal[r'']))

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')


class Z_2(Z):
    """
    Represents z surface cards, form #2.

    Attributes:
        j: z surface card `j` parameter.
        n: z surface card `n` parameter.
        keyword: z surface card `Z` symbol.
        z0: z surface card `z0` parameter.
        r0: z surface card `r0` parameter.
        z1: z surface card `z1` parameter.
        r1: z surface card `r1` parameter.
        z2: z surface card `z2` parameter.
        r2: z surface card `r2` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    j: literal.Integer | int | str
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] | int | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'Z'] | str = abc.Terminal[r'Z']('Z')
    z0: literal.Real | int | float | decimal.Decimal | str
    r0: literal.Real | int | float | decimal.Decimal | str
    z1: literal.Real | int | float | decimal.Decimal | str
    r1: literal.Real | int | float | decimal.Decimal | str
    z2: literal.Real | int | float | decimal.Decimal | str
    r2: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates z surface cards, form #2.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.j, literal.Integer)
        assert isinstance(self.n, (literal.Integer, abc.Terminal[r'']))

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')
