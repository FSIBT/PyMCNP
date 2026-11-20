import typing

from .... import abc
from ... import literal
from ..Surface import Surface


class Arb(Surface):
    """
    Represents arb surface cards.

    Attributes:
        prefix: arb surface card ``prefix`` parameter.
        j: arb surface card ``j`` parameter.
        keyword: arb surface card ``r'ARB'`` symbol.
        ax: arb surface card ``ax`` parameter.
        ay: arb surface card ``ay`` parameter.
        az: arb surface card ``az`` parameter.
        bx: arb surface card ``bx`` parameter.
        by: arb surface card ``by`` parameter.
        bz: arb surface card ``bz`` parameter.
        cx: arb surface card ``cx`` parameter.
        cy: arb surface card ``cy`` parameter.
        cz: arb surface card ``cz`` parameter.
        dx: arb surface card ``dx`` parameter.
        dy: arb surface card ``dy`` parameter.
        dz: arb surface card ``dz`` parameter.
        ex: arb surface card ``ex`` parameter.
        ey: arb surface card ``ey`` parameter.
        ez: arb surface card ``ez`` parameter.
        fx: arb surface card ``fx`` parameter.
        fy: arb surface card ``fy`` parameter.
        fz: arb surface card ``fz`` parameter.
        gx: arb surface card ``gx`` parameter.
        gy: arb surface card ``gy`` parameter.
        gz: arb surface card ``gz`` parameter.
        hx: arb surface card ``hx`` parameter.
        hy: arb surface card ``hy`` parameter.
        hz: arb surface card ``hz`` parameter.
        ni: arb surface card ``ni`` parameter.
    """

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    j: literal.Integer
    keyword: typing.Annotated[abc.Terminal, r'ARB'] = abc.Terminal[r'ARB']('ARB')
    ax: literal.Real
    ay: literal.Real
    az: literal.Real
    bx: literal.Real
    by: literal.Real
    bz: literal.Real
    cx: literal.Real
    cy: literal.Real
    cz: literal.Real
    dx: literal.Real
    dy: literal.Real
    dz: literal.Real
    ex: literal.Real
    ey: literal.Real
    ez: literal.Real
    fx: literal.Real
    fy: literal.Real
    fz: literal.Real
    gx: literal.Real
    gy: literal.Real
    gz: literal.Real
    hx: literal.Real
    hy: literal.Real
    hz: literal.Real
    ni: typing.Annotated[abc.Array, typing.Annotated[abc.Terminal, r'\d\d\d\d'], None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates arb surface cards.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')
