import typing

from .... import abc
from ... import literal
from ..Surface import Surface


class Gq(Surface):
    """
    Represents gq surface cards.

    Attributes:
        prefix: gq surface card ``prefix`` parameter.
        j: gq surface card ``j`` parameter.
        n: gq surface card ``n`` parameter.
        keyword: gq surface card ``r'GQ'`` symbol.
        a: gq surface card ``A`` parameter.
        b: gq surface card ``B`` parameter.
        c: gq surface card ``C`` parameter.
        d: gq surface card ``D`` parameter.
        e: gq surface card ``E`` parameter.
        f: gq surface card ``F`` parameter.
        g: gq surface card ``G`` parameter.
        h: gq surface card ``H`` parameter.
        J: gq surface card ``J`` parameter.
        k: gq surface card ``K`` parameter.
    """

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    j: literal.Integer
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'GQ'] = abc.Terminal[r'GQ']('GQ')
    a: literal.Real
    b: literal.Real
    c: literal.Real
    d: literal.Real
    e: literal.Real
    f: literal.Real
    g: literal.Real
    h: literal.Real
    J: literal.Real
    k: literal.Real

    def __post_init__(self) -> None:
        """
        Validates gq surface cards.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')
