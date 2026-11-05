import typing

from ..... import abc
from ..Dbrc import Dbrc
from .... import literal


class Endf(Dbrc):
    """
    Represents endf dbrc data options.

    Attributes:
        keyword: endf dbrc data option ``r'ENDF'`` symbol.
        equals: endf dbrc data option ``r'='`` symbol.
        nn: endf dbrc data option ``nn`` parameter.
    """

    keyword: typing.Annotated[abc.Terminal, r'ENDF'] | str = abc.Terminal[r'ENDF']('ENDF')
    equals: typing.Annotated[abc.Terminal, r'='] | typing.Annotated[abc.Terminal, r''] | str = abc.Terminal[r'']('')
    nn: literal.Integer | int | str

    def __post_init__(self) -> None:
        """
        Validates endf dbrc data options.

        Raises:
            Error: Invalid value.
        """

        if self.nn not in {71, 80}:
            raise abc.Error('Invalid value.', f'{self.nn=}')
