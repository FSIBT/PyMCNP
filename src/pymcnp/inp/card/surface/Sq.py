import typing
import decimal
import dataclasses

from .... import abc
from ... import literal
from ..Surface import Surface


class Sq(Surface):
    """
    Represents sq surface cards.

    Attributes:
        prefix: sq surface card `prefix` parameter.
        j: sq surface card `j` parameter.
        n: sq surface card `n` parameter.
        keyword: sq surface card `SQ` symbol.
        a: sq surface card `A` parameter.
        b: sq surface card `B` parameter.
        c: sq surface card `C` parameter.
        d: sq surface card `D` parameter.
        e: sq surface card `E` parameter.
        f: sq surface card `F` parameter.
        g: sq surface card `G` parameter.
        x: sq surface card `x` parameter.
        y: sq surface card `y` parameter.
        z: sq surface card `z` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'[+*]'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    j: literal.Integer | int | str
    n: literal.Integer | typing.Annotated[abc.Terminal, r''] | int | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'SQ'] | str = abc.Terminal[r'SQ']('SQ')
    a: literal.Real | int | float | decimal.Decimal | str
    b: literal.Real | int | float | decimal.Decimal | str
    c: literal.Real | int | float | decimal.Decimal | str
    d: literal.Real | int | float | decimal.Decimal | str
    e: literal.Real | int | float | decimal.Decimal | str
    f: literal.Real | int | float | decimal.Decimal | str
    g: literal.Real | int | float | decimal.Decimal | str
    x: literal.Real | int | float | decimal.Decimal | str
    y: literal.Real | int | float | decimal.Decimal | str
    z: literal.Real | int | float | decimal.Decimal | str

    def __post_init__(self) -> None:
        """
        Validates sq surface cards.
        """

        assert isinstance(self.j, literal.Integer)
        assert isinstance(self.n, (literal.Integer, abc.Terminal[r'']))

        if not (1 <= self.j <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.j=}')

        if isinstance(self.n, literal.Integer) and not (1 <= self.n <= 999):
            raise abc.Error('Invalid value.', f'{self.n=}')
