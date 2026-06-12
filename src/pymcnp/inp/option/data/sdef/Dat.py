import typing
import dataclasses

from ..... import abc
from ..Sdef import Sdef
from .... import literal


class Dat(Sdef):
    """
    Represents dat sdef data options.

    Attributes:
        keyword: dat sdef data option `DAT` symbol.
        equals: dat sdef data option `equals` parameter.
        m: dat sdef data option `m` parameter.
        d: dat sdef data option `d` parameter.
        y: dat sdef data option `y` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'DAT'] | str = abc.Terminal[r'DAT']('DAT')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    m: literal.Integer | int | str
    d: literal.Integer | int | str
    y: literal.Integer | int | str

    def __post_init__(self) -> None:
        """
        Validates dat sdef data options.

        Raises:
            Error: Invalid value.
        """

        assert isinstance(self.m, literal.Integer)
        assert isinstance(self.d, literal.Integer)

        if not (1 <= self.m <= 12):
            raise abc.Error('Invalid value.', f'{self.m=}')

        if not (1 <= self.d <= 31):
            raise abc.Error('Invalid value.', f'{self.d=}')
