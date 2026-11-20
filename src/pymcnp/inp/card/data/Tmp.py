import typing


from .... import abc
from ..Data import Data
from ... import literal


class Tmp(Data):
    """
    Represents tmp data cards.
    """

    if typing.TYPE_CHECKING:
        keyword: typing.Annotated[abc.Terminal, r'TMP']
        t: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r'']


class Tmp_0(Tmp):
    """
    Represents tmp data cards, form #0.

    Attributes:
        keyword: tmp data card ``r'TMP'`` symbol.
        suffix: tmp data card ``n`` parameter.
        t: tmp data card ``t`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'TMP'] = abc.Terminal[r'TMP']('TMP')
    suffix: literal.Integer
    t: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates tmp data cards, form #0.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 99):
            raise abc.Error('Invalid value.', f'{self.suffix=}')


class Tmp_1(Tmp):
    """
    Represents tmp data cards, form #1.

    Attributes:
        keyword: tmp data card ``r'TMP'`` symbol.
        t: tmp data card ``t`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'TMP'] = abc.Terminal[r'TMP']('TMP')
    t: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
