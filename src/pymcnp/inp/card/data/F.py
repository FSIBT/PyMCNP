import typing
import dataclasses

import collections


from .... import abc
from ..Data import Data
from ... import literal
from ... import group


class F(Data):
    """
    Represents f data cards.
    """

    pass


class F_0(F):
    """
    Represents f data cards, form #0.

    Attributes:
        prefix: f data card `prefix` parameter.
        keyword: f data card `F` symbol.
        suffix: f data card `n` parameter.
        colon: f data card `:` symbol.
        particle: f data card `particle` parameter.
        s: f data card `s` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'\+'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'F'] | str = abc.Terminal[r'F']('F')
    suffix: literal.Integer | int | str
    colon: typing.Annotated[abc.Terminal, r':'] | str = abc.Terminal[r':'](':')
    particle: literal.Particle | str
    s: typing.Annotated[abc.Array, group.ParenthesizedIntegers | literal.Real, None] | collections.abc.Sequence[int | str] | str = abc.Terminal[r'']('')
    t: typing.Annotated[abc.Terminal, r'T'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates f data cards, form #0.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')


class F_1(F):
    """
    Represents f data cards, form #1.

    Attributes:
        keyword: f data card `F` symbol.
        suffix: f data card `n` parameter.
        colon: f data card `:` symbol.
        particle: f data card `particle` parameter.
        x_y_z_ro: f data card `x_y_z_ro` parameter.
        nd: f data card `ND` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'F'] | str = abc.Terminal[r'F']('F')
    suffix: literal.Integer | int | str
    colon: typing.Annotated[abc.Terminal, r':'] | str = abc.Terminal[r':'](':')
    particle: literal.Particle | str
    x_y_z_ro: typing.Annotated[abc.Array, group.Xyzro, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[group.Xyzro | str] | str = abc.Terminal[r'']('')
    nd: typing.Annotated[abc.Terminal, r'ND'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates f data cards, form #1.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')


class F_2(F):
    """
    Represents f data cards, form #2.

    Attributes:
        keyword: f data card `F` symbol.
        suffix: f data card `n` parameter.
        suffix_a: f data card `a` parameter.
        colon: f data card `:` symbol.
        particle: f data card `particle` parameter.
        ao_r_ro: f data card `ao_r_ro` parameter.
        nd: f data card `ND` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'F'] | str = abc.Terminal[r'F']('F')
    suffix: literal.Integer | int | str
    suffix_a: typing.Annotated[abc.Terminal, r'X|Y|Z'] | str
    colon: typing.Annotated[abc.Terminal, r':'] | str = abc.Terminal[r':'](':')
    particle: literal.Particle | str
    ao_r_ro: typing.Annotated[abc.Array, group.Aorro, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[group.Aorro | str] | str = abc.Terminal[r'']('')
    nd: typing.Annotated[abc.Terminal, r'ND'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates f data cards, form #2.
        """

        assert isinstance(self.suffix, literal.Integer)

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
