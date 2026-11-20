import typing

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Dat(Sdef):
    """
    Represents dat sdef data options.

    Attributes:
        keyword: dat sdef data option ``r'DAT'`` symbol.
        equals: dat sdef data option ``equals`` parameter.
        m: dat sdef data option ``m`` parameter.
        d: dat sdef data option ``d`` parameter.
        y: dat sdef data option ``y`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'DAT'] = abc.Terminal[r'DAT']('DAT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] = abc.Terminal[r'']('')
    m: literal.Integer
    d: literal.Integer
    y: literal.Integer

    def __post_init__(self) -> None:
        """
        Validates dat sdef data options.

        Raises:
            Error: Invalid value.
        """

        if not (1 <= self.m <= 12):
            raise abc.Error('Invalid value.', f'{self.m=}')

        if not (1 <= self.d <= 31):
            raise abc.Error('Invalid value.', f'{self.d=}')
