import typing
import decimal
import dataclasses

from .... import abc
from ... import literal
from ..Surface import Surface


class Gq(Surface):
    """
    Represents gq surface cards.

    Attributes:
        prefix: gq surface card `prefix` parameter.
        j: gq surface card `j` parameter.
        n: gq surface card `n` parameter.
        keyword: gq surface card `GQ` symbol.
        a: gq surface card `A` parameter.
        b: gq surface card `B` parameter.
        c: gq surface card `C` parameter.
        d: gq surface card `D` parameter.
        e: gq surface card `E` parameter.
        f: gq surface card `F` parameter.
        g: gq surface card `G` parameter.
        h: gq surface card `H` parameter.
        J: gq surface card `J` parameter.
        k: gq surface card `K` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    j: literal.Integer | int | str
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] | int | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'GQ'] | str = abc.Terminal[r'GQ']('GQ')
    a: literal.Real | int | float | decimal.Decimal | str
    b: literal.Real | int | float | decimal.Decimal | str
    c: literal.Real | int | float | decimal.Decimal | str
    d: literal.Real | int | float | decimal.Decimal | str
    e: literal.Real | int | float | decimal.Decimal | str
    f: literal.Real | int | float | decimal.Decimal | str
    g: literal.Real | int | float | decimal.Decimal | str
    h: literal.Real | int | float | decimal.Decimal | str
    J: literal.Real | int | float | decimal.Decimal | str
    k: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates gq surface cards.
        """

        assert isinstance(self.j, literal.Integer)
        assert isinstance(self.n, (literal.Integer, abc.Terminal[r'']))

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')
