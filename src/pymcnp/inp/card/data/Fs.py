import typing

from .... import abc
from ... import literal
from ..Data import Data


class Fs(Data):
    """
    Represents fs data cards.

    Attributes:
        keyword: fs data card ``r'FS'`` symbol.
        suffix: fs data card ``n`` parameter.
        s: fs data card ``s`` parameter.
        t: fs data card ``r'T'`` symbol.
        c: fs data card ``r'C'`` symbol.
    """

    keyword: typing.Annotated[abc.Terminal, r'FS'] = abc.Terminal[r'FS']('FS')
    suffix: literal.Integer
    s: typing.Annotated[abc.Array, literal.Integer, None] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    t: typing.Annotated[abc.Terminal, r'T'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    c: typing.Annotated[abc.Terminal, r'C'] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')

    def __post_init__(self) -> None:
        """
        Validates fs data cards.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.suffix <= 99_999_999):
            raise abc.Error('Invalid value.', f'{self.suffix=}')

        if not isinstance(self.s, abc.Terminal) and not all(1 <= sk <= 99_999_999 for sk in self.s):
            raise abc.Error('Invalid value.', f'{self.s=}')
