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

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict, kw_only=True)

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    j: literal.Integer | int | str = dataclasses.field(kw_only=True)
    keyword: typing.Annotated[abc.Terminal, r'ARB'] | str = abc.Terminal[r'ARB']('ARB')
    ax: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    ay: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    az: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    bx: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    by: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    bz: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    cx: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    cy: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    cz: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    dx: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    dy: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    dz: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    ex: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    ey: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    ez: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    fx: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    fy: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    fz: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    gx: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    gy: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    gz: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    hx: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    hy: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
    hz: literal.Real | int | float | decimal.Decimal | str = dataclasses.field(kw_only=True)
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
