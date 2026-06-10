import typing
import dataclasses

from .... import abc
from ... import literal
from ..Data import Data


class Lea(Data):
    """
    Represents lea data cards.

    Attributes:
        keyword: lea data card `LEA` symbol.
        ipht: lea data card `ipht` parameter.
        icc: lea data card `icc` parameter.
        nobalc: lea data card `nobalc` parameter.
        nobale: lea data card `nobale` parameter.
        ifbrk: lea data card `ifbrk` parameter.
        ilvden: lea data card `ilvden` parameter.
        ievap: lea data card `ievap` parameter.
        nofis: lea data card `nofis` parameter.
    """

    spaces: dict[str, abc.Terminal] = dataclasses.field(default_factory=dict)

    keyword: typing.Annotated[abc.Terminal, r'LEA'] | str = abc.Terminal[r'LEA']('LEA')
    ipht: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    icc: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    nobalc: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    nobale: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    ifbrk: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    ilvden: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    ievap: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')
    nofis: literal.Integer | literal.Jump | typing.Annotated[abc.Terminal, r''] | int | str = literal.Jump('J')

    def __post_init__(self) -> None:
        """
        Validates lea data cards.
        """

        if isinstance(self.ipht, literal.Integer) and self.ipht not in {0, 1}:
            raise abc.Error('Invalid value.', f'{self.ipht=}')

        if isinstance(self.icc, literal.Integer) and self.icc not in {0, 1, 2, 3, 4}:
            raise abc.Error('Invalid value.', f'{self.icc=}')

        if isinstance(self.nobalc, literal.Integer) and self.nobalc not in {0, 1}:
            raise abc.Error('Invalid value.', f'{self.nobalc=}')

        if isinstance(self.nobale, literal.Integer) and self.nobale not in {0, 1}:
            raise abc.Error('Invalid value.', f'{self.nobale=}')

        if isinstance(self.ifbrk, literal.Integer) and self.ifbrk not in {0, 1}:
            raise abc.Error('Invalid value.', f'{self.ifbrk=}')

        if isinstance(self.ilvden, literal.Integer) and self.ilvden not in {-1, 0, 1}:
            raise abc.Error('Invalid value.', f'{self.ilvden=}')

        if isinstance(self.ievap, literal.Integer) and self.ievap not in {0, -1, 1, 2}:
            raise abc.Error('Invalid value.', f'{self.ievap=}')

        if isinstance(self.nofis, literal.Integer) and self.nofis not in {0, 1}:
            raise abc.Error('Invalid value.', f'{self.nofis=}')
