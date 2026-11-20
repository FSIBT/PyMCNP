import typing


from .... import abc
from ..Data import Data
from ... import literal
from ... import group


class F(Data):
    """
    Represents f data cards.
    """

    if typing.TYPE_CHECKING:
        prefix: typing.Annotated[abc.Terminal, r'\+'] | typing.Annotated[abc.Terminal, r'']
        keyword: typing.Annotated[abc.Terminal, r'F']
        suffix: literal.Integer
        colon: typing.Annotated[abc.Terminal, r':']
        particle: literal.Particle


class F_0(F):
    """
    Represents f data cards, form #0.

    Attributes:
        prefix: f data card ``prefix`` parameter.
        keyword: f data card ``r'F'`` symbol.
        suffix: f data card ``n`` parameter.
        colon: f data card ``r':'`` symbol.
        particle: f data card ``particle`` parameter.
        s: f data card ``s`` parameter.
    """

    prefix: typing.Annotated[abc.Terminal, r'\+'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'F'] = abc.Terminal[r'F']('F')
    suffix: literal.Integer
    colon: typing.Annotated[abc.Terminal, r':'] = abc.Terminal[r':'](':')
    particle: literal.Particle
    s: typing.Annotated[abc.Array, group.ParenthesizedIntegers | literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    t: typing.Annotated[abc.Terminal, r'T'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates f data cards, form #0.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')


class F_1(F):
    """
    Represents f data cards, form #1.

    Attributes:
        keyword: f data card ``r'F'`` symbol.
        suffix: f data card ``n`` parameter.
        colon: f data card ``r':'`` symbol.
        particle: f data card ``particle`` parameter.
        x_y_z_ro: f data card ``x_y_z_ro`` parameter.
        nd: f data card ``r'ND'`` symbol.
    """

    keyword: typing.Annotated[abc.Terminal, r'F'] = abc.Terminal[r'F']('F')
    suffix: literal.Integer
    colon: typing.Annotated[abc.Terminal, r':'] = abc.Terminal[r':'](':')
    particle: literal.Particle
    x_y_z_ro: typing.Annotated[abc.Array, group.Xyzro, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    nd: typing.Annotated[abc.Terminal, r'ND'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates f data cards, form #1.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')


class F_2(F):
    """
    Represents f data cards, form #2.

    Attributes:
        keyword: f data card ``r'F'`` symbol.
        suffix: f data card ``n`` parameter.
        suffix_a: f data card ``a`` parameter.
        colon: f data card ``r':'`` symbol.
        particle: f data card ``particle`` parameter.
        ao_r_ro: f data card ``ao_r_ro`` parameter.
        nd: f data card ``r'ND'`` symbol.
    """

    keyword: typing.Annotated[abc.Terminal, r'F'] = abc.Terminal[r'F']('F')
    suffix: literal.Integer
    suffix_a: typing.Annotated[abc.Terminal, r'X|Y|Z']
    colon: typing.Annotated[abc.Terminal, r':'] = abc.Terminal[r':'](':')
    particle: literal.Particle
    ao_r_ro: typing.Annotated[abc.Array, group.Aorro, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    nd: typing.Annotated[abc.Terminal, r'ND'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates f data cards, form #2.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')
