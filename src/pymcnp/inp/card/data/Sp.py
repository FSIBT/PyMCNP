import typing


from .... import abc
from ..Data import Data
from ... import literal


class Sp(Data):
    """
    Represents sp data cards.
    """

    if typing.TYPE_CHECKING:
        keyword: typing.Annotated[abc.Terminal, r'SP']
        suffix: literal.Integer
        option: typing.Annotated[abc.Terminal, r'D|C|V|W'] | typing.Annotated[abc.Terminal, r'']
        p: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r'']


class Sp_0(Sp):
    """
    Represents sp data cards, form #0.

    Attributes:
        keyword: sp data card ``r'SP'`` symbol.
        suffix: sp data card ``n`` parameter.
        option: sp data card ``option`` parameter.
        p: sp data card ``p`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'SP'] = abc.Terminal[r'SP']('SP')
    suffix: literal.Integer
    option: typing.Annotated[abc.Terminal, r'D|C|V|W'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    p: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates sp data cards, form #0.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')

        if isinstance(self.p, abc.Array) and not all(0 <= pi <= 1 for pi in self.p):
            raise abc.Error('Invalid value.', f'{self.p=}')


class Sp_1(Sp):
    """
    Represents sp data cards, form #1.

    Attributes:
        keyword: sp data card ``r'SP'`` symbol.
        suffix: sp data card ``n`` parameter.
        f: sp data card ``f`` parameter.
        a: sp data card ``a`` parameter.
        b: sp data card ``b`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'SP'] = abc.Terminal[r'SP']('SP')
    suffix: literal.Integer
    f: literal.Integer
    a: literal.Real
    b: literal.Real

    def __post_init__(self) -> None:
        """
        Validates sp data cards, form #1.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
