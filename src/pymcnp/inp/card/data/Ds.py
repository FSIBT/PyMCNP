import typing


from .... import abc
from ..Data import Data
from ... import literal
from ... import group


class Ds(Data):
    """
    Represents ds data cards.
    """

    if typing.TYPE_CHECKING:
        keyword: typing.Annotated[abc.Terminal, r'DS']
        suffix: literal.Integer


class Ds_0(Ds):
    """
    Represents ds data cards, form #0.

    Attributes:
        keyword: ds data card ``r'DS'`` symbol.
        suffix: ds data card ``n`` parameter.
        option: ds data card ``option`` parameter.
        j: ds data card ``j`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'DS'] = abc.Terminal[r'DS']('DS')
    suffix: literal.Integer
    option: typing.Annotated[abc.Terminal, r'H|L|S'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    j: typing.Annotated[abc.Array, literal.Distribution | typing.Annotated[abc.Terminal, r'0'], None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates ds data cards, form #0.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')


class Ds_1(Ds):
    """
    Represents ds data cards, form #1.

    Attributes:
        keyword: ds data card ``r'DS'`` symbol.
        suffix: ds data card ``n`` parameter.
        t: ds data card ``r'T'`` symbol.
        i_j: ds data card ``i_j`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'DS'] = abc.Terminal[r'DS']('DS')
    suffix: literal.Integer
    t: typing.Annotated[abc.Terminal, r'T'] = abc.Terminal[r'T']('T')
    i_j: typing.Annotated[abc.Array, group.I_J, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates ds data cards, form #1.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')


class Ds_2(Ds):
    """
    Represents ds data cards, form #2.

    Attributes:
        keyword: ds data card ``r'DS'`` symbol.
        suffix: ds data card ``n`` parameter.
        q: ds data card ``r'Q'`` symbol.
        v_s: ds data card ``v_s`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'DS'] = abc.Terminal[r'DS']('DS')
    suffix: literal.Integer
    q: typing.Annotated[abc.Terminal, r'Q'] = abc.Terminal[r'Q']('Q')
    v_s: typing.Annotated[abc.Array, group.V_S, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates ds data cards, form #2.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
