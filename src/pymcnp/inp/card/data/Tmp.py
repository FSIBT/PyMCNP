import typing
import decimal
import collections
import dataclasses


from .... import abc
from ..Data import Data
from ... import literal


class Tmp(Data):
    """
    Represents tmp data cards.
    """

    pass


class Tmp_0(Tmp):
    """
    Represents tmp data cards, form #0.

    Attributes:
        keyword: tmp data card `TMP` symbol.
        suffix: tmp data card `n` parameter.
        t: tmp data card `t` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'TMP'] | str = abc.Terminal[r'TMP']('TMP')
    suffix: literal.Integer | int | str
    t: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )

    def __post_init__(self) -> None:
        """
        Validates tmp data cards, form #0.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (1 <= self.suffix <= 99):
            raise abc.Error('Invalid value.', f'{self.suffix=}')


class Tmp_1(Tmp):
    """
    Represents tmp data cards, form #1.

    Attributes:
        keyword: tmp data card `TMP` symbol.
        t: tmp data card `t` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'TMP'] | str = abc.Terminal[r'TMP']('TMP')
    t: typing.Annotated[abc.Array, literal.Real, None] | collections.abc.Sequence[int | float | decimal.Decimal | str] | str
