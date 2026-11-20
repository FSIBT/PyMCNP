import typing

from .... import abc
from ... import literal
from ..Surface import Surface


class Sq(Surface):
    """
    Represents sq surface cards.

    Attributes:
        prefix: sq surface card ``prefix`` parameter.
        j: sq surface card ``j`` parameter.
        n: sq surface card ``n`` parameter.
        keyword: sq surface card ``r'SQ'`` symbol.
        a: sq surface card ``A`` parameter.
        b: sq surface card ``B`` parameter.
        c: sq surface card ``C`` parameter.
        d: sq surface card ``D`` parameter.
        e: sq surface card ``E`` parameter.
        f: sq surface card ``F`` parameter.
        g: sq surface card ``G`` parameter.
        x: sq surface card ``x`` parameter.
        y: sq surface card ``y`` parameter.
        z: sq surface card ``z`` parameter.
    """

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    j: literal.Integer
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'SQ'] = abc.Terminal[r'SQ']('SQ')
    a: literal.Real
    b: literal.Real
    c: literal.Real
    d: literal.Real
    e: literal.Real
    f: literal.Real
    g: literal.Real
    x: literal.Real
    y: literal.Real
    z: literal.Real

    def __post_init__(self) -> None:
        """
        Validates sq surface cards.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')
