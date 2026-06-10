import typing
import decimal
import collections
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class C(Data):
    """
    Represents c data cards.

    Attributes:
        prefix: c data card `*` symbol.
        keyword: c data card `C` symbol.
        suffix: c data card `n` parameter.
        ck: c data card `ck` parameter.
        t: c data card `T` symbol.
        c: c data card `C` symbol.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    prefix: typing.Annotated[abc.Terminal, r'\*'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'C'] | str = abc.Terminal[r'C']('C')
    suffix: literal.Integer | int | str
    ck: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] | collections.abc.Sequence[literal.Real | int | float | decimal.Decimal | str] | str = abc.Terminal[r''](
        ''
    )
    nt: typing.Annotated[abc.Terminal, r'T'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    c: typing.Annotated[abc.Terminal, r'C'] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates c data cards.
        """

        assert isinstance(self.suffix, literal.Integer)
        assert isinstance(self.ck, (abc.Array, abc.Terminal[r'']))
        assert not isinstance(self.ck, abc.Array) or all(isinstance(c, literal.Real) for c in self.ck)

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')

        if isinstance(self.ck, abc.Array) and not (len(self.ck) > 0 and self.ck[0] > -1 and self.ck[-1] == 1):
            raise abc.Error('Invalid value.', f'{self.ck=}')
