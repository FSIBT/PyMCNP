import typing
import decimal
import collections
import dataclasses


from .... import abc
from ..Data import Data
from ... import literal


class Sp(Data):
    """
    Represents sp data cards.
    """

    pass


class Sp_0(Sp):
    """
    Represents sp data cards, form #0.

    Attributes:
        keyword: sp data card `SP` symbol.
        suffix: sp data card `n` parameter.
        option: sp data card `option` parameter.
        p: sp data card `p` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'SP'] | str = abc.Terminal[r'SP']('SP')
    suffix: literal.Integer | int | str
    option: typing.Annotated[abc.Terminal, r'D|C|V|W'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    p: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )

    def __post_init__(self) -> None:
        """
        Validates sp data cards, form #0.
        """

        assert isinstance(self.suffix, literal.Integer)
        assert isinstance(self.p, (abc.Array, abc.Terminal[r'']))

        if not (1 <= self.suffix <= 999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')

        if isinstance(self.p, abc.Array) and not all(0 <= pi <= 1 for pi in self.p):
            raise abc.Error('Invalid value.', f'{self.p=}')


class Sp_1(Sp):
    """
    Represents sp data cards, form #1.

    Attributes:
        keyword: sp data card `SP` symbol.
        suffix: sp data card `n` parameter.
        f: sp data card `f` parameter.
        a: sp data card `a` parameter.
        b: sp data card `b` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'SP'] | str = abc.Terminal[r'SP']('SP')
    suffix: literal.Integer | int | str
    f: literal.Integer | int | str
    a: literal.Real | int | float | decimal.Decimal | str
    b: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates sp data cards, form #1.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (1 <= self.suffix <= 999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
