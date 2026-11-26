import typing


from .... import abc
from ..Data import Data
from ... import literal
from ... import group


class F(Data):
    """
    Represents f data cards, the standard tallies.

    ``F_0`` is the F1, F2, F4, F6, F7 and F8 tallies (``Fn:pl s1 ... sk``), ``F_1`` the F5 point detector
    (``F5:pl x y z ro``) and ``F_2`` the F5 ring detector (``F5a:pl ao r ro``); the last digit of the
    ``suffix`` is the tally type, e.g., ``14`` is an F4 tally.
    """

    if typing.TYPE_CHECKING:
        prefix: typing.Annotated[abc.Terminal, r'\+'] | typing.Annotated[abc.Terminal, r'']
        keyword: typing.Annotated[abc.Terminal, r'F']
        suffix: literal.Integer
        colon: typing.Annotated[abc.Terminal, r':']
        particle: literal.Particle


class F_0(F):
    """
    Represents f data cards, form #0: the F1, F2, F4, F6, F7 and F8 tallies, ``Fn:pl s1 ... sk [T]``.

    E.g., ``F_0(suffix=4, particle='n', s=[2])`` is ``F4:n 2``, the neutron flux in cell 2.

    Attributes:
        prefix: f data card ``prefix`` parameter, ``+`` for +F6, the energy deposition of all particles.
        keyword: f data card ``r'F'`` symbol.
        suffix: f data card ``n`` parameter, the tally number, whose last digit is the tally type.
        colon: f data card ``r':'`` symbol.
        particle: f data card ``particle`` parameter.
        s: f data card ``s`` parameter, the surfaces or cells.
        t: f data card ``r'T'`` symbol, which adds the total over the surfaces or cells.
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
    Represents f data cards, form #1: the F5 point detector tally, ``F5:pl x y z ro [ND]``.

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
    Represents f data cards, form #2: the F5 ring detector tally, ``F5a:pl ao r ro [ND]``, with ``a`` X, Y or Z.

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
