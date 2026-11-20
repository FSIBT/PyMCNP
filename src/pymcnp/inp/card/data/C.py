import typing

from .... import abc
from ... import literal
from ..Data import Data


class C(Data):
    """
    Represents c data cards.

    Attributes:
        prefix: c data card ``r'*'`` symbol.
        keyword: c data card ``r'C'`` symbol.
        suffix: c data card ``n`` parameter.
        ck: c data card ``ck`` parameter.
        t: c data card ``r'T'`` symbol.
        c: c data card ``r'C'`` symbol.
    """

    prefix: typing.Annotated[abc.Terminal, r'\*'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    keyword: typing.Annotated[abc.Terminal, r'C'] = abc.Terminal[r'C']('C')
    suffix: literal.Integer
    ck: typing.Annotated[abc.Array, literal.Real, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    nt: typing.Annotated[abc.Terminal, r'T'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    c: typing.Annotated[abc.Terminal, r'C'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates c data cards.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')

        if isinstance(self.ck, abc.Array):
            if self.prefix == '*':
                valid = len(self.ck) > 0 and self.ck[0] < 180 and self.ck[-1] == 0
            else:
                valid = len(self.ck) > 0 and self.ck[0] > -1 and self.ck[-1] == 1

            if not valid:
                raise abc.Error('Invalid value.', f'{self.ck=}')
