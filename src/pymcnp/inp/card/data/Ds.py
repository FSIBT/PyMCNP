import typing
import dataclasses

import collections


from .... import abc
from ..Data import Data
from ... import literal
from ... import group


class Ds(Data):
    """
    Represents ds data cards.
    """

    pass


class Ds_0(Ds):
    """
    Represents ds data cards, form #0.

    Attributes:
        keyword: ds data card `DS` symbol.
        suffix: ds data card `n` parameter.
        option: ds data card `option` parameter.
        j: ds data card `j` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'DS'] | str = abc.Terminal[r'DS']('DS')
    suffix: literal.Integer | int | str
    option: typing.Annotated[abc.Terminal, r'H|L|S'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    j: (
        typing.Annotated[abc.Array, literal.Distribution | typing.Annotated[abc.Terminal, r'0'], None]
        | typing.Annotated[abc.Terminal, r'']
        | collections.abc.Sequence[literal.Distribution | typing.Annotated[abc.Terminal, r'0'] | str]
        | str
    ) = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates ds data cards, form #0.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (1 <= self.suffix <= 999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')


class Ds_1(Ds):
    """
    Represents ds data cards, form #1.

    Attributes:
        keyword: ds data card `DS` symbol.
        suffix: ds data card `n` parameter.
        t: ds data card `T` symbol.
        i_j: ds data card `i_j` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'DS'] | str = abc.Terminal[r'DS']('DS')
    suffix: literal.Integer | int | str
    t: typing.Annotated[abc.Terminal, r'T'] | str = abc.Terminal[r'T']('T')
    i_j: typing.Annotated[abc.Array, group.I_J, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[group.I_J | str] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates ds data cards, form #1.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (1 <= self.suffix <= 999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')


class Ds_2(Ds):
    """
    Represents ds data cards, form #2.

    Attributes:
        keyword: ds data card `DS` symbol.
        suffix: ds data card `n` parameter.
        q: ds data card `Q` symbol.
        v_s: ds data card `v_s` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'DS'] | str = abc.Terminal[r'DS']('DS')
    suffix: literal.Integer | int | str
    q: typing.Annotated[abc.Terminal, r'Q'] | str = abc.Terminal[r'Q']('Q')
    v_s: typing.Annotated[abc.Array, group.V_S, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[group.V_S | str] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates ds data cards, form #2.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (1 <= self.suffix <= 999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
