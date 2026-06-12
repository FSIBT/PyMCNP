import typing
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Mgopt(Data):
    """
    Represents mgopt data cards.

    Attributes:
        keyword: mgopt data card `MGOPT` symbol.
        mcal: mgopt data card `mcal` parameter.
        igm: mgopt data card `igm` parameter.
        iplt: mgopt data card `iplt` parameter.
        isb: mgopt data card `isb` parameter.
        icw: mgopt data card `icw` parameter.
        fnw: mgopt data card `fnw` parameter.
        rim: mgopt data card `rim` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'MGOPT'] | str = abc.Terminal[r'MGOPT']('MGOPT')
    mcal: typing.Annotated[abc.Terminal, r'F|A'] | str
    igm: literal.Integer | int | str
    iplt: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    isb: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    icw: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    fnw: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    rim: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')

    def __post_init__(self) -> None:
        """
        Validates mgopt data cards.

        Raises:
            Error: Invalid value.
        """

        if isinstance(self.iplt, literal.Integer) and self.iplt not in {0, 1, 2}:
            raise abc.Error('Invalid value.', f'{self.iplt=}')

        if isinstance(self.isb, literal.Integer) and self.isb not in {0, 1, 2}:
            raise abc.Error('Invalid value.', f'{self.isb=}')
