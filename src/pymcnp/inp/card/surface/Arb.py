import typing
import decimal
import collections
import dataclasses

from .... import abc
from ... import literal
from ..Surface import Surface


class Arb(Surface):
    """
    Represents arb surface cards.

    Attributes:
        prefix: arb surface card `prefix` parameter.
        j: arb surface card `j` parameter.
        keyword: arb surface card `ARB` symbol.
        ax: arb surface card `ax` parameter.
        ay: arb surface card `ay` parameter.
        az: arb surface card `az` parameter.
        bx: arb surface card `bx` parameter.
        by: arb surface card `by` parameter.
        bz: arb surface card `bz` parameter.
        cx: arb surface card `cx` parameter.
        cy: arb surface card `cy` parameter.
        cz: arb surface card `cz` parameter.
        dx: arb surface card `dx` parameter.
        dy: arb surface card `dy` parameter.
        dz: arb surface card `dz` parameter.
        ex: arb surface card `ex` parameter.
        ey: arb surface card `ey` parameter.
        ez: arb surface card `ez` parameter.
        fx: arb surface card `fx` parameter.
        fy: arb surface card `fy` parameter.
        fz: arb surface card `fz` parameter.
        gx: arb surface card `gx` parameter.
        gy: arb surface card `gy` parameter.
        gz: arb surface card `gz` parameter.
        hx: arb surface card `hx` parameter.
        hy: arb surface card `hy` parameter.
        hz: arb surface card `hz` parameter.
        ni: arb surface card `ni` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    j: literal.Integer | int | str
    keyword: typing.Annotated[abc.Terminal, r'ARB'] | str = abc.Terminal[r'ARB']('ARB')
    ax: literal.Real | int | float | decimal.Decimal | str
    ay: literal.Real | int | float | decimal.Decimal | str
    az: literal.Real | int | float | decimal.Decimal | str
    bx: literal.Real | int | float | decimal.Decimal | str
    by: literal.Real | int | float | decimal.Decimal | str
    bz: literal.Real | int | float | decimal.Decimal | str
    cx: literal.Real | int | float | decimal.Decimal | str
    cy: literal.Real | int | float | decimal.Decimal | str
    cz: literal.Real | int | float | decimal.Decimal | str
    dx: literal.Real | int | float | decimal.Decimal | str
    dy: literal.Real | int | float | decimal.Decimal | str
    dz: literal.Real | int | float | decimal.Decimal | str
    ex: literal.Real | int | float | decimal.Decimal | str
    ey: literal.Real | int | float | decimal.Decimal | str
    ez: literal.Real | int | float | decimal.Decimal | str
    fx: literal.Real | int | float | decimal.Decimal | str
    fy: literal.Real | int | float | decimal.Decimal | str
    fz: literal.Real | int | float | decimal.Decimal | str
    gx: literal.Real | int | float | decimal.Decimal | str
    gy: literal.Real | int | float | decimal.Decimal | str
    gz: literal.Real | int | float | decimal.Decimal | str
    hx: literal.Real | int | float | decimal.Decimal | str
    hy: literal.Real | int | float | decimal.Decimal | str
    hz: literal.Real | int | float | decimal.Decimal | str
    ni: (
        typing.Annotated[abc.Array, typing.Annotated[abc.Terminal, r'\d\d\d\d'], None]
        | typing.Annotated[abc.Terminal, r'']
        | collections.abc.Sequence[typing.Annotated[abc.Terminal, r'\d\d\d\d'] | str]
        | str
    ) = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates arb surface cards.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.j, literal.Integer)

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')
