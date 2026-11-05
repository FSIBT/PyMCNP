import typing

from ..... import abc
from ..Ssr import Ssr
from .... import literal


class Col(Ssr):
    """
    Represents col ssr data options.

    Attributes:
        keyword: col ssr data option ``r'COL'`` symbol.
        equals: col ssr data option ``r'='`` symbol.
        value: col ssr data option ``value`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'COL'] | str = abc.Terminal[r'COL']('COL')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    value: literal.Integer | int | str

    def __post_init__(self) -> None:
        """
        Validates col ssr data options.

        Raises:
            Error: Invalid value.
        """

        if self.value not in {-1, 1, 0}:
            raise abc.Error('Invalid value.', f'{self.value=}')
